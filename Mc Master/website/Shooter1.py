import pygame
import random

HEIGHT = 600
WIDTH = 480
FPS = 60




#Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gold = (255,215,0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = HEIGHT - 20
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            
        

pygame.init()#initializes pygame
pygame.mixer.init()# initializes sound

screen = pygame.display.set_mode((WIDTH, HEIGHT))#creates screen 
pygame.display.set_caption("Shooting jiji") # creates name of the game
clock = pygame.time.Clock() # keeps track of game speed 


all_sprites=pygame.sprite.Group()
player = Player()
all_sprites.add(player)



#game loop
running = True
while running:
    clock.tick(FPS)
    #processing imputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #update
    all_sprites.update()
    #Draw (render)
    screen.fill(black)

    screen.fill(black)
    all_sprites.draw(screen)

    pygame.display.flip()
    
    
pygame.quit()
