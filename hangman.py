import tkinter as tk
from tkinter import messagebox
from string import ascii_uppercase
import random


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Hangman by Krzysztof Zielinski')

        self.word_list = ['MUMBAI', 'DELHI', 'BANGLORE', 'HYDRABAD', 'AHMEDABAD', 'CHENNAI', 'KOLKATA', 'SURAT', 'PUNE',
                          'JAIPUR', 'AMRITSAR', 'ALLAHABAD', 'RANCHI',
                          'LUCKNOW', 'KANPUR', 'NAGPUR', 'INDORE', 'THANE', 'BHOPAL', 'PATNA', 'GHAZIABAD', 'AGRA',
                          'FARIDABAD', 'MEERUT', 'RAJKOT', 'VARANASI', 'SRINAGAR',
                          'RAIPUR', 'KOTA', 'JHANSI']

        self.photos = [tk.PhotoImage(file=f"images/hang{i}.png") for i in range(12)]

        self.imgLabel = tk.Label(root)
        self.imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

        self.lblWord = tk.StringVar()
        tk.Label(root, textvariable=self.lblWord, font=('consolas 24 bold')).grid(row=0, column=3, columnspan=6,
                                                                                  padx=10)

        self.newGameButton = tk.Button(root, text="New\nGame", command=self.newGame, font=("Helvetica 10 bold"))
        self.newGameButton.grid(row=3, column=8)

        self.keyboardButtons = []
        self.createKeyboard()

        self.newGame()

    def createKeyboard(self):
        n = 0
        for c in ascii_uppercase:
            button = tk.Button(self.root, text=c, command=lambda c=c: self.guess(c), font=('Helvetica 18'), width=4)
            button.grid(row=1 + n // 9, column=n % 9)
            self.keyboardButtons.append(button)
            n += 1

    def newGame(self):
        self.numberOfGuesses = 0
        self.the_word = random.choice(self.word_list)
        self.the_word_withSpaces = " ".join(self.the_word)
        self.lblWord.set(' '.join("_" * len(self.the_word)))


    def guess(self, letter):
        if self.numberOfGuesses < 11:
            txt = list(self.the_word_withSpaces)
            guessed = list(self.lblWord.get())
            if self.the_word_withSpaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                self.lblWord.set("".join(guessed))
                if self.lblWord.get() == self.the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You guessed it!")
            else:
                self.numberOfGuesses += 1
                self.imgLabel.config(image=self.photos[self.numberOfGuesses])
                if self.numberOfGuesses == 11:
                    messagebox.showwarning("Hangman", "Game Over")


def main():
    window = tk.Tk()
    hangman_game = HangmanGame(window)
    window.mainloop()


if __name__ == "__main__":
    main()
