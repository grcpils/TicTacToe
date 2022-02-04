#!/usr/bin/env python3

import pygame

class TicTacToe():

  window_size = (340, 380)

  color_background = (230, 230, 230)
  color_empty = (200, 200, 200)

  button_size = (100, 100)

  game_array = []

  def __init__(self, player1, player2):

    print(player1 + " VS " + player2)
    self.players = {
      "player1": player1,
      "player2": player2
    }
    self.players_color = {
      "player1": (20, 120, 245),
      "player2": (245, 140, 20)
    }

    self.current_player = "player1"

    self.done = False
    self.winner = ""

    pygame.init()
    self.window = pygame.display.set_mode(self.window_size)
    pygame.display.set_caption('Tic Tac Toe')
    self.clock = pygame.time.Clock()

  def gameloop(self):

    self.init_game_dictionnary()

    while self.done == False:
      self.window.fill(self.color_background)

      text_font = pygame.font.SysFont('Corbel', 43)
      player_text = text_font.render(self.players[self.current_player], True, self.players_color[self.current_player])

      self.window.blit(player_text, (10, 10))

      for dict in self.game_array:
        pygame.draw.rect(self.window, dict["color"], dict["rect"])

      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True
        if event.type == pygame.MOUSEBUTTONUP:
          x,y = pygame.mouse.get_pos()
          self.button_click(x, y)

      self.clock.tick(60)

  def swap_players(self):
    if self.current_player == "player1":
      self.current_player = "player2"
    else:
      self.current_player = "player1"

  def init_game_dictionnary(self):
    btn_coord = [(10,50), (120, 50), (230, 50),
                   (10, 160), (120, 160), (230,160),
                   (10, 270), (120, 270), (230, 270)]

    for pos in btn_coord:
      rect = pygame.Rect(pos[0], pos[1], self.button_size[0], self.button_size[1])
      dict = {
        "rect": rect,
        "color": self.color_empty,
        "player": -1
      }
      self.game_array.append(dict)

  def button_click(self, x, y):
    for dict in self.game_array:
      if dict["rect"].collidepoint(x, y) == True and dict["player"] == -1:
        dict["player"] = self.current_player
        dict["color"] = self.players_color[self.current_player]
        self.check_victory()
        self.swap_players()

  # [0][1][2]
  # [3][4][5]
  # [6][7][8]

  def check_victory(self):
    if (self.game_array[0]["player"] == self.game_array[1]["player"] == self.game_array[2]["player"] != -1 or # top line
        self.game_array[3]["player"] == self.game_array[4]["player"] == self.game_array[5]["player"] != -1 or # middle line
        self.game_array[6]["player"] == self.game_array[7]["player"] == self.game_array[8]["player"] != -1 or # bottom line
        self.game_array[0]["player"] == self.game_array[3]["player"] == self.game_array[6]["player"] != -1 or # left column
        self.game_array[1]["player"] == self.game_array[4]["player"] == self.game_array[7]["player"] != -1 or # middle column
        self.game_array[2]["player"] == self.game_array[5]["player"] == self.game_array[8]["player"] != -1 or # right column
        self.game_array[0]["player"] == self.game_array[4]["player"] == self.game_array[8]["player"] != -1 or # top left to bottom right
        self.game_array[6]["player"] == self.game_array[4]["player"] == self.game_array[2]["player"] != -1): # bottom left to top right
      self.winner = self.players[self.current_player]
      self.done = True

  def quit(self):
    print("Well done " + self.winner + " !!")
    pygame.quit()




def main():
  print('TicTacToe')
  player1, player2 = "", ""

  while player1 == "":
    player1 = str(input("Pseudo player 1: "))
  while player2 == "":
    player2 = str(input("Pseudo player 2: "))

  tictactoe = TicTacToe(player1, player2)
  tictactoe.gameloop()
  tictactoe.quit()

main()