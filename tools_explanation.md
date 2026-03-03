# Explicação das Ferramentas Utilizadas no Projeto SOC Threat Detection Lab

Este documento detalha as ferramentas utilizadas na simulação do laboratório de detecção de ameaças SOC, explicando a função de cada uma e o motivo de sua escolha para este projeto.

## 1. Wazuh (SIEM - Security Information and Event Management)

*   **O que é:** Wazuh é uma plataforma de segurança de código aberto que unifica recursos de SIEM, EDR (Endpoint Detection and Response) e XDR (Extended Detection and Response). Ele coleta, agrega, indexa e analisa dados de segurança de diversos endpoints e sistemas, fornecendo visibilidade sobre eventos de segurança, detecção de ameaças, monitoramento de integridade de arquivos, avaliação de vulnerabilidades e conformidade.
*   **Por que foi usado:** No contexto deste laboratório, o Wazuh é fundamental para simular o papel de um SIEM em um SOC real. Ele é responsável por:
    *   **Coleta de Logs:** Ingerir os logs de autenticação do servidor Linux vítima.
    *   **Detecção de Ameaças:** Aplicar regras pré-definidas para identificar padrões de ataque, como múltiplas falhas de login SSH (ataque de força bruta).
    *   **Geração de Alertas:** Notificar sobre atividades suspeitas, permitindo que um analista de SOC investigue o incidente.
    *   **Visibilidade:** Fornecer uma interface centralizada para visualizar eventos de segurança e alertas.

## 2. VirtualBox (Plataforma de Virtualização)

*   **O que é:** VirtualBox é um software de virtualização de código aberto da Oracle que permite criar e executar máquinas virtuais (VMs) em um sistema operacional host. Cada VM funciona como um computador independente, com seu próprio sistema operacional e recursos alocados.
*   **Por que foi usado:** A virtualização é essencial para criar um ambiente de laboratório isolado e seguro. O VirtualBox permite:
    *   **Isolamento:** Separar o ambiente de ataque e defesa do sistema operacional principal, evitando riscos reais.
    *   **Flexibilidade:** Criar múltiplas máquinas virtuais (Kali Linux, servidor Linux vítima, máquina Wazuh) para simular diferentes componentes de uma rede real.
    *   **Reprodução:** Facilitar a reprodução do cenário de ataque e a reconfiguração do ambiente conforme necessário.
    *   **Custo-benefício:** É uma solução gratuita e amplamente utilizada para ambientes de teste e aprendizado.

## 3. Kali Linux (Sistema Operacional para Testes de Penetração)

*   **O que é:** Kali Linux é uma distribuição Linux baseada em Debian, desenvolvida especificamente para testes de penetração, auditoria de segurança e forense digital. Ele vem pré-carregado com centenas de ferramentas de segurança.
*   **Por que foi usado:** No laboratório, o Kali Linux desempenha o papel da máquina do atacante. Ele foi escolhido por:
    *   **Ferramentas Integradas:** Possuir ferramentas como o Hydra (para ataques de força bruta) já instaladas e configuradas, simplificando a simulação do ataque.
    *   **Realismo:** Simular um atacante real que utilizaria um sistema operacional e ferramentas dedicadas para atividades maliciosas.
    *   **Facilidade de Uso:** Ser uma plataforma conhecida e documentada na comunidade de segurança para a execução de testes de segurança.

## 4. Python (Linguagem de Programação para Automação)

*   **O que é:** Python é uma linguagem de programação de alto nível, interpretada, de propósito geral, conhecida por sua sintaxe clara e legibilidade. É amplamente utilizada em desenvolvimento web, análise de dados, inteligência artificial e automação de segurança.
*   **Por que foi usado:** O Python foi incluído para demonstrar a capacidade de automação dentro de um SOC. O script `ip_reputation_checker.py` exemplifica como Python pode ser usado para:
    *   **Proatividade:** Automatizar tarefas repetitivas, como a consulta de reputação de IPs suspeitos.
    *   **Integração:** Interagir com APIs externas (como AbuseIPDB) para enriquecer dados de incidentes.
    *   **Melhoria Contínua:** Adicionar funcionalidades personalizadas que podem agilizar a resposta a incidentes e a tomada de decisões.
    *   **Flexibilidade:** Ser uma linguagem versátil que pode ser adaptada para diversas necessidades de automação em segurança.

## 5. MITRE ATT&CK (Base de Conhecimento de Táticas e Técnicas de Adversários)

*   **O que é:** MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) é uma base de conhecimento globalmente acessível de táticas e técnicas de adversários baseadas em observações do mundo real. Ele serve como um catálogo de comportamentos de atacantes que podem ser usados para melhorar a detecção de ameaças, a análise de segurança e o desenvolvimento de defesas.
*   **Por que foi usado:** O mapeamento MITRE ATT&CK é uma prática essencial em SOCs modernos e foi incluído para:
    *   **Padronização:** Fornecer uma linguagem comum para descrever o comportamento do atacante, facilitando a comunicação interna e externa.
    *   **Análise Aprofundada:** Ajudar a entender as táticas e técnicas específicas utilizadas no ataque de força bruta (T1110 sob a tática de Acesso a Credenciais TA0006).
    *   **Maturidade Profissional:** Demonstrar a capacidade de um analista de SOC de contextualizar um incidente dentro de um framework reconhecido globalmente, o que é altamente valorizado por recrutadores.
    *   **Melhoria da Defesa:** Informar o desenvolvimento de estratégias de detecção e mitigação mais eficazes, cobrindo lacunas de segurança com base em comportamentos de atacantes conhecidos.
