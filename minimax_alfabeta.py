import math
import utility

def calc_heuristica(tabuleiro, player):
  player_score = 0
  oponente_score = 0
  for linha in tabuleiro:
    for elemento in linha:
      if elemento == player:
        player_score += 1
      elif elemento != ' ':
        oponente_score += 1
  return player_score - oponente_score

def minimax(tabuleiro, profundidade, maximizando, player, alpha, beta):
  if profundidade == 0 or utility.game_over(tabuleiro):
    return calc_heuristica(tabuleiro, player)

  if maximizando:
    heuristica_max = -math.inf
    movimentos_validos = utility.get_movimentos_validos(tabuleiro, player)
    for movimento in movimentos_validos:
      novo_tabuleiro = [linha[:] for linha in tabuleiro]
      utility.fazer_jogada(novo_tabuleiro, movimento[0], movimento[1], player)
      heuristica = minimax(novo_tabuleiro, profundidade - 1, False, player, alpha, beta)
      heuristica_max = max(heuristica_max, heuristica)
      alpha = max(alpha, heuristica)
      if alpha >= beta:
        return alpha
    return heuristica_max
  else:
    min_heuristica = math.inf
    oponente = 'B' if player == 'P' else 'P'
    movimentos_validos = utility.get_movimentos_validos(tabuleiro, oponente)
    for movimento in movimentos_validos:
      novo_tabuleiro = [linha[:] for linha in tabuleiro]
      utility.fazer_jogada(novo_tabuleiro, movimento[0], movimento[1], oponente)
      heuristica = minimax(novo_tabuleiro, profundidade - 1, True, player, alpha, beta)
      min_heuristica = min(min_heuristica, heuristica)
      beta = min(beta, heuristica)
      if beta <= alpha:
        return beta
    return min_heuristica

def get_melhor_movimento(tabuleiro, player):
  melhor_movimento = None
  melhor_heuristica = -math.inf
  movimentos_validos = utility.get_movimentos_validos(tabuleiro, player)
  if len(movimentos_validos) == 1:
    return movimentos_validos[0]
  alpha = -math.inf
  beta = math.inf
  for movimento in movimentos_validos:
    novo_tabuleiro = [linha[:] for linha in tabuleiro]
    utility.fazer_jogada(novo_tabuleiro, movimento[0], movimento[1], player)
    heuristica = minimax(novo_tabuleiro, 5, False, player, alpha, beta)
    if heuristica > melhor_heuristica:
      melhor_heuristica = heuristica
      melhor_movimento = movimento
  return melhor_movimento