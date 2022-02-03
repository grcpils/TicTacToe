#!/usr/bin/env python3

import pygame

class Mastermind():

  window_size = (720, 480)

  color_primary = (200, 125, 100)
  color_secondary = (150, 50, 201)

  def __init__(self):
    self.done = False

    pygame.init()
    self.window = pygame.display.set_mode(self.window_size)
    pygame.display.set_caption('Mastermind')
    self.clock = pygame.time.Clock()

  def gameloop(self):

    while self.done == False:
      self.window.fill(self.color_primary)

      button_size = (160, 40)
      button_pos = ((self.window_size[0]/2) - button_size[0]/2, (self.window_size[1]/2) - button_size[1]/2)

      pygame.draw.rect(self.window, self.color_secondary, pygame.Rect(button_pos[0], button_pos[1], button_size[0], button_size[1]))

      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True

      self.clock.tick(60)

  def quit(self):
    pygame.quit()


def main():
  print('Mastermind')
  mastermind = Mastermind()

  mastermind.gameloop()
  mastermind.quit()

main()