#display_board
def display_board(game_board):
    print(game_board[7],"|",game_board[8],"|",game_board[9])
    print("----------")
    print(game_board[4],"|",game_board[5],"|",game_board[6])
    print("----------")
    print(game_board[1],"|",game_board[2],"|",game_board[3])

#function in which the players choose character 
#to mark position on the board
def marker_choice():
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


#function in which the players choose position on board
def place_player_marker_choice(game_board,marker,position_list):
    player_place_marker=""
    while player_place_marker not in position_list:
            player_place_marker=int(input("Choose position where you want to put character : "))
            #check if this position is empty
            if player_place_marker in position_list:
                position_list.remove(player_place_marker)
                game_board[player_place_marker]=marker
                break
            else:
                print("Sorry wrong the number or this position is not empty")
    return (game_board,position_list)

#Version 2 - function in which the players choose position on board - second solution
def place_player_marker_choiceV2(game_board,marker):
    player_place_marker=0
    while player_place_marker not in range(1,10) and not free_space_check(game_board,player_place_marker):
            player_place_marker=int(input("Choose place where you want to put : "))
            #check if this position is empty
            if player_place_marker in range(1,10) and not free_space_check(game_board,player_place_marker):
                game_board[player_place_marker]=marker
                break
            else:
                print("Sorry wrong the number or this position is not empty")
    return game_board

# check if any of player win the game
def win_check(game_board,marker1,marker2,position_list):
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

# Version 2 - function to check free place
def free_space_check(game_board,position):
    for x in range(1,10):
        if game_board[position]=="{x}":
            #this place is empty
            return True
    #this place is not empty
    return False

# Version 2 - function to check all places in the board are taken
def full_board_check(game_board):
    for x in range(1,10):
        if free_space_check(game_board,x):
            #the board is not filled
            return False
    #the board if full
    return True

#Version 2 - check if any of player win the game
def win_checkV2(game_board,marker1,marker2):
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
        elif full_board_check:
            print("Nobody win")
            return True     
  
#check if the players want to play again
def try_again():
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
def play():
    #game board is filled positon numbers
    game_board=["x","1","2","3","4","5","6","7","8","9"]
    #position list on board
    position_list=list(range(1,10))
    game_on=False
    #players will select character
    markers=marker_choice()
    while game_on==False:
        #display position board
        display_board(game_board)
        print("Player 1")
        #player one choose position
        game_board_and_position_list =place_player_marker_choice(game_board,markers[0],position_list)
        #the board is filled of player' choice
        game_board=game_board_and_position_list[0]
        #list free positions on board
        position_list=game_board_and_position_list[1]
        #display updated position board
        display_board(game_board)
        #check if any of player win the game
        end_game=win_check(game_board,markers[0],markers[1],position_list)
        # if there is an end game, players can play again
        if end_game==True:
            play_again=try_again()
            if play_again:
                game_board=["x","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
        print("Player 2")
        #player two choose position
        game_board_and_position_list =place_player_marker_choice(game_board,markers[1],position_list)
        #the board is filled of player' choice
        game_board=game_board_and_position_list[0]
        #list free positions on board
        position_list=game_board_and_position_list[1]
        #check if any of player win the game
        end_game=win_check(game_board,markers[0],markers[1],position_list)
        # if there is an end game, players can play again
        if end_game==True:
            play_again=try_again()
            if play_again:
                game_board=["x","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
            
play()

#Version 2
def playV2():
    game_board=["0","1","2","3","4","5","6","7","8","9"]
    position_list=list(range(1,10))
    game_on=False
    markers=marker_choice()
    while game_on==False:
        display_board(game_board)
        print("Player 1")
        game_board=place_player_marker_choiceV2(game_board,markers[0])
        display_board(game_board)
        end_game=win_checkV2(game_board,markers[0],markers[1])
        if end_game==True:
            play_again=try_again()
            if play_again:
                game_board=["0","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break
        print("Player 2")
        game_board=place_player_marker_choiceV2(game_board,markers[1])
        end_game=win_checkV2(game_board,markers[0],markers[1])
        if end_game==True:
            play_again=try_again()
            if play_again:
                game_board=["x","1","2","3","4","5","6","7","8","9"]
                continue
            else:
                break

