import sys
import requests
import json

def check_ip_reputation(ip_address):
    """
    Checks the reputation of an IP address using the AbuseIPDB API.
    Note: A valid API key is required to use this script in a real environment.
    """
    api_key = 'YOUR_ABUSEIPDB_API_KEY'  # Replace with your actual API key
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    
    print(f"[*] Checking reputation for IP: {ip_address}...")
    
    try:
        # For simulation purposes, we'll mock the response if no API key is provided
        if api_key == 'YOUR_ABUSEIPDB_API_KEY':
            print("[!] API Key not configured. Using mock data for demonstration.")
            mock_response = {
                "data": {
                    "ipAddress": ip_address,
                    "abuseConfidenceScore": 85,
                    "countryCode": "US",
                    "usageType": "Data Center/Web Hosting/Content Delivery Network",
                    "isp": "DigitalOcean, LLC",
                    "domain": "digitalocean.com",
                    "totalReports": 120,
                    "lastReportedAt": "2026-03-03T10:00:00+00:00"
                }
            }
            return mock_response
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to AbuseIPDB: {e}")
        return None

def classify_risk(score):
    if score >= 75:
        return "HIGH RISK"
    elif score >= 25:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

def main():
    if len(sys.argv) < 2:
        print("Usage: python ip_reputation_checker.py <IP_ADDRESS>")
        sys.exit(1)
        
    target_ip = sys.argv[1]
    result = check_ip_reputation(target_ip)
    
    if result and 'data' in result:
        data = result['data']
        score = data.get('abuseConfidenceScore', 0)
        risk = classify_risk(score)
        
        print("-" * 30)
        print(f"IP Address: {data.get('ipAddress')}")
        print(f"Abuse Confidence Score: {score}%")
        print(f"Risk Classification: {risk}")
        print(f"Country: {data.get('countryCode')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Total Reports: {data.get('totalReports')}")
        print("-" * 30)
    else:
        print("[!] Failed to retrieve reputation data.")

if __name__ == "__main__":
    main()

