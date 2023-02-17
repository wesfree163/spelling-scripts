# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
pygame.init()

# Set up the drawing window
x_axis = 800
y_axis = 600

x = 0
y = 0
z = 255

##posx = random.randint(1, 10)
##posy = random.randint(1, 10)

posx = x_axis/2
posy = y_axis/2

screen = pygame.display.set_mode([x_axis, y_axis])

# Run until the user asks to quit
running = True
youre_sure = False

while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = 255
            y = 0
            z = 0
            if youre_sure:
                running = False
            youre_sure = True


    # Fill the background with some color other than white now
    screen.fill((150, 255, 150))


    # Draw a solid blue circle in the center
##  Circle is drawn with parameters (what display for it?, what color?, what position on window?, what size by radius?)    
    pygame.draw.circle(screen, (x, y, z), (posx, posy), 75)


    # Flip the display
    pygame.display.flip() # without this, nothing appears on the window

# Done! Time to quit.
pygame.quit()

