import pygame

class block():
    def __init__(self, screen, x, y):
        self.active = True
        self.gravity = 4
    
    def drawself():
        pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect( (self.x,self.y)))
        
    def update():
        player_rect2.bottom += gravity
        #collide = pygame.Rect.collidelistall(player_rect)
       