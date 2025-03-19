import pygame  
import os
import time  

def play_music(index):
    pygame.mixer.music.load(list_of_mus[index])
    pygame.mixer.music.play() 
def name_mus(index):
    font = pygame.font.Font(None,22)
    text = font.render(for_txt[index],True,(0,0,0))
    return text
def name_mus_long(index):
    font = pygame.font.Font(None,18) 
    text = font.render(for_txt[index],True,(0,0,0))
    return text


pygame.init()
pygame.mixer.init()




mus_fl_path = "music"
for_txt = os.listdir(mus_fl_path)
list_of_mus = os.listdir(mus_fl_path)
for i in range(len(list_of_mus)):
    list_of_mus[i] = mus_fl_path+"/"+list_of_mus[i]


mus = pygame.mixer.music.load(list_of_mus[0]) 
play_music(0)
index = 0




WIDTH, HEIGHT = 600,800  
im = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("pl")
background = pygame.image.load("background1.jpeg")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))


fon = pygame.Surface((300, 200))  
fon.fill((255, 255, 255)) 

next = pygame.image.load("next.png")
next = pygame.transform.scale(next,(100,100))
back = pygame.image.load("back.png")
back = pygame.transform.scale(back,(100,100))
plae = pygame.image.load("play.png")
plae = pygame.transform.scale(plae,(100,100))
pause = pygame.image.load("pause.png")
pause = pygame.transform.scale(pause,(115,113))



running = True    
while running:
    im.blit(background, (0,0))
    im.blit(fon, (155, 500))
    im.blit(next,(350,580))
    im.blit(back,(165,580))
    im.blit(name_mus(index),(200,530))


    if pygame.mixer.music.get_busy():
        im.blit(pause,(249,575))
        
    else:
        im.blit(plae,(256,580))
        


    for event in pygame.event.get():  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                        im.blit(pause,(249,575))
                        
                else:
                    pygame.mixer.music.unpause()
                    
                    im.blit(plae,(256,580))
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(list_of_mus)
                play_music(index)

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(list_of_mus)
                play_music(index)
            
            
    

        if event.type == pygame.QUIT:  
            running = False  

    pygame.display.update()





pygame.quit()