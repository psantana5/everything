import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.core.window import Window
from kivy.lang import Builder
import random
import pickle
import os

# Initialize Kivy
Builder.load_file('hangman.kv')

# Hangman parameters
hangman_x = 0
hangman_y = 0
hangman_radius = 0
hangman_parts = []

# Game variables
hangman_state = 0
game_over = False
game_result = ""
guessed_letters = []
word = ""
score = 0

# Function to generate a random word


def generate_word():
    return random.choice(words)

# Function to reset the game


def reset_game():
    global word, guessed_letters, hangman_state, game_over, game_result, score
    word = generate_word()
    guessed_letters = []
    hangman_state = 0
    game_over = False
    game_result = ""
    score = 0

# Function to handle button clicks


def handle_button_click(instance):
    global game_over, game_result
    if instance.text == "Play Again":
        reset_game()
    elif instance.text == "Quit":
        game_over = True

# Function to draw the hangman


def draw_hangman(canvas):
    if hangman_state >= 1:
        canvas.add(Color(1, 1, 1))
        canvas.add(Line(circle=(
            hangman_parts[0][0], hangman_parts[0][1], hangman_radius, 0, 360), width=2))
    if hangman_state >= 2:
        canvas.add(Line(points=(
            hangman_parts[1][0], hangman_parts[1][1], hangman_parts[2][0], hangman_parts[2][1]), width=2))
    if hangman_state >= 3:
        canvas.add(Line(points=(
            hangman_parts[1][0], hangman_parts[1][1], hangman_parts[3][0], hangman_parts[3][1]), width=2))
    if hangman_state >= 4:
        canvas.add(Line(points=(
            hangman_parts[1][0], hangman_parts[1][1], hangman_parts[4][0], hangman_parts[4][1]), width=2))
    if hangman_state >= 5:
        canvas.add(Line(points=(
            hangman_parts[1][0], hangman_parts[1][1], hangman_parts[5][0], hangman_parts[5][1]), width=2))

# Function to save the game


def save_game():
    game_data = {
        'word': word,
        'guessed_letters': guessed_letters,
        'hangman_state': hangman_state,
        'score': score
    }
    with open('hangman_savegame.pkl', 'wb') as file:
        pickle.dump(game_data, file)

# Function to load the game


def load_game():
    global word, guessed_letters, hangman_state, score
    try:
        with open('hangman_savegame.pkl', 'rb') as file:
            game_data = pickle.load(file)
        word = game_data['word']
        guessed_letters = game_data['guessed_letters']
        hangman_state = game_data['hangman_state']
        score = game_data['score']
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")
        reset_game()


# Check if it's the first time running the program
first_time_file = "first_time.txt"
first_time = False

if not os.path.isfile(first_time_file):
    first_time = True
    with open(first_time_file, "w") as file:
        file.write("")

# List of words
words = ["cat", "dog", "apple", "banana", "car", "house", "sun", "book", "tree", "flower", "bird", "chair", "table", "pen",
         "pencil", "ball", "clock", "door", "key", "milk", "bread", "shoe", "hat", "bed", "lamp", "fish", "orange", "moon", "star", "shirt"]

# Generate the initial word
word = ""  # Initialize with an empty string
load_game()

# Kivy app class


class HangmanApp(App):
    def build(self):
        layout = FloatLayout()

        # Add the canvas for drawing
        canvas = Widget()
        layout.add_widget(canvas)

        # Add the word label
        word_label = Label(text="", font_size=13,
                           pos_hint={"x": 0.05, "y": 0.6})
        layout.add_widget(word_label)

        # Add the guessed letters label
        guessed_label = Label(text="Guessed letters: ", font_size=13, pos_hint={
                              "x": 0.05, "y": 0.75})
        layout.add_widget(guessed_label)

        # Add the score label
        score_label = Label(text="Score: 0", font_size=13, pos_hint={
                            "x": 0.05, "y": 0.9})
        layout.add_widget(score_label)

        # Add the play again button
        play_again_button = Button(text="Play Again", font_size=13, pos_hint={
                                   "x": 0.4, "y": 0.53}, size_hint=(0.2, 0.07))
        play_again_button.bind(on_release=handle_button_click)
        layout.add_widget(play_again_button)

        # Add the quit button
        quit_button = Button(text="Quit", font_size=13, pos_hint={
                             "x": 0.45, "y": 0.68}, size_hint=(0.1, 0.07))
        quit_button.bind(on_release=handle_button_click)
        layout.add_widget(quit_button)

        # Draw the hangman on the canvas
        with canvas.canvas:
            draw_hangman(canvas.canvas)

        return layout


if __name__ == '__main__':
    HangmanApp().run()
