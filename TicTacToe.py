#!/usr/bin/env python3

import pygame

class TicTacToe():

  window_size = (340, 340)

  color_primary = (200, 125, 100)
  color_secondary = (150, 50, 201)

  button_size = (100, 100)

  def __init__(self):
    self.done = False

    pygame.init()
    self.window = pygame.display.set_mode(self.window_size)
    pygame.display.set_caption('Tic Tac Toe')
    self.clock = pygame.time.Clock()

  def gameloop(self):

    while self.done == False:
      self.window.fill(self.color_primary)

      btn_coord = [(10,10), (120, 10), (230, 10),
                   (10, 120), (120, 120), (230,120),
                   (10, 230), (120, 230), (230, 230)]
      rect_array = []

      for pos in btn_coord:
        rect = pygame.Rect(pos[0], pos[1], self.button_size[0], self.button_size[1])
        rect_array.append(rect)

      for rect in rect_array:
        pygame.draw.rect(self.window, self.color_secondary, rect)

      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True
        if event.type == pygame.MOUSEBUTTONUP:
          (x,y) = pygame.mouse.get_pos()

      self.clock.tick(60)



  def quit(self):
    pygame.quit()




def main():
  print('Mastermind')
  tictactoe = TicTacToe()

  tictactoe.gameloop()
  tictactoe.quit()

main()