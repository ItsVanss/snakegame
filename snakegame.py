import pygame
import random

WIDTH = 1000
HEIGHT = 600
FPS = 15

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

LEVEL_SPEEDS = {
    "gampang": 10,
    "mayan": 15,
    "wangel": 25,
    "wangelpoll": 40
}

title_font = pygame.font.Font(None, 72)

def select_level():
    selected = False
    level = "mayan"

    while not selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level = "gampang"
                    selected = True
                elif event.key == pygame.K_2:
                    level = "mayan"
                    selected = True
                elif event.key == pygame.K_3:
                    level = "wangel"
                    selected = True
                elif event.key == pygame.K_4:
                    level = "wangelpoll"
                    selected = True

        screen.fill((0, 0, 0))
        title_text = title_font.render("Uler Uleran", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_text, title_rect)

        font = pygame.font.Font(None, 36)
        text = font.render("Milih Level Disik:", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        text_gampang = font.render("1 - Gampang", True, (0, 255, 0))  
        text_mayan = font.render("2 - Mayan", True, (0, 0, 255))  
        text_wangel = font.render("3 - Wangel", True, (255, 0, 0))  
        text_wangelpoll = font.render("4 - Wangel Poll", True, (0, 0, 128))  

        text_rect_gampang = text_gampang.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        text_rect_mayan = text_mayan.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        text_rect_wangel = text_wangel.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        text_rect_wangelpoll = text_wangelpoll.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

        screen.blit(text_gampang, text_rect_gampang)
        screen.blit(text_mayan, text_rect_mayan)
        screen.blit(text_wangel, text_rect_wangel)
        screen.blit(text_wangelpoll, text_rect_wangelpoll)

        pygame.display.update()

    return level

def start_game():
    x = WIDTH // 2
    y = HEIGHT // 2

    direction = "RIGHT"

    body = [(x, y)]

    fruit = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10))

    level = select_level()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        if direction == "UP":
            y -= 10
        elif direction == "DOWN":
            y += 10
        elif direction == "LEFT":
            x -= 10
        elif direction == "RIGHT":
            x += 10

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False

        if (x, y) in body[:-1]:
            running = False

        body.append((x, y))

        if abs(x - fruit[0]) < 10 and abs(y - fruit[1]) < 10:
            fruit = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10))
        else:
            body.pop(0)

        screen.fill((0, 0, 0))
        for segment in body:
            pygame.draw.rect(screen, (255, 0, 0), (*segment, 10, 10))
        pygame.draw.rect(screen, (0, 255, 0), (*fruit, 10, 10))
        pygame.display.update()
        clock.tick(LEVEL_SPEEDS[level])

    game_over()

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

    new_game = None  

    while new_game is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_n:
                    new_game = True  

    if new_game: 
        start_game()
    else:
        select_level()

start_game()
