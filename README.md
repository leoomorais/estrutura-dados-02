# Exercício -- Análise de Complexidade Assintótica (Big-O)

Autor: Leonardo Morais

## Exercício 1

Complexidade: **O(1)**

Justificativa: O algoritmo apenas acessa o primeiro elemento da lista.
Esse acesso ocorre em tempo constante, independentemente do tamanho da
lista.

------------------------------------------------------------------------

## Exercício 2

Complexidade: **O(n)**

Justificativa: O algoritmo percorre todos os elementos da lista uma
única vez para somá-los. O número de operações cresce proporcionalmente
ao tamanho da lista.

------------------------------------------------------------------------

## Exercício 3

Complexidade: **O(log n)**

Justificativa: A busca binária divide o espaço de busca pela metade a
cada iteração do loop. Assim, o número de passos cresce de forma
logarítmica.

------------------------------------------------------------------------

## Exercício 4

Complexidade: **O(n²)**

Justificativa: Existem dois loops aninhados que percorrem a lista. Para
cada elemento, o algoritmo compara com os demais elementos.

------------------------------------------------------------------------

## Exercício 5

Complexidade: **O(n²)**

Justificativa: O primeiro loop é O(n), mas o segundo possui dois loops
aninhados O(n²). Como consideramos o crescimento dominante, o resultado
final é O(n²).

------------------------------------------------------------------------

## Exercício 6

Complexidade: **O(log n)**

Justificativa: O valor de `i` dobra a cada iteração (i \*= 2). Isso faz
com que o número de repetições seja proporcional ao logaritmo de n.

------------------------------------------------------------------------

## Exercício 7

Complexidade: **O(2ⁿ)**

Justificativa: A implementação recursiva do Fibonacci gera duas chamadas
recursivas para cada chamada original, formando uma árvore de chamadas
exponencial.

------------------------------------------------------------------------

## Exercício 8

Complexidade: **O(n²)**

Justificativa: O Bubble Sort possui dois loops aninhados que percorrem a
lista várias vezes para comparar e trocar elementos.

------------------------------------------------------------------------

## Exercício 9

Complexidade: **O(n³)**

Justificativa: A multiplicação de matrizes utiliza três loops aninhados,
fazendo com que o número de operações cresça proporcionalmente a n³.

------------------------------------------------------------------------

## Exercício 10

Complexidade: **O(n log n)**

Justificativa: O Merge Sort divide a lista recursivamente (log n níveis)
e em cada nível realiza operações de merge que percorrem todos os
elementos (n).

------------------------------------------------------------------------

## Como executar os testes

``` bash
python algoritmosTeste.py
```
