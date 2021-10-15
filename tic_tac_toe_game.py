"""
TICTACTOE GAME
"""

def display_board(game_board):
    """
    display_board
    """
    print(game_board[7],"|",game_board[8],"|",game_board[9])
    print("----------")
    print(game_board[4],"|",game_board[5],"|",game_board[6])
    print("----------")
    print(game_board[1],"|",game_board[2],"|",game_board[3])


def marker_choice():
    """
    function in which the players choose character
    mark position in the board
    """
    player1_marker=""
    player2_marker=""
    while player1_marker not in ["X","O"]:
        player1_marker=input("Player 1, choose character you want to be (X or O) : ")
        if player1_marker=="X":
            player2_marker="O"
        elif player1_marker=="O":
            player2_marker="X"
        else:
            print("Sorry you choose wrong character. Try again")
    return (player1_marker,player2_marker)

def place_player_marker_choice(game_board,marker,position_list):
    """
    function in which the players select position in the board
    """
    player_place_marker=""
    while player_place_marker not in position_list:
        player_place_marker=int(input("Choose position where you want to put character : "))
        if player_place_marker in position_list: #check if this position is empty
            position_list.remove(player_place_marker)
            game_board[player_place_marker]=marker
            break
        else:
            print("Sorry wrong the number or position is not empty")
    return (game_board,position_list)

def win_check(game_board,marker1,marker2,position_list):
    """
    check if any of player win the game
    """
    if  (game_board[1]==marker1 and game_board[2]==marker1 and game_board[3]==marker1) or \
        (game_board[4]==marker1 and game_board[5]==marker1 and game_board[6]==marker1) or \
        (game_board[7]==marker1 and game_board[8]==marker1 and game_board[9]==marker1) or \
        (game_board[1]==marker1 and game_board[4]==marker1 and game_board[7]==marker1) or \
        (game_board[2]==marker1 and game_board[5]==marker1 and game_board[8]==marker1) or \
        (game_board[3]==marker1 and game_board[6]==marker1 and game_board[9]==marker1) or \
        (game_board[1]==marker1 and game_board[5]==marker1 and game_board[9]==marker1) or \
        (game_board[3]==marker1 and game_board[5]==marker1 and game_board[7]==marker1):
        print("Congratulations. Win the player1")
        return 1
    elif(game_board[1]==marker2 and game_board[2]==marker2 and game_board[3]==marker2) or \
        (game_board[4]==marker2 and game_board[5]==marker2 and game_board[6]==marker2) or \
        (game_board[7]==marker2 and game_board[8]==marker2 and game_board[9]==marker2) or \
        (game_board[1]==marker2 and game_board[4]==marker2 and game_board[7]==marker2) or \
        (game_board[2]==marker2 and game_board[5]==marker2 and game_board[8]==marker2) or \
        (game_board[3]==marker2 and game_board[6]==marker2 and game_board[9]==marker2) or \
        (game_board[1]==marker2 and game_board[5]==marker2 and game_board[9]==marker2) or \
        (game_board[3]==marker2 and game_board[5]==marker2 and game_board[7]==marker2):
        print("Congratulations. Win the player2")
        return 2
    elif len(position_list)==0:
        print("Nobody win")
        return 3

def try_again():
    """
    #check do the players want to play again
    """
    play_or_not_play = ""
    while play_or_not_play not in["Y","N"]:
        play_or_not_play=input("Do you want try again ? (Y or N) : ")
        if play_or_not_play=="Y":
            return True
        elif play_or_not_play=="N":
            return False
        else:
            print("Sorry wrong the character")

def main():
    """pyt
    main function
    """
    game_board=["x","1","2","3","4","5","6","7","8","9"] #game board is filled numbers of position
    position_list=list(range(1,10))#list of board position
    game_on=True
    markers=marker_choice()#players will select character
    while game_on:
        display_board(game_board)#display board positions
        print("Player 1")
        game_board_and_position_list = \
        place_player_marker_choice(game_board,markers[0],position_list)#player one selects position
        game_board=game_board_and_position_list[0]#the board is filled of player'choice
        position_list=game_board_and_position_list[1]#list of free positions on the board
        display_board(game_board)#display updated position board
        end_game=win_check(game_board,markers[0],markers[1],position_list)#check if any of player win the game
        if end_game in [1,2,3]:#if there is an end game,players can play again
            play_again=try_again()
            if play_again:
                position_list=list(range(1,10))
                game_board=["x","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
        print("Player 2")
        game_board_and_position_list = \
        place_player_marker_choice(game_board,markers[1],position_list)#player two choose position
        game_board=game_board_and_position_list[0] #the board is filled of player' choice
        position_list=game_board_and_position_list[1] #list free positions on board
        end_game=win_check(game_board,markers[0],markers[1],position_list) #check if any of player win the game
        if end_game: #if there is an end game, players can play again
            play_again=try_again()
            if play_again:
                game_board=["x","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
    return end_game #added line to make unittest
main()
