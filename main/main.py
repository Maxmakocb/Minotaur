import pygame
from graphics.window import Window, WindowConfig
import time


def main():
    pygame.init()
    Window(WindowConfig())

    background = pygame.image.load("../cat.jpg")

    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # RGB colors
        screen.fill((234, 0, 0))
        # background image
        screen.blit(background, (0, 0))

        # update display
        pygame.display.flip()


if __name__ == "__main__":
    main()
