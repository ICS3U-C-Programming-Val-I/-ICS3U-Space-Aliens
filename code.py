#!/usr/bin/env python3

# Created By: Val I
# Date: Jan *8, 2024
# Game file for cops simulator

import ugame
import stage
import constants
import time
import random

def splash_scene():
    # This function is the splash scene.

     # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    background = stage.Grid(image_bank_mt_background, 10, 8)

    # used this program to split the image into tile: 

    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white
    
    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    # repeat forever, game loop
    while true:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # This function is the menu scene.

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text objects
    text = []
    text1 = stage.Text (width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("VAL I Game Studios")
    text.append(text1)

    text2 = stage.Text (width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)



    background = stage.Grid(image_bank_mt_background, 10, 8)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            gamescene()

        # redraw Sprites
        game.tick()


def gamescene():
    # This function is the main game scene.

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    #buttons that you want to keep state information on 
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    alien = stage.Sprite(image_bank_sprites, 9,
                      int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                      16)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # B button
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x < constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        # update game logic
        # Play sound if A button is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()

if __name__ == "__main__":
    menu_scene()