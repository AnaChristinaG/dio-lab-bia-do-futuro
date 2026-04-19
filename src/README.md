# Código da Aplicação - Passo a passo de Execução

## Estrutura Sugerida

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar modelo leve
ollama pull phi3

# 3. Testar se funciona
ollama run phi3
````

## Código Completo

Todo o código-fonte está no arquivo `app.py`


## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que o Ollama está rodando
Ollama serve

# 3. Rodar a aplicação
streamlit run .\src\app.py
```

## Evidência de Execução

<img width="1361" height="637" alt="image" src="https://github.com/user-attachments/assets/e4bebe19-eb7b-41db-be4a-b0a6f628e23d" />
