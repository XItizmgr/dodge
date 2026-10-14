import pygame
import time
import random

pygame.font.init()
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Pumpkin")
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 35
PLAYER_HEIGHT = 50

speed = 5
star_width = 10
star_height = -5
font = pygame.font.SysFont("arial", 30)
big_font = pygame.font.SysFont("arial", 55)

clock = pygame.time.Clock()


def draw(player, show, stars):

    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, "red", player)
    for star in stars:
        pygame.draw.rect(screen, "white", star)
    timer_text = font.render(f"Time: {int(show)}s", True, "white")
    screen.blit(timer_text, (10, 10))

    pygame.display.update()


def main():
    run = True
    player = pygame.Rect(400, HEIGHT - PLAYER_HEIGHT * 1.3, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    started_time = time.time()
    show_time = 0

    star_add_increament = 2000
    star_count = 0
    star_vel = 10
    stars = []
    hit = False
    while run:
        star_count += clock.tick(60)
        show_time = time.time() - started_time
        if star_count > star_add_increament:
            for _ in range(random.randint(0, 5)):
                star_x = random.randint(0, WIDTH - star_width)
                star = pygame.rect(star_x, -star_height, star_width, star_height)
                stars.append(star)
            star_add_increament = max(200, star_add_increament - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - speed >= 0:
                player.x = player.x - speed
            if keys[pygame.K_RIGHT] and player.x + speed + PLAYER_WIDTH <= WIDTH:
                player.x = player.x + speed
        for star in stars[:]:
            star.y += star_vel
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star_height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        draw(player, show_time, stars)
    pygame.quit()


if __name__ == "__main__":
    main()
