import pygame

x = pygame.init()
# game window
gamewindow = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

# game specific variables
exit_game = False
game_over = False

# game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        # event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("you have pressed right key")

                if event.type == pygame.quit:
                    exit_game = True

    pygame.quit()
    quit()
