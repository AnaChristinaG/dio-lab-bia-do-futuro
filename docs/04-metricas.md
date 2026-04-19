# Avaliação e Métricas

## Como Avaliar o Agente

A avaliação da Simaria foi realizada por meio de duas abordagens complementares:

1. **Testes estruturados: cenários definidos para validar cálculos e respostas;
2. **Testes práticos: simulações reais de uso com base no perfil do cliente fictício.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | PInformar valor e prazo e validar cálculo da parcela |
| **Segurança** | Se o agente evita inventar dados | Perguntar algo fora do escopo e verificar resposta |
| **Coerência** | Se a análise respeita a renda do cliente | Avaliar se alerta quando ultrapassa 30% da renda |

> [!TIP]
> Os testes consideram o perfil fictício do cliente João Silva, com renda mensal de R$ 5.000 e gastos médios de R$ 2.488.

---

## Exemplos de Cenários de Teste

### Teste 1: Simulação de empréstimo viável
- **Pergunta:** "Quero um empréstimo de 10000 em 12 meses"
- **Resposta esperada:** Parcela calculada corretamente e comprometimento abaixo de 30% `perfil_investidor.json`
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Empréstimo com alto comprometimento
- **Pergunta:** "Quero um empréstimo de 20000 em 12 meses"
- **Resposta esperada:** Alerta de risco financeiro (acima de 30%)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "O que é criptomoeda?"
- **Resposta esperada:** Agente esclarece a dúvida de forma sucinta e informa que seu foco é simulação de empréstimos
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Dados insuficientes
- **Pergunta:** "Quero fazer um empréstimo"
- **Resposta esperada:** Solicitação de mais informações (valor e prazo)
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Cálculo de parcelas consistente com base na taxa definida;
- Respostas claras e objetivas;
- Boa adaptação ao perfil financeiro do cliente;
- Capacidade de orientar o usuário sobre riscos de endividamento.

**O que pode melhorar:**
- Interpretação mais avançada de linguagem natural;
- Integração com modelos de IA para respostas mais dinâmicas;
- Personalização mais profunda com base em histórico financeiro;
- Interface mais interativa e visual.

---

## Métricas Avançadas

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Tempo de resposta da aplicação;
- Taxa de erro nas requisições;
- Monitoramento de interações do usuário;
- Integração com ferramentas como LangFuse para observabilidade.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
