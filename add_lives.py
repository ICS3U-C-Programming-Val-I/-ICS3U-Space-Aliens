#!/usr/bin/env python3

# Created By: Val I
# Date: Jan *8, 2024
# Game file for cops simulator

import ugame
import stage
import constants
import time
import random
import supervisor

def splash_scene():
    # This function is the splash scene.

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    # An image bank for CircuitPython.
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # Sets background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, 10, 8)

    # Sets background to image 0 in the image bank
   

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
    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # This function is the menu scene.

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text objects
    text = []
    text1 = stage.Text (width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(10, 10)
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
    # declare variables score
    score = 0
    lives = 3
    

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene(score, lives)

        # redraw Sprites
        game.tick()


def game_scene(score, lives):
    # This function is the main game scene.

    # for score
    
    lives_text = stage.Text(width = 29, height = 14)
    lives_text.clear()
    lives_text.cursor(0,0)
    lives_text.move(95,1)
    lives_text.text("Lives: {0}".format(lives))

    score_text = stage.Text(width = 29, height = 14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format(score))

    def show_alien():
        # This function takes an alien from off scene and moves it on screen.
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    #buttons that you want to keep state information on 
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    
    

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y): 
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)


    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    # create list for when we shoot (lasers)
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
    # place 1 alien on screen
    show_alien()

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [score_text] + [lives_text] + lasers + [ship] + aliens + [background]
    game.render_block()

    # repeat forever, game loop
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
            # Fire a laser, if we have not used up all lasers
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        
        # each frame move the lasers, that have been fired.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x,
                                          lasers[laser_number].y -
                                          constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)

        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))

        # each frame check if any lasers are touching any aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2, lasers[laser_number].x + 11, lasers[laser_number].y + 12, aliens [alien_number].x + 1, aliens[alien_number].y, aliens[alien_number].x + 15, aliens [alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y) 
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))
                            
        # each frame check if any aliens are touching the space ship 
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens [alien_number].x + 1, aliens [alien_number].y, aliens [alien_number].x + 8, aliens [alien_number].y + 8, ship.x, ship.y, ship.x + 15, ship.y +15):
                    #alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(1.0)
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    if lives > 0:
                        lives = lives -1
                        lives_text.clear()
                        lives_text.cursor(0,0)
                        lives_text.move(95,1)
                        lives_text.text("Lives: {0}".format(lives))
                        game_scene(score, lives)
                    if lives <= 0:
                        game_over_scene(score)

        # redraw Sprites
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()

def game_over_scene(final_score):
    # this function is the game over scene

    # image banks for circuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to the image 0 in the image bank. 
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # add text objects
    text = []
    text1=stage.Text (width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text (width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None) 
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3=stage.Text (width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(32,110)
    text3.text("PRESS SELECT") 
    text.append(text3)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game=stage.Stage(ugame.display, constants.FPS)
    
    #Set the layer, items show up in order
    game.layers = text + [background]

    #render the background and initial location of sprite list
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Start button selected
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick() # wait until refresh rate finishes


if __name__ == "__main__":
   splash_scene() 