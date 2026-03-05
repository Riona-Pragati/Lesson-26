import tkinter as tk
import random

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    message_label.config(text="I’m thinking of a number between 1 and 100.")
    guess_entry.delete(0, tk.END)

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
    except ValueError:
        message_label.config(text="Please enter a valid number.")
        return
    attempts += 1
    if guess < secret_number:
        message_label.config(text="Too low! Try again.")
    elif guess > secret_number:
        message_label.config(text="Too high! Try again.")
    else:
        message_label.config(text=f"Correct! You guessed it in {attempts} tries.")

def reset_game():
    start_game()

root = tk.Tk()
root.title("Guess the Number Game")

message_label = tk.Label(root, text="Click 'Start' to begin!", font=("Arial", 14))
message_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 14))
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=5)

root.mainloop()
