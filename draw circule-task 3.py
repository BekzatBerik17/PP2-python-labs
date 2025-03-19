import pygame 

pygame.init()

weid,heigh = 600,600

screen = pygame.display.set_mode((weid,heigh))
pygame.display.set_caption("ball")
screen.fill((255,255,255))

center_for_ball = [300,300]
raduis = 30

run = True
while run :
    pygame.draw.circle(screen,(139,0,0),center_for_ball,raduis)
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if center_for_ball[0] < (weid-30):
                    center_for_ball[0] = center_for_ball[0] + 30
                    screen.fill((255,255,255))
                
            elif event.key == pygame.K_LEFT:
                if center_for_ball[0] > 30:
                    center_for_ball[0] = center_for_ball[0] - 30
                    screen.fill((255,255,255))

            elif event.key == pygame.K_UP:
                if center_for_ball[1] > 30 :
                    center_for_ball[1] = center_for_ball[1] - 30
                    screen.fill((255,255,255))

            elif event.key == pygame.K_DOWN:
                if center_for_ball[1] < heigh-30 :
                    center_for_ball[1] = center_for_ball[1] + 30
                    screen.fill((255,255,255))

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()