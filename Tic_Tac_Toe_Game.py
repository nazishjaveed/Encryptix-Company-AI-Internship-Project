
# Tic Tac Toe Game with Minimax Algorithm 🎮
import tkinter as tk
from tkinter import messagebox
# Tic Tac Toe Class Initialization 🔄
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.master, text="", font=('Helvetica', 24), width=4, height=2,
                            command=lambda idx=i: self.on_button_click(idx))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)
# Handling Button Clicks 🖱️
    def on_button_click(self, idx):
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.comp_move()
# Checking for a Win 🏆
    def check_win(self):
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != "":
                return True
        return False
# Resetting the Game ♻️
    def reset(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"
# Computer's Move Using Minimax Algorithm 💡
    def comp_move(self):
        best_score = float("-inf")
        best_move = None
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = "O"
        self.buttons[best_move].config(text="O")
        if self.check_win():
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            self.reset()
        elif "" not in self.board:
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            self.reset()
        else:
            self.current_player = "X"
# Minimax Algorithm Implementation 🤖
    def minimax(self, board, is_maximizing):
        if self.check_win():
            return 1 if is_maximizing else -1
        elif "" not in self.board:
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "O"
                    score = self.minimax(self.board, False)
                    self.board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "X"
                    score = self.minimax(self.board, True)
                    self.board[i] = ""
                    best_score = min(score, best_score)
            return best_score

# Main Function 🚀
def main():
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()

