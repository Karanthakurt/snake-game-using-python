import pygame
import random

x = pygame.init()
# game window
gamewindow = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
# game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 50
velocity_x = 0
velocity_y = 0
fps = 60
score = 0
init_velocity = 5
food_x = random.randint(20, 250)
food_y = random.randint(20, 250)
clock = pygame.time.Clock()

# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x) < 6 and abs(snake_x - food_x) < 6:
        score += 10
        print("score:", score * 10)
        food_x = random.randint(20, 250)
        food_y = random.randint(20, 250)

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
