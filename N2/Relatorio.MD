RELATÓRIO:
PROGRAMAÇÃO DINÂMICA E DISTÂNCIA DE LEVENSHTEIN
S4 - Sistemas de Informação

EQUIPE:
Emilly Jullyane de Morais Silva
Guilherme Leandro Nogueira
Maria Clara Landim Braz
Descrição de problema
O objetivo deste projeto é desenvolver um sistema simples de correção ortográfica que sugere palavras do português corretas com base na Distância de Levenshtein. Sabemos que erros ortográficos são muito comuns na digitação, principalmente quando não há um corretor automático para o auxílio do usuário, com isso fizemos a curadoria de cinquenta palavras começadas com a letra E.

O que é a Distância de Levenshtein
A Distância de Levenshtein é uma métrica que mede o número mínimo de operações (inserções, deleções e substituições) necessárias para transformar uma string em outra. Um exemplo seria a distância da palavra “pato” e “pata”, que resulta em 1, por conta da substituição da letra “o” por “a”.

Programação Dinâmica na Solução
Para evitar recomputações desnecessárias, utilizamos Programação Dinâmica (PD), que é uma técnica utilizada para resolver problemas quebrando-os em subproblemas menores e guardando os resultados intermediários para que os cálculos não sejam repetidos. Com isso, calculamos a Distância de Levenshtein de forma mais eficiente, com complexidade O(m × n), sendo m e n os comprimentos das strings.

Explicação da solução
A solução implementada em Python funciona da seguinte forma:
Solicitamos ao usuário que ele faça a entrada de uma palavra no sistema;
O cálculo da Distância de Levenshtein, funciona utilizando da função levenshtein(a, b) para comparar a palavra digitada com as palavras de um dicionário pré-carregado. Com isso, o programa define quais as palavras mais próximas da informada.
A filtragem por um limite de distância menor ou igual a um número X reduz o tempo de processamento e mostra sugestões relevantes de palavras. 
Utilizamos a distância limite 2, pois a nossa solução foca em solucionar erros comuns, como trocas ou omissões de letras. Logo, a distância 2 é suficiente para este tipo de  problema.
Após isso, as palavras filtradas são ordenadas por distância crescente;
Como saída, o sistema exibe uma lista com as palavras mais próximas.. 

Análise de complexidade
A análise de complexidade baseia-se em:
Tempo:
A função de Levenshtein tem complexidade O(n × m);
n e m são os comprimentos das duas palavras;
Como a palavra digitada é comparada com as palavras do dicionário, temos  O(k × n × m) como complexidade geral do sistema.

Espaço:
A complexidade de espaço, assim como a de tempo, também é O(n × m);
A matriz utilizada pelo algoritmo possui tamanho (n+1) × (m+1), o que gera a complexidade de espaço, citada acima.

Vale ressaltar que o algoritmo de Levenshtein sem o uso da Programação Dinâmica tem complexidade O(3^n).

Conclusão
A Distância de Levenshtein se mostra eficaz para correção ortográfica simples. A Programação Dinâmica permitiu que o algoritmo funcionasse com melhor desempenho, mesmo com listas de palavras maiores.
