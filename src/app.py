import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "phi3"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ CÁLCULOS FINANCEIROS ============
gastos = transacoes[transacoes['tipo'] == 'saida']['valor'].sum()
renda = perfil['renda_mensal']
renda_disponivel = renda - gastos

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos
RENDA: R$ {perfil['renda_mensal']}
GASTOS MENSAIS: R$ {gastos:.2f}
RENDA DISPONÍVEL: R$ {renda_disponivel:.2f}
PERFIL DE CRÉDITO: {perfil['perfil_credito']}
OBJETIVO: {perfil['objetivo']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SIMULAÇÃO DE EMPRÉSTIMO ============
def simular_emprestimo(valor, prazo, taxa=0.02):
    parcela = (valor * (1 + taxa) ** prazo) / prazo
    comprometimento = parcela / renda

    return {
        "parcela": parcela,
        "comprometimento": comprometimento
    }
    
    
# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais.
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}
    """

    try:
        r = requests.post(
            OLLAMA_URL,
            json={"model": MODELO, "prompt": prompt, "stream": False}
        )

        data = r.json()

        if "response" not in data:
            return f"Erro na resposta do modelo:\n{data}"

        return data["response"]

    except Exception as e:
        return f"Erro ao conectar com o modelo: {e}"


# ============ INTERFACE ============
st.title("💰 Simaria, Sua Assistente de Empréstimos")

if pergunta := st.chat_input("Digite sua simulação ou dúvida financeira..."):
    st.chat_message("user").write(pergunta)
    
    with st.spinner("Analisando sua situação financeira..."):
        st.chat_message("assistant").write(perguntar(pergunta))
