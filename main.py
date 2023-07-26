import random
import tkinter as tk

global color_main
global color_text
global color_secondary

class WhatToPlay(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Variables
        global color_main
        global color_text
        global color_secondary

        color_main = "light gray"
        color_text = "black"
        color_secondary = "light gray"

        # Create GUI
        self.title("What To Play")
        #self.geometry("300x300")
        self.configure(bg=color_main)

        # Call Functions
        self.create_widgets()

    # Define Functions

    # Create Widgets
    def create_widgets(self):
        self.main_label = tk.Label(self, text="Click the 'Random Game' button to get a random game.\n\n "
                                   "Click the 'Edit Games' button view and edit list of games. \n\n\n\n\n",
                              bg=color_main, fg=color_text)
        self.main_label.pack()

        self.game_label = tk.Label(self, text="Add games through the \n"
                                              "'Edit Games button.\n", bg=color_main, fg=color_text, font=("", 28))
        self.game_label.pack()

        self.random_game_button = tk.Button(self, text="Random Game", bg=color_secondary, fg=color_text,
                                            command=self.random_game_button_pressed)
        self.random_game_button.pack()

        # Label to put space between buttons
        self.space_label = tk.Label(self, text="---------", bg=color_main, fg=color_main)
        self.space_label.pack()

        self.edit_games_button = tk.Button(self, text="Edit Games", bg=color_secondary, fg=color_text,
                                           command=self.edit_games_popup)
        self.edit_games_button.pack()

    # Button commands
    def random_game_button_pressed(self):
        with open('games.txt') as f:
            lines = f.readlines()
            random_line = random.choice(lines) if lines else None
            self.game_label.configure(text=f"{random_line} \n")

    def edit_games_popup(self):
        edit_games_popup = tk.Toplevel()
        edit_games_popup.title("Edit Games List")
        edit_games_popup.geometry("650x400")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.games_entry = tk.Text(edit_games_popup)
        self.games_entry.grid(row=0, column=0, sticky="nsew")

        games_list = self.load_games()
        self.games_entry.insert(tk.END, games_list)

        games_list_save_button = tk.Button(edit_games_popup, text="Save", bg="dark blue", fg="white",
                                           command=lambda: self.save_games(self.games_entry))
        games_list_save_button.grid(row=0, column=0, sticky="ne")

    def load_games(self):
        try:
            with open("games.txt", "r") as file:
                games_list = file.read()
            return games_list
        except FileNotFoundError:
            return ""

    def save_games(self, entry):
        games_list = entry.get("1.0", tk.END)
        with open("games.txt", "w") as file:
            file.write(games_list)


if __name__ == "__main__":
    app = WhatToPlay()
    app.mainloop()
