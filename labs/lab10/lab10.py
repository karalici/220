"""
Name: Iva Karalic
lab10.py
"""


def build_board():
    tictactoe_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return tictactoe_list


def display_board(tictactoe_list):
    counter = 0
    print("----------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(tictactoe_list[counter], end="|")
            counter += 1
        print()
    print("----------")


def place_spot(tictactoe_list, spot, marker):
    tictactoe_list[spot-1] = marker


def legal_spot(tictactoe_list, spot):
    if ((tictactoe_list[spot-1] == "X" or tictactoe_list[spot-1] == "0") or (spot < 1 or spot > 9)):
        return False
    else:
        return True


def game_won(tictactoe_list):
    wincon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7]]
    for condition in wincon:
        counter = 0
        for spot in condition:
            if tictactoe_list[spot-1] == "X":
                counter += 1
            if counter == 3:
                return "X Wins"
    for condition in wincon:
        counter = 0
        for spot in condition:
            if tictactoe_list[spot-1] == "O":
                counter += 1
            if counter == 3:
                return "O Wins"


def game_over(tictactoe_list, turn_count):
    if ((game_won(tictactoe_list) == "X wins" or game_won(tictactoe_list) == "O Wins")
            or (turn_count > 9)):
        return True
    else:
        return False


def play_game():
    tictactoe_list = build_board()
    turn_count = 1
    while not game_over(tictactoe_list, turn_count):
        display_board(tictactoe_list)
        if turn_count % 2 == 0:
            print("It is X turn")
            spot = eval(input("Enter the spot where you want to place X "))
            if legal_spot(tictactoe_list, spot):
                place_spot(tictactoe_list, spot, "X")
            if game_over(tictactoe_list, turn_count):
                if game_won(tictactoe_list):
                    display_board(tictactoe_list)
                    print("X Wins")

        if turn_count % 2 == 1:
            print("It is O turn")
            spot = eval(input("Enter the spot where you want to play O "))
            if legal_spot(tictactoe_list, spot):
                place_spot(tictactoe_list, spot, "O")
            if game_over(tictactoe_list, turn_count):
                if game_won(tictactoe_list):
                    display_board(tictactoe_list)
                    print("O Wins")

        turn_count += 1


def main():
    # add other function calls here
    play_game()
    pass


main()
