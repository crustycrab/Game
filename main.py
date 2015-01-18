import pygame
from pygame.locals import *

from Game import colors


def main():
    pygame.init()
    fps_clock = pygame.time.Clock()

    window = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Test Game')

    running = True

    while running:
        window.fill(colors.BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            pygame.display.update()
            fps_clock.tick()

    pygame.quit()


if __name__ == '__main__':
    main()