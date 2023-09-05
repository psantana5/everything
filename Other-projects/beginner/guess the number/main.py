import pygame
import os
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Guess the Number")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
FONT_LARGE = pygame.font.Font(None, 48)
FONT_MEDIUM = pygame.font.Font(None, 32)
FONT_SMALL = pygame.font.Font(None, 24)

# Game variables
min_value = 1
max_value = 100
target_number = random.randint(min_value, max_value)
attempts = 0
game_over = False

def clear_screen():
    """Clears the Pygame screen."""
    window.fill(WHITE)

def display_text(text, font, color, x, y):
    """Displays text on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    window.blit(text_surface, text_rect)

def display_menu():
    """Displays the game menu."""
    clear_screen()
    title_font = pygame.font.Font(None, 64)
    menu_font = pygame.font.Font(None, 32)
    title_text = title_font.render("Guess the Number", True, BLACK)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH/2, 100))
    window.blit(title_text, title_rect)
    pygame.draw.line(window, BLACK, (WINDOW_WIDTH/2 - 150, 200), (WINDOW_WIDTH/2 + 150, 200), 3)
    play_text = menu_font.render("Play", True, BLACK)
    play_rect = play_text.get_rect(center=(WINDOW_WIDTH/2, 250))
    window.blit(play_text, play_rect)
    set_range_text = menu_font.render("Set Range", True, BLACK)
    set_range_rect = set_range_text.get_rect(center=(WINDOW_WIDTH/2, 300))
    window.blit(set_range_text, set_range_rect)
    high_scores_text = menu_font.render("View High Scores", True, BLACK)
    high_scores_rect = high_scores_text.get_rect(center=(WINDOW_WIDTH/2, 350))
    window.blit(high_scores_text, high_scores_rect)
    reset_scores_text = menu_font.render("Reset High Scores", True, BLACK)
    reset_scores_rect = reset_scores_text.get_rect(center=(WINDOW_WIDTH/2, 400))
    window.blit(reset_scores_text, reset_scores_rect)
    quit_text = menu_font.render("Quit", True, BLACK)
    quit_rect = quit_text.get_rect(center=(WINDOW_WIDTH/2, 450))
    window.blit(quit_text, quit_rect)
    pygame.display.update()

def get_menu_choice():
    """Gets the menu choice from the player."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "1"
                elif event.key == pygame.K_2:
                    return "2"
                elif event.key == pygame.K_3:
                    return "3"
                elif event.key == pygame.K_4:
                    return "4"
                elif event.key == pygame.K_5:
                    return "5"

def generate_number(min_value, max_value):
    """Generates a random number within the given range."""
    return random.randint(min_value, max_value)

def get_guess():
    """Gets the player's guess."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    return int(event.unicode)

def save_score(score):
    """Saves the player's score to a file."""
    with open("scores.txt", "a") as file:
        file.write(str(score) + "\n")

def display_high_scores():
    """Displays the high scores from the file."""
    clear_screen()
    display_text("High Scores", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
    if not os.path.isfile("scores.txt"):
        display_text("No high scores found.", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
    else:
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            if not scores:
                display_text("No high scores found.", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
            else:
                scores = [int(score.strip()) for score in scores]
                scores.sort(reverse=True)
                y = 250
                for i, score in enumerate(scores[:10]):
                    display_text(f"{i+1}. {score}", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, y)
                    y += 30
    pygame.display.update()

def reset_high_scores():
    """Resets the high scores file."""
    clear_screen()
    display_text("Are you sure you want to reset the", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
    display_text("high scores? (Y/N)", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 300)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    with open("scores.txt", "w") as file:
                        file.write("")
                    display_text("High scores reset.", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 400)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    return
                elif event.key == pygame.K_n:
                    return

def set_range():
    """Allows the player to set a custom number range."""
    clear_screen()
    display_text("Set Range", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
    display_text("Enter the minimum value:", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
    pygame.display.update()

    min_value_input = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    min_value_input += event.unicode
                elif event.key == pygame.K_RETURN:
                    min_value = int(min_value_input)
                    break

        clear_screen()
        display_text("Set Range", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
        display_text("Enter the minimum value:", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
        display_text(min_value_input, FONT_MEDIUM, RED, WINDOW_WIDTH // 2, 300)
        pygame.display.update()

        if len(min_value_input) > 0 and event.key == pygame.K_RETURN:
            break

    clear_screen()
    display_text("Set Range", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
    display_text("Enter the maximum value:", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
    pygame.display.update()

    max_value_input = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    max_value_input += event.unicode
                elif event.key == pygame.K_RETURN:
                    max_value = int(max_value_input)
                    return min_value, max_value

        clear_screen()
        display_text("Set Range", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
        display_text("Enter the maximum value:", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
        display_text(max_value_input, FONT_MEDIUM, RED, WINDOW_WIDTH // 2, 300)
        pygame.display.update()

        if len(max_value_input) > 0 and event.key == pygame.K_RETURN:
            break

def play_game(min_value, max_value):
    """Plays the game."""
    global attempts, target_number, game_over

    clear_screen()
    display_text("Guess the Number", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
    pygame.display.update()

    target_number = generate_number(min_value, max_value)
    attempts = 0
    game_over = False

    while not game_over:
        clear_screen()
        display_text("Guess the Number", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
        display_text("Enter your guess:", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
        pygame.display.update()

        guess = get_guess()
        attempts += 1

        if guess < target_number:
            clear_screen()
            display_text("Too low! Try again.", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
            pygame.display.update()
            pygame.time.wait(500)
        elif guess > target_number:
            clear_screen()
            display_text("Too high! Try again.", FONT_LARGE, BLACK, WINDOW_WIDTH // 2, 100)
            pygame.display.update()
            pygame.time.wait(500)
        else:
            clear_screen()
            display_text(f"Congratulations! You guessed the number in {attempts} attempts.", FONT_MEDIUM, BLACK, WINDOW_WIDTH // 2, 250)
            pygame.display.update()
            save_score(attempts)
            pygame.time.wait(2000)
            game_over = True

# Main game loop
def main():
    """Main function."""
    min_value = 1
    max_value = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            play_game(min_value, max_value)
        elif choice == "2":
            min_value, max_value = set_range()
            play_game(min_value, max_value)
        elif choice == "3":
            display_high_scores()
        elif choice == "4":
            reset_high_scores()
        elif choice == "5":
            pygame.quit()
            quit()

if __name__ == "__main__":
    main()
