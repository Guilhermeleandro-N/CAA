# RELATÓRIO  
## PROGRAMAÇÃO DINÂMICA E DISTÂNCIA DE LEVENSHTEIN  
**S4 - Sistemas de Informação**

---

### EQUIPE:
- Emilly Jullyane de Morais Silva  
- Guilherme Leandro Nogueira  
- Maria Clara Landim Braz

---

### Descrição do Problema

O objetivo deste projeto é desenvolver, a partir da curadoria de **cinquenta palavras começadas com a letra E**, um sistema simples de correção ortográfica que sugere palavras do português corretas com base na **Distância de Levenshtein**.  

Sabe-se que erros ortográficos são muito comuns na digitação, principalmente quando não há um corretor automático para auxiliar o usuário.

---

### O que é a Distância de Levenshtein

A **Distância de Levenshtein** é uma métrica que mede o número mínimo de operações (inserções, deleções e substituições) necessárias para transformar uma string em outra.  

Um exemplo seria a distância entre as palavras *"pato"* e *"pata"*, que resulta em 1, por conta da substituição da letra *"o"* por *"a"*.

---

### Programação Dinâmica na Solução

Para evitar recomputações desnecessárias, utilizamos **Programação Dinâmica (PD)** — uma técnica que resolve problemas ao dividi-los em subproblemas menores e armazenar os resultados intermediários.  

Com isso, conseguimos calcular a Distância de Levenshtein de forma mais eficiente, com complexidade **O(m × n)**, sendo *m* e *n* os comprimentos das strings.

---

### Explicação da Solução

A solução foi implementada em **Python** e funciona da seguinte forma:

1. O usuário insere uma palavra no sistema;
2. O cálculo da Distância de Levenshtein é feito com a função `levenshtein(a, b)`, que compara a palavra digitada com as 50 palavras do dicionário pré-carregado;
3. O sistema define quais palavras são mais próximas da digitada;
4. Utilizamos um **limite de distância igual a 2**, suficiente para capturar erros comuns como trocas ou omissões de letras;
5. As palavras com distância menor ou igual a 2 são filtradas e ordenadas por distância crescente;
6. Como saída, o sistema exibe uma lista com as palavras mais próximas.

---

### Análise de Complexidade

**Tempo:**  
- A função de Levenshtein tem complexidade **O(n × m)**, onde *n* e *m* são os comprimentos das palavras;
- Como a palavra digitada é comparada com as palavras do dicionário (de tamanho *k*), a complexidade total é **O(k × n × m)**.

**Espaço:**  
- A complexidade de espaço também é **O(n × m)**, pois o algoritmo utiliza uma matriz de tamanho *(n+1) × (m+1)*.

> Vale lembrar que o algoritmo de Levenshtein **sem Programação Dinâmica** tem complexidade **O(3ⁿ)**.

---

### Conclusão

A **Distância de Levenshtein** se mostra uma abordagem eficaz para correção ortográfica simples.  

A aplicação de **Programação Dinâmica** permite que o algoritmo tenha melhor desempenho, mesmo quando aplicado a listas maiores — como no nosso caso, com as cinquenta palavras iniciadas com a letra **E**.
