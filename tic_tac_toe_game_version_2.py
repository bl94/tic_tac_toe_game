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
    mark position on the board
    """
    player1_marker=""
    player2_marker=""
    while player1_marker !="X" and player1_marker !="Y" :
        player1_marker=input("Player 1, choose character you want to be(X or Y) : ")
        if player1_marker=="X":
            player2_marker="Y"
        elif player1_marker=="Y":
            player2_marker="X"
        else:
            print("Sorry you choose wrong character. Try again")
    return (player1_marker,player2_marker)

def place_player_marker_choice(game_board,marker,position_list):
    """
    function in which the players select position on board
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

def place_player_marker_choice_v2(game_board,marker):
    """
    Version 2 - function in which the players choose position on board - second solution
    """
    player_place_marker=0
    while player_place_marker not in range(1,10) \
        and not free_space_check(game_board,player_place_marker):
        player_place_marker=int(input("Choose place where you want to put : "))
        if player_place_marker in range(1,10)and not free_space_check(game_board,player_place_marker): #check if this position is empty
            game_board[player_place_marker]=marker
            break
        else:
            print("Sorry wrong the number or this position is not empty")
    return game_board

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
        return True
    elif(game_board[1]==marker2 and game_board[2]==marker2 and game_board[3]==marker2) or \
        (game_board[4]==marker2 and game_board[5]==marker2 and game_board[6]==marker2) or \
        (game_board[7]==marker2 and game_board[8]==marker2 and game_board[9]==marker2) or \
        (game_board[1]==marker2 and game_board[4]==marker2 and game_board[7]==marker2) or \
        (game_board[2]==marker2 and game_board[5]==marker2 and game_board[8]==marker2) or \
        (game_board[3]==marker2 and game_board[6]==marker2 and game_board[9]==marker2) or \
        (game_board[1]==marker2 and game_board[5]==marker2 and game_board[9]==marker2) or \
        (game_board[3]==marker2 and game_board[5]==marker2 and game_board[7]==marker2):
        print("Congratulations. Win the player2")
        return True
    elif len(position_list)==0:
        print("Nobody win")
        return True

def free_space_check(game_board,position):
    """
    Version 2 - function to check free place
    """
    for num in range(1,10):
        if game_board[position]==str(num): #change 1
            return True  #this place is empty
    return False #this place is not empty

def full_board_check(game_board):
    """
    Version 2 - function to check all places in the board are taken
    """
    for number in range(1,10):
        if free_space_check(game_board,number):
            return False #the board is not filled
    return True #the board if full

def win_check_v2(game_board,marker1,marker2):
    """
    #Version 2 - check if any of player win the game
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
        return True
    elif(game_board[1]==marker2 and game_board[2]==marker2 and game_board[3]==marker2) or \
        (game_board[4]==marker2 and game_board[5]==marker2 and game_board[6]==marker2) or \
        (game_board[7]==marker2 and game_board[8]==marker2 and game_board[9]==marker2) or \
        (game_board[1]==marker2 and game_board[4]==marker2 and game_board[7]==marker2) or \
        (game_board[2]==marker2 and game_board[5]==marker2 and game_board[8]==marker2) or \
        (game_board[3]==marker2 and game_board[6]==marker2 and game_board[9]==marker2) or \
        (game_board[1]==marker2 and game_board[5]==marker2 and game_board[9]==marker2) or \
        (game_board[3]==marker2 and game_board[5]==marker2 and game_board[7]==marker2):
        print("Congratulations. Win the player2")
        return True
    elif full_board_check(game_board):
        print("Nobody win")
        return True

def try_again():
    """
    #check if the players want to play again
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

# main function
def main():
    """
    main function
    """
    game_board=["x","1","2","3","4","5","6","7","8","9"] #game board is filled positon numbers
    position_list=list(range(1,10))#position list on board
    game_on=False
    markers=marker_choice()#players will select character
    while game_on:
        display_board(game_board)#display position board
        print("Player 1")
        game_board_and_position_list = \
        place_player_marker_choice(game_board,markers[0],position_list)#player one selects position
        game_board=game_board_and_position_list[0]#the board is filled of player'choice
        position_list=game_board_and_position_list[1]#list free positions on the board
        display_board(game_board)#display updated position board
        end_game=win_check(game_board,markers[0],markers[1],position_list)#check if any of player win the game
        if end_game:#if there is an end game,players can play again
            play_again=try_again()
            if play_again:
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
        if end_game: # if there is an end game, players can play again
            play_again=try_again()
            if play_again:
                game_board=["x","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
main()

#Version 2
def playV2():
    game_board=["0","1","2","3","4","5","6","7","8","9"]
    game_on=False
    markers=marker_choice()
    while game_on==False:
        display_board(game_board)
        print("Player 1")
        game_board=place_player_marker_choice_v2(game_board,markers[0])
        display_board(game_board)
        end_game=win_check_v2(game_board,markers[0],markers[1])
        if end_game==True:
            play_again=try_again()
            if play_again:
                game_board=["0","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
        print("Player 2")
        game_board=place_player_marker_choice_v2(game_board,markers[1])
        end_game=win_check_v2(game_board,markers[0],markers[1])
        if end_game==True:
            play_again=try_again()
            if play_again:
                game_board=["x","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
