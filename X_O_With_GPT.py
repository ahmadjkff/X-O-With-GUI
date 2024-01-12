import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic-Tac-Toe")

        # Initialize scores as instance attributes
        self.player_score = self.PC_score = 0

        # Initialize the player
        self.current_player = "X"

        # Create buttons for the grid
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

        # Create buttons in a 3x3 grid
        for i in range(3):
            for j in range(3):
                button = tk.Button(window, font=("Helvetica", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.Player_move(row, col))
                button.grid(row=i+2, column=j)  # Move buttons to a new row
                self.buttons[i][j] = button

        # Set the computer player
        self.computer_player = "O"

        # Create the player score label
        self.player_score_label = tk.Label(window, text=f"You: {self.player_score}")
        self.player_score_label.grid(row=0, column=0, padx=5)

        # Create the PC score label
        self.PC_score_label = tk.Label(window, text=f"PC: {self.PC_score}")
        self.PC_score_label.grid(row=0, column=2)

        # Create the restart button
        self.restart_button = tk.Button(window, text="Restart", command=self.reset_game)
        self.restart_button.grid(row=1, column=1, pady=(10, 0))  # Placed in the top row with some vertical padding

        # Store the original button color
        self.original_button_color = self.buttons[0][0].cget("bg")

    def Player_move(self, row, col):
        # Check if the clicked button is empty
        if not self.buttons[row][col]["text"]:
            # Set the text of the button to the current player (X)
            self.buttons[row][col]["text"] = self.current_player

            # Check for a winner or tie after the player's move
            winning_cells = self.check_winner()
            if winning_cells:
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.player_score += 1
                self.player_score_label.config(text=f"You: {self.player_score}")
                self.update_grid_colors("green", winning_cells)  # Change color for winner cells
            elif self.check_tie():
                messagebox.showinfo("Tie!", "It's a tie!")
                self.update_grid_colors("gray")  # Change color for the entire grid in case of a tie
            else:
                # Switch to the computer player
                self.current_player = self.computer_player

                # Computer makes a move after a delay
                self.window.after(500, self.computer_move)

    def update_grid_colors(self, color, winning_cells=None):
        # Update the background color of buttons to the specified color
        if color == "gray":
            for i in range (3):
                for j in range(3):
                    self.buttons[i][j].config(bg=color)
                    self.window.update()
        
        else:
            for i in range(3):
                for j in range(3):
                    if winning_cells and (i, j) in winning_cells:
                        self.buttons[i][j].config(bg=color)
                    else: 
                        self.buttons[i][j].config(bg=self.original_button_color)
                    self.window.update()  # Update the window to reflect color changes

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return [(i, 0), (i, 1), (i, 2)]
            elif self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return [(0, i), (1, i), (2, i)]

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return [(0, 0), (1, 1), (2, 2)]
        elif self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return[(0, 2), (1, 1), (2, 0)]
       
        return None

    def check_tie(self):
        # Check if all buttons are filled (no winner, hence a tie)
        for row in self.buttons:
            for button in row:
                if not button["text"]:
                    return False
        return True

    def reset_game(self):
        # Reset the game by clearing the button texts and resetting the original button colors
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j].config(bg=self.original_button_color)
        self.current_player = "X"

    def computer_move(self):
        # Simple random move by the computer
        empty_cells = [(i, j) for i in range(3) for j in range(3) if not self.buttons[i][j]["text"]]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.buttons[row][col]["text"] = self.computer_player

            # Check for a winner after the computer's move
            winning_cells = self.check_winner()
            if winning_cells:
                messagebox.showinfo("Winner!", f"Player {self.computer_player} wins!")
                self.PC_score += 1
                self.PC_score_label.config(text=f"PC: {self.PC_score}")
                self.update_grid_colors("yellow", winning_cells)  # Change color for winner cells
                self.window.after(2000, self.reset_game)  # Reset the game after 2 seconds
            else:
                # Switch back to the player
                self.current_player = "X"


if __name__ == "__main__":
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()
