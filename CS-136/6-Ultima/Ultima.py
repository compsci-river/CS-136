#
# Author: Michele Van Dyne
#
# Description: Game loop for the Ultima 0.0 project.
#

import sys
from World import World
import StdDraw

# Program must be run with a configuration file specified
if len(sys.argv) < 1:
    print("Must specify a level file!")
else:
    # Create a game world and draw it
    world = World(sys.argv[1])
    world.draw()
    # Forever:
    while True:
        # Check to see if the player has entered a key
        #  and if so, let the world handle it
        if StdDraw.hasNextKeyTyped():
            ch = StdDraw.nextKeyTyped()
            world.handleKey(ch)
            world.draw()
        else:
            StdDraw.show(100)
