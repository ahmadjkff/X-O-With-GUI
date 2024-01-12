import tkinter as tk
import random

global player_score
global PC_score
player_score = PC_score = 0

def Player_move(row, col):
    if not buttons[row][col]["text"]:
        buttons[row][col]["text"] = 'X'
        
        if not check_winner('X') and not check_tie():
            PC_move()

def check_winner(cur_player):
    global player_score, PC_score, result_label
    for i in range(3):
        if (buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '' or
            buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != ''):
            result_label.config(text=f"Player {cur_player} wins!", bg="green")
            if cur_player == 'X':
                player_score += 1
            else:
                PC_score += 1
            player_score_label.config(text=f"You: {player_score}") 
            PC_score_label.config(text=f"PC: {PC_score}")  
            return True

    if (buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '' or
            buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != ''):
        result_label.config(text=f"Player {cur_player} wins!", bg="green")
        if cur_player == 'X':
            player_score += 1
        else:
            PC_score += 1
        player_score_label.config(text=f"You: {player_score}", font=20)  
        PC_score_label.config(text=f"PC: {PC_score}")  
        return True
    return False
    
def Restart():
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text']=''
    result_label.config(text="", bg="#F0F0F0")

def PC_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if not buttons[i][j]["text"]]
    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col]['text'] = 'O'
        if not check_winner('O'):
            check_tie()

def check_tie():
    for i in range(3):
        for j in range(3):
            if not buttons[i][j]["text"]:
                return False
            
    result_label.config(text="Tie, NO Winner!")
    result_label.config(bg="Red")
    return True

window = tk.Tk()
window.title("X O Game")

font = ("Helvetica", 24)

player_score_label = tk.Label(text=f"You: {player_score}", font=(12))
PC_score_label = tk.Label(text=f"PC: {PC_score}", font=(20))
result_label = tk.Label(font=(20))

player_score_label.grid(row=0, column=0)
PC_score_label.grid(row=0, column=2)
result_label.grid(row=1, column=1)

restart_button = tk.Button(text="Restart", relief="raised", command=Restart)
restart_button.grid(row=2, column=1)

buttons = [['', '', ''],
           ['', '', ''],
           ['', '', '']
          ]

for i in range(3):
    for j in range(3):
        button = tk.Button(window, font=font, width=5, height=2, command=lambda row=i, col=j: Player_move(row, col))
        button.grid(row=i + 3, column=j)
        buttons[i][j] = button

window.mainloop()
