#!/usr/bin/env python3

# Created By: Val I
# Date: Jan *8, 2024
# Game file for cops simulator

import ugame
import stage

def gamescene():
    # This function is the main game scene.

    image_bank_background =stage.Bank.from_bmp16("space_aliens_background")
    background = stage.Grid(space_aliens_background, 10, 8)

    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    while True:
        # repeat forever, or you turn it off!
        pass # Placeholder

if __name__ == "__main__":
    gamescene()