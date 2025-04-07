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

O objetivo deste projeto é desenvolver um sistema simples de correção ortográfica que sugere palavras do português corretas com base na **Distância de Levenshtein**. Sabemos que erros ortográficos são muito comuns na digitação, principalmente quando não há um corretor automático para o auxílio do usuário.

---

### O que é a Distância de Levenshtein

A **Distância de Levenshtein** é uma métrica que mede o número mínimo de operações (inserções, deleções e substituições) necessárias para transformar uma string em outra.  

Um exemplo seria a distância entre as palavras *"pato"* e *"pata"*, que resulta em 1, por conta da substituição da letra *"o"* por *"a"*.

---

### Programação Dinâmica na Solução

Para evitar recomputações desnecessárias, utilizamos **Programação Dinâmica (PD)**, que é uma técnica utilizada para resolver problemas quebrando-os em subproblemas menores e armazenando os resultados intermediários.  

Com isso, calculamos a Distância de Levenshtein de forma mais eficiente, com complexidade **O(m × n)**, sendo *m* e *n* os comprimentos das strings.

---

### Explicação da Solução

A solução implementada em Python funciona da seguinte forma:

1. Solicitamos ao usuário que insira uma palavra no sistema;
2. O cálculo da Distância de Levenshtein é realizado por meio da função `levenshtein(a, b)`, que compara a palavra digitada com as palavras de um dicionário pré-carregado;
3. O programa define quais palavras estão mais próximas da informada;
4. A filtragem por um limite de distância menor ou igual a um número *X* reduz o tempo de processamento e mostra sugestões relevantes;
5. Utilizamos a **distância limite 2**, pois nossa solução foca em solucionar erros comuns, como trocas ou omissões de letras;
6. Após isso, as palavras filtradas são ordenadas por distância crescente;
7. Como saída, o sistema exibe uma lista com as palavras mais próximas.

---

### Análise de Complexidade

**Tempo:**  
- A função de Levenshtein tem complexidade **O(n × m)**, onde *n* e *m* são os comprimentos das palavras;
- Como a palavra digitada é comparada com todas as palavras do dicionário, a complexidade geral é **O(k × n × m)**, onde *k* é o número de palavras no dicionário.

**Espaço:**  
- A complexidade de espaço também é **O(n × m)**, pois o algoritmo utiliza uma matriz de tamanho *(n+1) × (m+1)*.

> Vale ressaltar que o algoritmo de Levenshtein sem o uso de Programação Dinâmica tem complexidade **O(3^n)**.

---

### Conclusão

A **Distância de Levenshtein** se mostra eficaz para correção ortográfica simples.  
A **Programação Dinâmica** permitiu que o algoritmo funcionasse com melhor desempenho, mesmo com listas de palavras maiores.
