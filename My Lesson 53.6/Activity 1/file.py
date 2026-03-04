import tkinter as tk
import random

def play(choice):
    moves = ["Rock", "Paper", "Scissor"]
    computer = random.choice(moves)

    if choice == computer:
        result = "Tie!"
    elif (choice == "Rock" and computer == "Scissor") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissor" and computer == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"You: {choice} | Computer: {computer}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissor")

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissor", width=10, command=lambda: play("Scissor")).pack(pady=5)

root.mainloop()
