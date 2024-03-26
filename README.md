# Jogo Reversi-Othello

Esta é uma implementação em Python do jogo Reversi-Othello. Abaixo você encontrará instruções sobre como jogar o jogo e executar o projeto.

## Como Jogar

### Objetivo
O objetivo do Reversi-Othello é ter mais peças da sua cor no tabuleiro do que o seu oponente ao final do jogo.

### Jogadores
- 2 jogadores (1 Humano VS 1 Computador)

### Peças
- 64 peças, cada uma com um lado preto e um lado branco.

### Tabuleiro
- O tabuleiro consiste em 64 quadrados.

### Início do Jogo
- O jogo começa com quatro peças colocadas no centro do tabuleiro em uma formação quadrada, com duas peças brancas e duas peças pretas. O jogador com as peças pretas faz o primeiro movimento.

### Fazendo Jogadas
- Para colocar uma peça em um quadrado, um jogador deve ter pelo menos uma linha reta (horizontal, vertical ou diagonal) entre o quadrado onde deseja colocar sua peça e outra peça sua, com uma ou mais peças do oponente entre elas.
- Quando um jogador faz uma jogada válida, todas as peças do oponente em linha reta entre a peça recém-colocada e qualquer outra peça do jogador que fez o movimento são viradas e passam a ser da cor desse jogador.

### Fim do Jogo
- O jogo termina quando nenhum dos jogadores pode fazer uma jogada, seja porque todos os quadrados estão preenchidos ou todas as peças no tabuleiro são da mesma cor.
- Se um jogador tiver mais peças que o outro, ele vence.
- Se ambos os jogadores tiverem o mesmo número de peças, o jogo termina em empate.

## Executando o Projeto

### Requisitos
- Python 3.4.2
- Biblioteca Pygame

### Passos
1. Clone ou baixe o projeto do repositório.
2. Instale a biblioteca Pygame se ainda não tiver feito. Você pode fazer isso via pip:
```
    pip install pygame
```
3. Navegue até o diretório contendo os arquivos do projeto.
4. Execute o seguinte comando para iniciar o jogo:
```
    python main.py
``` 