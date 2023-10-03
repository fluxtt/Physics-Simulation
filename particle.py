import pygame, sys, pymunk

width = 800
height = 800

''' This will get moved to a class '''
def createCircle(space, x, y, radius, mass, inertia):
    body = pymunk.Body(mass, inertia, body_type=pymunk.Body.DYNAMIC) # mass, inertia
    body.position = (x, y) # x, y
    shape = pymunk.Circle(body, radius) # radius
    space.add(body, shape)
    return shape

def drawCircles(circles, radius):
    for circle in circles:
        pygame.draw.circle(screen, (0,0,0), circle.body.position, radius)
        
def createWalls(space):
    walls = [
                pymunk.Segment(space.static_body, (0, 0), (width, 0), 0.0),      # TOP WALL
                pymunk.Segment(space.static_body, (width, 0), (width, height), 0.0),    # RIGHT WALL
                pymunk.Segment(space.static_body, (0, height), (width, height), 0.0),  # BOTTOM WALL
                pymunk.Segment(space.static_body, (0, 0), (0, height), 0.0),  # LEFT WALL
                ] 
    for wall in walls:
        wall.collision_type = 1
        space.add(wall)
    

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

space = pymunk.Space() # create physical space
space.gravity = (0,500) # x and y gravity
createWalls(space)
circles = []
circles.append(createCircle(space, 0, 0, 10, 1, 100))

while True: # Game loop
    for event in pygame.event.get(): # checking for user input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()
            
    screen.fill((217,217,217)) # background colour
    drawCircles(circles, 80)
    space.step(1/50)
    pygame.display.update() # rendering the frame
    clock.tick(120) # limit the frames per second to 120    
    