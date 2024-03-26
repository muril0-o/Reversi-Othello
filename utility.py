def movimento_eh_valido(tabuleiro, linha, coluna, player):
  if tabuleiro[linha][coluna] != ' ':
      return False
  direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
  for dir_linha, dir_coluna in direcoes:
      r, c = linha + dir_linha, coluna + dir_coluna
      achou_peca_oponente = False
      while 0 <= r < 8 and 0 <= c < 8 and tabuleiro[r][c] != ' ':
          if tabuleiro[r][c] == player:
              if achou_peca_oponente:
                  return True
              else:
                  break
          else:
              achou_peca_oponente = True
          r += dir_linha
          c += dir_coluna
  return False

def get_movimentos_validos(tabuleiro, player):
  movimentos_validos = []
  for linha in range(8):
      for coluna in range(8):
          if movimento_eh_valido(tabuleiro, linha, coluna, player):
              movimentos_validos.append((linha, coluna))
  return movimentos_validos

def game_over(tabuleiro):
  return len(get_movimentos_validos(tabuleiro, 'P')) == 0 and len(get_movimentos_validos(tabuleiro, 'B')) == 0

def fazer_jogada(tabuleiro, linha, coluna, player):
  tabuleiro[linha][coluna] = player
  direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
  for dir_linha, dir_coluna in direcoes:
      r, c = linha + dir_linha, coluna + dir_coluna
      while 0 <= r < 8 and 0 <= c < 8 and tabuleiro[r][c] != ' ' and tabuleiro[r][c] != player:
          r += dir_linha
          c += dir_coluna
      if 0 <= r < 8 and 0 <= c < 8 and tabuleiro[r][c] == player:
          r -= dir_linha
          c -= dir_coluna
          while r != linha or c != coluna:
              tabuleiro[r][c] = player
              r -= dir_linha
              c -= dir_coluna