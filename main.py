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


PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40
player_img = pygame.transform.scale(
    pygame.image.load("ghost.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)
)

speed = 5
star_width = 35
star_height = 20


star_img = pygame.transform.scale(
    pygame.image.load("pumkin.png").convert_alpha(), (star_width, star_height)
)

font = pygame.font.SysFont("arial", 30)
big_font = pygame.font.SysFont("arial", 55)

clock = pygame.time.Clock()


def draw(player, show, stars, game_over):
    screen.blit(bg, (0, 0))
    screen.blit(player_img, player)
    for star in stars:
        screen.blit(star_img, star)
    timer_text = font.render(f"Time: {int(show)}s", True, "white")
    screen.blit(timer_text, (10, 10))
    if game_over:
        message = big_font.render("GAME OVER", True, "red")
        restart = font.render("Press R to restart", True, "white")
        screen.blit(message, message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25)))
        screen.blit(restart, restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
    pygame.display.update()


def main():
    player = pygame.Rect(400, HEIGHT - PLAYER_HEIGHT - 20, PLAYER_WIDTH, PLAYER_HEIGHT)

    run = True
    game_over = False
    started_time = time.time()
    show_time = 0

    star_add_increament = 1000
    star_count = 0
    star_vel = 5
    stars = []
    hit = False

    while run:
        dt = clock.tick(60)
        star_count += dt

        if not game_over:
            show_time = time.time() - started_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN :
                if game_over and event.key == pygame.K_r:
                    player = pygame.Rect(
                        400, HEIGHT - PLAYER_HEIGHT - 20, PLAYER_WIDTH, PLAYER_HEIGHT
                    )

                    stars.clear()
                    game_over = False
                    started_time = time.time()
                    show_time = 0
                    star_count = 0
                    star_add_increament = 1000
                    star_vel = 5
                    hit = False

        if not game_over:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.x -= speed

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.x += speed

            player.clamp_ip(screen.get_rect())

            if star_count >= star_add_increament:
                star_count = 0
                for _ in range(random.randint(1, 3)):
                    star_x = random.randint(0, WIDTH - star_width)
                    star = pygame.Rect(star_x, -star_height, star_width, star_height)
                    stars.append(star)
                star_add_increament = max(200, star_add_increament - 50)
            for star in stars[:]:
                star.y += star_vel
                if star.top > HEIGHT:
                    stars.remove(star)
                elif star.colliderect(player):
                    hit = True
                    game_over = True
                    break
        draw(player, show_time, stars, game_over)
    pygame.quit()


if __name__ == "__main__":
    main()
