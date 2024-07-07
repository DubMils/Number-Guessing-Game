import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        self.secret_number = random.randint(1, 100)
        self.guess_count = 0

        self.label = tk.Label(root, text="Guess the number (between 1 and 100):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count += 1

            if guess < self.secret_number:
                messagebox.showinfo("Hint", "Too low! Guess higher.")
            elif guess > self.secret_number:
                messagebox.showinfo("Hint", "Too high! Guess lower.")
            else:
                messagebox.showinfo("Congratulations!", f"Correct! It took you {self.guess_count} guesses.")
                self.reset_game()
                return

            self.entry.delete(0, tk.END)
            self.entry.focus_set()

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.guess_count = 0
        self.submit_button["state"] = tk.NORMAL
        self.reset_button["state"] = tk.DISABLED
        self.entry.delete(0, tk.END)
        self.label.config(text="Guess the number (between 1 and 100):")

def main():
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
