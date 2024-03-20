import random
import pygame
import pygame.freetype  # Importa o módulo freetype.

font_size = 20


# Define os possíveis estados para cada espaço
EMPTY = ' '
WHITE = 'W'
BLACK = 'B'

# Cria um tabuleiro 8x8 inicializado com todos os espaços vazios
board = [[EMPTY for _ in range(8)] for _ in range(8)]

# Inicia o jogo com quatro peças no centro do tabuleiro
board[3][3] = board[4][4] = WHITE
board[3][4] = board[4][3] = BLACK

# Define as cores para cada estado
colors = {
    EMPTY: (155, 155, 155),  # Cinza para EMPTY (Fundo do tabuleiro)
    WHITE: (255, 255, 255),  # Jogador branco
    BLACK: (0, 0, 0),  # Jogador preto
}

# Inicializa o Pygame
pygame.init()

# Define a largura e a altura de cada localização da grade
width, height = 60, 60

# Define o tamanho da grade
grid = [width + 5, height + 5]

# Define o tamanho da janela
size = [grid[0] * 8, grid[1] * 8]
screen = pygame.display.set_mode(size)

# Define o título da tela
pygame.display.set_caption("Reversi-Othello Game")

done = False

# Usado para gerenciar a velocidade de atualização da tela
clock = pygame.time.Clock()

# Cria um objeto de fonte
font = pygame.freetype.SysFont(None, 24)

# Define quem começa
turn = random.choice([WHITE, BLACK])

def is_valid_move(board, row, col, player):
  if board[row - 5][col - 5] != EMPTY:
      return False
  
  opponent = WHITE if player == BLACK else BLACK
  
  # Verifica todas as direções
  for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
      r, c = row + dr, col + dc
  
      # Move na direção atual enquanto a posição estiver dentro do tabuleiro e contiver uma peça do oponente
      if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
          while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
              r, c = r + dr, c + dc
  
          # Se a posição estiver dentro do tabuleiro e contiver uma peça do jogador, então o movimento é válido
          if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
              return True
  
  return False


def make_move(board, row, col, player):
    # Coloca a peça no tabuleiro
    board[row - 5][col - 5] = player
    # Vira as peças do oponente
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        r, c = row + dr, col + dc
        # Move na direção atual enquanto a posição estiver dentro do tabuleiro e contiver uma peça do oponente
        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == (WHITE if player == BLACK else BLACK):
            r, c = r + dr, c + dc
        # Se a posição estiver dentro do tabuleiro e contiver uma peça do jogador, então vira as peças do oponente
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == (WHITE if player == BLACK else BLACK):
                board[r][c] = player
                r, c = r + dr, c + dc

def game_over(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def get_winner(board):
    white_pieces = sum(row.count(WHITE) for row in board)
    black_pieces = sum(row.count(BLACK) for row in board)
    if white_pieces > black_pieces:
        return WHITE
    elif black_pieces > white_pieces:
        return BLACK
    else:
        return None

# Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            # Obtém a posição do mouse
            pos = pygame.mouse.get_pos()

            # Converte a posição do mouse em coordenadas do grid
            column = pos[0] // width
            row = pos[1] // height

            if is_valid_move(board, row, column, turn):
                make_move(board, row, column, turn)

                # Troca o turno
                turn = BLACK if turn == WHITE else WHITE

    # Define o fundo da tela
    screen.fill((0, 0, 0))

    # Cria o gradeado
    for row in range(8):
        for column in range(8):
            color = colors[board[row][column]]
            pygame.draw.rect(screen, color, [width * column, height * row, width, height])

    # Desenha o gradeado
    for x in range(0, size[0], width):
        pygame.draw.line(screen, (0,0,0), (x,0), (x,size[1]), 2)
    for y in range(0, size[1], height):
        pygame.draw.line(screen, (0,0,0), (0,y), (size[0],y), 2)

    # Escreve a linha e as colunas
    font = pygame.font.Font(None, font_size)

    for i in range(8):
            # Rótulos das colunas (letras)
        col_label = font.render(chr(65 + i), True, (200, 200, 200))
        col_label_rect = col_label.get_rect(center=(width * i + width // 2, font_size // 2 + 488))
        screen.blit(col_label, col_label_rect)

        # Rótulos das linhas (números)
        row_label = font.render(str(1 + i), True, (200, 200, 200))
        row_label_rect = row_label.get_rect(center=(font_size // 2 + 488, height * i + height // 2))
        screen.blit(row_label, row_label_rect)

    # Verifica se o jogo terminou
    if game_over(board):
        winner_color = get_winner(board)
        if winner_color == WHITE:
            winner = "Branco venceu!"
        elif winner_color == BLACK:
            winner = "Preto venceu!"
        else:
            winner = "Empate!"        
        
      # Escreve o Vencedor na tela
        font.render_to(screen, (size[0] // 2, size[1] // 2), winner, (200, 200, 200))

    # FPS
    clock.tick(60)

    # Atualiza o display
    pygame.display.flip()

pygame.quit()