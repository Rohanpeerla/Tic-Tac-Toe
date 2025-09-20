import random

def display_board(board):
    print()
    for i, row in enumerate(board):
        display_row = []
        for j, cell in enumerate(row):
            display_row.append(cell if cell != ' ' else str(i*3 + j + 1))
        print(" | ".join(display_row))
        if i < 2:
            print("--+---+--")
    print()

def get_user_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            row = (int(move) - 1) // 3
            col = (int(move) - 1) % 3
            if board[row][col] == ' ':
                return row, col
        print("Invalid input. Try again.")

def check_winner(board):
    lines = []
    lines.extend(board)  
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  
    lines.append([board[i][i] for i in range(3)])  
    lines.append([board[i][2 - i] for i in range(3)])  
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != ' ':
            return line[0]
    return None

def is_tie(board):
    return all(cell != ' ' for row in board for cell in row)

def get_computer_move(board):
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'O'
                if check_winner(board) == 'O':
                    return r, c
                board[r][c] = ' '
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                if check_winner(board) == 'X':
                    board[r][c] = ' '
                    return r, c
                board[r][c] = ' '
    
    if board[1][1] == ' ':
        return 1, 1
    
    corners = [(0,0),(0,2),(2,0),(2,2)]
    empty_corners = [pos for pos in corners if board[pos[0]][pos[1]] == ' ']
    if empty_corners:
        return random.choice(empty_corners)
    
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    current_player = 'X'  

    while True:
        display_board(board)
        if current_player == 'X':
            row, col = get_user_move(board)
        else:
            print("Computer's turn:")
            row, col = get_computer_move(board)
        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            display_board(board)
            if winner == 'X':
                print("🎉 You win!")
            else:
                print("💻 Computer wins!")
            break
        if is_tie(board):
            display_board(board)
            print("🤝 It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()