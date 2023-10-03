import pygame, sys, pymunk

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

space = pymunk.Space() # create physical space
space.gravity = (0,500) # x and y gravity

while True: # Game loop
    for event in pygame.event.get(): # checking for user input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()
            
    screen.fill((217,217,217)) # background colour
    space.step(1/50)
    pygame.display.update() # rendering the frame
    clock.tick(120) # limit the frames per second to 120        
    