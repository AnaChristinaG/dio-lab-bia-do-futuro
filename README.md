# 💸 Simaria — Assistente Inteligente de Empréstimos

> Agente financeiro com IA Generativa desenvolvido como solução para o Lab **"Bia do Futuro"** da [DIO](https://www.dio.me/).

**Simaria** (Simulador de Empréstimos com IA) é uma assistente virtual consultiva que ajuda o usuário a entender o impacto real de um empréstimo no seu orçamento — calculando parcelas, analisando comprometimento de renda e orientando com clareza, segurança e sem jargões.

---

## 🤖 Sobre a Simaria

| | |
|---|---|
| **Problema resolvido** | Usuários tomam decisões de empréstimo sem entender o impacto financeiro real |
| **Solução** | Simulação interativa com cálculo de parcelas e análise de comprometimento de renda |
| **Público-alvo** | Clientes bancários com pouca familiaridade com termos financeiros |
| **Tom de voz** | Consultivo, humanizado e educativo |
| **Interface** | Streamlit |
| **LLM** | Ollama (API local) |

---

## 🧠 Comportamento do Agente

A Simaria segue regras claras de segurança e anti-alucinação:

- Responde **apenas com base nos dados fornecidos** — nunca inventa valores ou taxas
- Considera **saudável** um comprometimento de até **30% da renda mensal**
- Alerta o usuário quando o empréstimo representa risco de endividamento
- Recusa compartilhar dados sensíveis ou de terceiros
- Solicita mais informações quando o contexto é insuficiente

---

## 📁 Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md
├── 📁 data/                          # Dados mockados do cliente fictício
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json        # João Silva — renda R$ 5.000/mês
│   ├── produtos_financeiros.json
│   └── transacoes.csv
│
├── 📁 docs/                          # Documentação completa da solução
│   ├── 01-documentacao-agente.md     # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # System prompt e exemplos (few-shot)
│   ├── 04-metricas.md                # Avaliação, testes e formulário de feedback
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py
│
└── 📁 assets/                        # Imagens e diagramas
```

---

## 📚 Documentação

| # | Arquivo | Conteúdo |
|---|---------|----------|
| 01 | `docs/01-documentacao-agente.md` | Caso de uso, persona da Simaria e arquitetura do sistema |
| 02 | `docs/02-base-conhecimento.md` | Estratégia de uso dos dados mockados |
| 03 | `docs/03-prompts.md` | System prompt, exemplos de interação e aprendizados |
| 04 | `docs/04-metricas.md` | Cenários de teste, resultados e formulário de feedback |
| 05 | `docs/05-pitch.md` | Roteiro do pitch de apresentação |

---

## 🛠️ Tecnologias

| Categoria | Ferramenta |
|-----------|------------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (API local) |
| Linguagem | Python |
| Dados | JSON e CSV (dados mockados) |

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/AnaChristinaG/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run src/app.py
```

---

## 👩‍💻 Autora

Desenvolvido por **Ana Christina G.** como entrega do Lab **"Bia do Futuro"** — DIO.

<img width="1358" height="640" alt="Simaria 00" src="https://github.com/user-attachments/assets/1fff4078-38cf-4f5c-a830-8b1a5b5a05a1" />


[![GitHub](https://img.shields.io/badge/GitHub-AnaChristinaG-181717?style=flat&logo=github)](https://github.com/AnaChristinaG)
