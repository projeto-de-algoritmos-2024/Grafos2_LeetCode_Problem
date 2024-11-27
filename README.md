# Resolução de Problemas no LeetCode

## Visão Geral
Este repositório contém a resolução de três problemas do LeetCode, que abordam tópicos fundamentais discutidos em sala de aula, como o algoritmo de Árvore Geradora Mínima (MST) e o algoritmo de Dijkstra. Os problemas foram resolvidos utilizando essas técnicas e outros conceitos de algoritmos clássicos de grafos. Abaixo, você encontrará uma breve descrição de cada problema e o nível de dificuldade.

## Questões
1. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/) - Nível: Médio

        Descrição: Este problema busca encontrar o custo mínimo de voos entre duas cidades, com a restrição de que o número de escalas seja limitado a K. O desafio é otimizar o caminho para o destino com o custo mínimo, respeitando o número máximo de escalas. A solução foi implementada utilizando o algoritmo de Dijkstra modificado, considerando o número de escalas como uma variável adicional na otimização.

2. [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/) - Nível: Difícil

        Descrição: Este problema envolve encontrar o caminho de custo mínimo em uma grade onde cada célula tem uma direção associada. O objetivo é transformar a grade, se necessário, para que pelo menos um caminho válido de (0, 0) até (m-1, n-1) seja possível. Foi utilizado o algoritmo de BFS com modificação de custo, onde cada célula poderia ser modificada com um custo adicional para ajustar a direção e tornar o caminho válido.

3. [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/) - Nível: Difícil

        Descrição: Este problema exige que você identifique as arestas críticas e pseudo-críticas em uma árvore geradora mínima. Uma aresta crítica é aquela que, se removida, aumenta o custo da árvore geradora mínima. A solução foi implementada utilizando o algoritmo de Kruskal para Árvore Geradora Mínima, com a modificação de testar se a remoção ou inclusão forçada de uma aresta altera o custo total da árvore.

## Como executar
Para cada um desses problemas, o código foi implementado em Python e está disponível neste repositório (pasta src). Você pode executar os scripts diretamente ou adaptá-los conforme necessário para o seu ambiente de desenvolvimento. Cada problema está isolado em um arquivo de script separado, facilitando o teste individual.

## Contribuidores
<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="https://github.com/Hellen159">
                <img style="border-radius: 50%;" src="https://github.com/Hellen159.png" width="150px;"/>
                <h5 class="text-center"> <br> Hellen Faria Matrícula: 202016480 </h5>
            </a>
        </td>
      <td align="center">
            <a href="https://github.com/deboracaires">
                <img style="border-radius: 50%;" src="https://github.com/deboracaires.png" width="150px;"/>
                <h5 class="text-center"> <br> Debora Caires Matrícula: 222015103</h5>
            </a>
        </td>
    </tr>
</table>