import pygame
pygame.init()
import random





white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
score = 0
snake_x = 45
snake_y = 45
size = 10
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Snakes by Ahmad")
pygame.display.update()
exit_game = False
game_over = False
timer = pygame.time.Clock()
fps = 55
velocity_x = 0
velocity_y = 0
foodx = random.randint(0, 600)
foody = random.randint(0, 400)

font = pygame.font.SysFont(None, 40)
def score_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    screen.blit(screen_text, [x,y])


snk_list = []
snk_len = 1


while exit_game != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x =   5
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x =  - 5
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -5
                velocity_x = 0
                
            if event.key == pygame.K_DOWN:
                velocity_y = 5
                velocity_x = 0
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y


    if abs(snake_x - foodx) < 8 and abs(foody - snake_y) < 8:
        score += 1
        print(f"{score}")
        
        foodx = random.randint(10, 500)
        foody = random.randint(10, 300)

        snk_len += 5



    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list) > snk_len:
        del snk_list[0]




    screen.fill(white)
    score_screen("Score: "+str(score * 10), black, 5, 5)
    pygame.draw.rect(screen, red, [foodx,foody,10,10])
    
    pygame.draw.rect(screen, black, [snake_x,snake_y,size,size])
    
    
    
    pygame.display.update()



    timer.tick(fps)





pygame.quit()
quit()