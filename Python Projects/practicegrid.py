import pygame

#initialize the game engine
pygame.init()

#Define the color choices
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255, 0, 0)

#setting the size of the display window
size = (700, 500)
#creates the window
screen = pygame.display.set_mode(size)

#sets a title for the window
pygame.display.set_caption("Practice Grid")

#looping application until we press the exit button
done = False

#manages the refresh rate of the application
clock = pygame.time.Clock()

#the main loop
while done == False:
    #user does a thing
    for event in pygame.event.get():#pygame.event.get() is a list such as keystrokes
    #states that if the input evaluates to pygame.QUIT, done will equal true and loop will break
    if event.type == pygame.QUIT:
      #loop breaks upon requirements met
        done = True

#screen.fill(thecolor) optional function for filling in the background of a window
screen.fill(White)
#updates the game after every action, not sure how it works, just that it does.
pygame.display.flip()







#sets the maximum fps value to 20fps
clock.tick(20)

#quits the game
pygame.quit()