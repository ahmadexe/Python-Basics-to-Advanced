import pygame
pygame.init()
gamewindow = pygame.display.set_mode((1200,600))
pygame.display.set_caption("A game")
exit_game = False
game_over = False

#creating game loop
while exit_game != True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("You pressed right arrow key.")

pygame.quit()
quit()