#!/usr/bin/env python3

# Created By: Val I
# Date: Jan *8, 2024
# Game file for cops simulator

import ugame
import stage

def gamescene():
    # This function is the main game scene.

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    background = stage.Grid(image_bank_background, 10, 8)

    character = stage.Sprite(image_bank_sprites, 5, 75, 66)
    game = stage.Stage(ugame.display, 60)
    game.layers = [character] + [background]
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            character.move(character.x + 1, character.y)
        if keys & ugame.K_LEFT:
            character.move(character.x 1, character.y)
        if keys & ugame.K_UP:
            character.move(character.x, character.y - 1)
        if keys & ugame.K_DOWN:
            character.move(character.x, character.y + 1)
        # update game logic
        
        # redraw Sprites
        game.render_sprites([character])
        game.tick()

if __name__ == "__main__":
    gamescene()