#
# Author: Michele Van Dyne
#
# Description: Game loop for the Ultima 0.1 project.
#

import sys
from World import World
import StdDraw
import pygame

# Program must be run with a configuration file specified
if len(sys.argv) < 1:
    print("Must specify a level file!")
else:
    # Create a game world and draw it
    world = World(sys.argv[1])
    world.draw()
    # While the game is still on:
    while world.avatarAlive() and world.getNumMonsters() > 0:
        # Check to see if the player has entered a key
        #  and if so, let the world handle it
        if StdDraw.hasNextKeyTyped():
            ch = StdDraw.nextKeyTyped()
            world.handleKey(ch)
        # Redraw the world - keeping in mind there are threads
        world.lock.acquire()
        world.draw()
        world.lock.release()
        # Display avatar health in the windoe title bar
        caption = "Health: " + str(world.avatar.getHitPoints())
        pygame.display.set_caption(caption)
        StdDraw.show(100)

    # Game is over - display win or loss
    if (world.getNumMonsters() == 0):
        print("You win!!!")
    else:
        print("You lose...")
