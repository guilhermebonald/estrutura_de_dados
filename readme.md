
# Documentação sobre "Lista Encadeada"

- Uma __Lista Encadeada__ começa pelo __Nó__, que representa cada __elemento individual__ de uma __lista__. Cada __Nó__ é acompanhado por um __ponteiro__, cada __Nó__ é __carregado__ com uma __valor__ e ocupa um __espaço__ na __memória__. Cada __ponteiro__ é  carregado com o valor do proximo __nó__ exceto o __último__ da lista que é sempre __Null__ e ocupa um espaço em __memória__ que __aponta__ para um possivel novo nó.
- Um ponteiro não tem o mesmo valor do próximo nó, mas sim o valor do endereço de memória do próximo nó. Um endereço de memória é um número que identifica uma posição na memória onde um dado está armazenado. Um ponteiro é uma variável que guarda um endereço de memória como seu valor.

- Listas encadeadas são a forma mais simples de estrutura de dados dinâmica. Em uma lista, os elementos não são armazenados contiguamente, como acontece em arranjos. Nelas, cada elemento é armazenado separadamente, e possui valor (o dado que desejamos acessar) e um ponteiro para o próximo elemento. Um ponteiro (ou apontador) é uma variável que armazena o endereço de outra variável (eles referenciam outra variável). No caso de listas encadeadas, um ponteiro armazena o endereço do próximo elemento da lista. Para percorrermos a lista, basta seguirmos os ponteiros ao longo dela.

- A flexibilidade de listas encadeadas não vem de graça. Listas encadeadas possuem duas desvantagens principais. Primeiro, precisamos de espaço adicional para armazenar os ponteiros. Segundo, se quisermos acessar um elemento em uma dada posição da lista, precisamos percorrer todos os elementos anteriores a ele na lista.
## Referência

 - [Listas Encadeadas](https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/listas-encadeadas/)
 
