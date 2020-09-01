import pygame
# x = column 
# y = row
class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False #start with all cells dead
        self.surface = surface
        self.grid_x = grid_x #grid position
        self.grid_y = grid_y
        self.image = pygame.Surface((20,20)) #Cell size
        self.rect = self.image.get_rect()
        
        
    def update(self):
        self.rect.topleft = (self.grid_x*20, self.grid_y*20)
    
    def draw(self):
        if self.alive:
            self.image.fill((0,0,0)) #if cell is alive, set background image to black
        else:
            self.image.fill((33, 47, 61)) #outline
            pygame.draw.rect(self.image, (255,255,255), (2,2,18,18))  #if cell is dead, set to white (dark outline and a smaller white rect on top for effect)
        self.surface.blit(self.image, (self.grid_x*20, self.grid_y*20))