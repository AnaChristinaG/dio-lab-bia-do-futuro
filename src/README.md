# Código da Aplicação - Passo a passo de Excecução

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Biaxar modelo leve
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
