
import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
    K_p,
    K_w,
    K_DOWN,
)

class main():    

    def __init__(self):

        self.running = True

        import os
        # load an image of background (located in the "images" folder)
        self.background = pygame.image.load(os.path.join('images', 'background.jpg'))
        # resizing the background image to fit the screen perfectly
        self.background = pygame.transform.scale(self.background, self.getScreenSize())

        
        # Set up the drawing window
        self.screen = pygame.display.set_mode(self.getScreenSize())
        
        # Set up the clock to count the FPS
        self.clock = pygame.time.Clock()


    def getScreenSize(self):
        # get screen size
        import ctypes
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


    def update(self):
        events = pygame.event.get()

        # Look at every event in the queue
        for event in events:
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    self.running = False

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                self.running = False
        
        # if the game is not running anymore, exit
        if not self.running:
            pygame.quit()
            import sys
            sys.exit(0)


    def display(self):
        
        self.screen.blit(self.background, (0, 0))


# here's how to create a pygame sprite
class alien(pygame.sprite.Sprite):
    def __init__(self, x, y, dir):
        super(alien, self).__init__()
        print("I'm a new alien!!!")
        pass

pygame.init()
main = main()

while True:
    main.update()
    main.display()
    
    # make game slow until it reaches 30 fps
    main.clock.tick(30)
    # set the name of the pygame window to the number of fps
    pygame.display.set_caption(str(main.clock.get_fps()))

    # Flip the display SUPER IMPORTANT, renders the screen
    pygame.display.flip()


# If you were to exit the while true without the exit() function or without completely exiting the program
pygame.quit()






