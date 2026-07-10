import pygame
from game.game import Game

def main():
    """Main game function"""
    pygame.init()

    game = Game()
    game.run()

    pygame.quit()

if __name__ == '__main__':
    main()