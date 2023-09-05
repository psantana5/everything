import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Number Guessing Game")

# Set up colors
PURPLE = (128, 0, 128)
LIGHT_PURPLE = (200, 100, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up game variables
number_to_guess = random.randint(1, 100)
attempts = 0
message = ""
start_time = 0
timer = 0

# Create an input box class
class InputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = ""

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)
        pygame.draw.rect(screen, self.color, (self.rect.x + 5, self.rect.y + 5, self.rect.width - 10, self.rect.height - 10))
        font_surface = pygame.font.SysFont(None, 32).render(self.text, True, BLACK)
        screen.blit(font_surface, (self.rect.x + 10, self.rect.y + 10))

    def clear(self):
        self.text = ""

# Create an instance of the input box
input_box = InputBox(screen_width // 2 - 100, screen_height // 2 - 20, 200, 40)

# Create a start menu class
class StartMenu:
    def __init__(self):
        self.options = ["Quit", ]
        self.selected_option = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    self.start_game()
                elif self.selected_option == 1:
                    pygame.quit()
                    quit()

    def start_game(self):
        global show_menu, start_time
        show_menu = False
        start_time = pygame.time.get_ticks()

    def draw(self, screen):
        title_font = pygame.font.SysFont(None, 48)
        menu_font = pygame.font.SysFont(None, 32)
        title_text = title_font.render("Number Guessing Game", True, WHITE)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 2 - 150))

        for i, option in enumerate(self.options):
            if i == self.selected_option:
                option_text = menu_font.render(option, True, LIGHT_PURPLE)
            else:
                option_text = menu_font.render(option, True, WHITE)
            screen.blit(option_text, (screen_width // 2 - option_text.get_width() // 2, screen_height // 2 + i * 50))

# Create an instance of the start menu
start_menu = StartMenu()

# Main game loop
running = True
show_menu = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if show_menu:
            start_menu.handle_event(event)
        else:
            input_box.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    attempts += 1
                    guess = int(input_box.text)
                    input_box.clear()

                    if guess < number_to_guess:
                        message = "Higher!"
                    elif guess > number_to_guess:
                        message = "Lower!"
                    else:
                        end_time = pygame.time.get_ticks()
                        elapsed_time = end_time - start_time
                        message = "Congratulations! You guessed the number in {} attempts. Time: {:.2f} seconds".format(attempts, elapsed_time / 1000)
                        number_to_guess = random.randint(1, 100)
                        attempts = 0
                        start_time = 0

    # Clear the screen
    screen.fill(PURPLE)

    if show_menu:
        # Draw the start menu
        start_menu.draw(screen)
    else:
        # Draw the input box
        input_box.draw(screen)

        # Display the message
        text = pygame.font.SysFont(None, 32).render(message, True, BLACK)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, 250))

        # Display the attempts
        attempts_text = pygame.font.SysFont(None, 32).render("Attempts: {}".format(attempts), True, BLACK)
        attempts_text_x = screen_width // 2 - attempts_text.get_width() // 2
        attempts_text_y = screen_height // 2 + 100  # Adjust the vertical position
        screen.blit(attempts_text, (attempts_text_x, attempts_text_y))

        # Display the timer
        if start_time != 0:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - start_time
            timer_text = pygame.font.SysFont(None, 32).render("Time: {:.2f} seconds".format(elapsed_time / 1000), True, BLACK)
            screen.blit(timer_text, (screen_width - timer_text.get_width() - 20, 20))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
