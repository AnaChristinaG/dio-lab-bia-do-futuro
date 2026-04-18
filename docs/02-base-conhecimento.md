# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar dúvidas e interações anteriores do cliente |
| `perfil_investidor.json` | JSON | Personalizar simulações com base em renda, perfil e objetivos |
| `produtos_financeiros.json` | JSON | Apoiar explicações financeiras e contextualizar decisões |
| `transacoes.csv` | CSV | Analisar padrão de gastos e estimar capacidade de pagamento |

---

## Adaptações nos Dados

> Os dados mockados foram utilizados como base e complementados com regras simples de negócio, como definição de taxa de juros e prazos para simulação de empréstimos. Também foi realizada uma análise das transações para calcular a média de gastos mensais e estimar a renda disponível do cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Os arquivos JSON e CSV são carregados no início da execução do sistema utilizando Python. As informações são processadas e organizadas em variáveis estruturadas, que são utilizadas ao longo da interação com o usuário.


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
Os dados do cliente são utilizados para enriquecer o contexto das respostas, permitindo que o agente gere explicações personalizadas. Parte das informações pode ser inserida no prompt como contexto, enquanto outras são usadas diretamente na lógica de cálculo antes da geração da resposta.


```text
Perfil do cliente:
- Nome: João Silva
- Idade: 32 anos
- Renda mensal: R$ 5.000
- Perfil: Moderado

Transações:
- Gastos médios mensais: R$ 2.488

Parâmetros da simulação:
- Valor solicitado: R$ 10.000
- Prazo: 12 meses
- Taxa: 2% ao mês

````
---

## Exemplo de Contexto Montado

> O exemplo de contexto montado abaixo, se baseia em dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relenvantes, otimizando o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é para ter todas as informações relevantes disponíveis em seu contexto.

```text
Dados do Cliente:
- Nome: João Silva
- Idade: 32 anos
- Renda mensal: R$ 5.000
- Gastos médios mensais: R$ 2.488
- Perfil: Moderado
- Objetivo: Construir reserva de emergência

Simulação solicitada:
- Valor do empréstimo: R$ 10.000
- Prazo: 12 meses
- Taxa de juros: 2% ao mês

Análise:
- Parcela estimada: R$ 945
- Comprometimento da renda: ~19%
```
