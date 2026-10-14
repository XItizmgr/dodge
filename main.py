import pygame
import time
import random

pygame.init()

WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Pumpkin")
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60


def draw(player):
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, "red", player)
    pygame.display.update()


def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT * 1.3, PLAYER_WIDTH, PLAYER_HEIGHT)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(player)
    pygame.quit()


if __name__ == "__main__":
    main()
