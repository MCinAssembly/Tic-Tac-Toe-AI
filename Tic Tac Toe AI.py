import random

end_game = " "

board_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
board_preview = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def print_board():
    global board_array
    for a in range(0,3):
        for b in range(0,11):
            if (b + 1) % 4 == 0 and b != 0:
                print("|", end = "")

            elif b == 1:                   
                    print(board_array[a][0], end = "")

            elif b == 5:
                    print(board_array[a][1], end = "")

            elif b == 9:
                    print(board_array[a][2], end = "")
                    
            else:
                print(" ", end = "")

        print()

        if a < 2:
            for c in range(0,11):
                print("-", end = "")

            print()
    print()


def print_preview():
    for a in range(0,3):
        for b in range(0,11):
            if (b + 1) % 4 == 0 and b != 0:
                print("|", end = "")

            elif b == 1:                   
                    print(board_preview[a][0], end = "")

            elif b == 5:
                    print(board_preview[a][1], end = "")

            elif b == 9:
                    print(board_preview[a][2], end = "")
                    
            else:
                print(" ", end = "")

        print()

        if a < 2:
            for c in range(0,11):
                print("-", end = "")

            print()

    print()



def user_move():
    global end_game
    global board_array
    if (end_game != "Computer Win") and (end_game != "Player Win"):
        print_preview()
        while True:
            user_input = input("Please select: ").strip()


            if user_input == "1":

                if board_array[0][0] == " ":
                    board_array[0][0] = "X"
                    break;

                else:
                    print("That location is occupied")

            elif user_input == "2":

                if board_array[0][1] == " ":
                    board_array[0][1] = "X"
                    break;

                else:
                    print("That location is occupied")

            elif user_input == "3":

                if board_array[0][2] == " ":
                    board_array[0][2] = "X"
                    break;

                else:
                    print("That location is occupied")

            elif user_input == "4":

                if board_array[1][0] == " ":
                    board_array[1][0] = "X"
                    break;

                else:
                    print("That location is occupied")

            elif user_input == "5":

                if board_array[1][1] == " ":
                    board_array[1][1] = "X"
                    break;

                else:
                    print("That location is occupied")

            elif user_input == "6":

                if board_array[1][2] == " ":
                    board_array[1][2] = "X"
                    break;
                
                else:
                    print("That location is occupied")

            elif user_input == "7":

                if board_array[2][0] == " ":
                    board_array[2][0] = "X"
                    break;

                else:
                    print("That location is occupied")

            elif user_input == "8":

                if board_array[2][1] == " ":
                    board_array[2][1] = "X"
                    break;

                else:
                    print("That location is occupied")

            elif user_input == "9":

                if board_array[2][2] == " ":
                    board_array[2][2] = "X"
                    break;

                else:
                    print("That location is occupied")

            else:
                print("Please enter either 1,2,3,4,5,6,7,8,9")

    else:
        return
    print_board()
    end_game = check_win()
    if (end_game == "Computer Win"):
        print("You lose")
        main()
    elif (end_game == "Player Win"):
        print("You win!")
        main()
    elif (end_game == "Draw!"):
        print("Draw!")
                # or board array full:
        main()
    computer_move()


def check_win():
    global board_array
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if board_array[i][j] != " ":
                count += 1

    if (board_array[0][0] == "X") and (board_array[0][1] == "X") and (board_array[0][2] == "X"):
        return "Player Win"

    elif (board_array[1][0] == "X") and (board_array[1][1] == "X") and (board_array[1][2] == "X"):
        return "Player Win"

    elif (board_array[2][0] == "X") and (board_array[2][1] == "X") and (board_array[2][2] == "X"):
        return "Player Win"

    elif (board_array[0][0] == "X") and (board_array[1][0] == "X") and (board_array[2][0] == "X"):
        return "Player Win"

    elif (board_array[0][1] == "X") and (board_array[1][1] == "X") and (board_array[2][1] == "X"):
        return "Player Win"

    elif (board_array[0][2] == "X") and (board_array[1][2] == "X") and (board_array[2][2] == "X"):
        return "Player Win"

    elif (board_array[0][0] == "X") and (board_array[1][1] == "X") and (board_array[2][2] == "X"):
        return "Player Win"

    elif (board_array[0][2] == "X") and (board_array[1][1] == "X") and (board_array[2][0] == "X"):
        return "Player Win"

###################################################################################################################################### Player Check

    if (board_array[0][0] == "O") and (board_array[0][1] == "O") and (board_array[0][2] == "O"):
        return "Computer Win"

    elif (board_array[1][0] == "O") and (board_array[1][1] == "O") and (board_array[1][2] == "O"):
        return "Computer Win"

    elif (board_array[2][0] == "O") and (board_array[2][1] == "O") and (board_array[2][2] == "O"):
        return "Computer Win"

    elif (board_array[0][0] == "O") and (board_array[1][0] == "O") and (board_array[2][0] == "O"):
        return "Computer Win"

    elif (board_array[0][1] == "O") and (board_array[1][1] == "O") and (board_array[2][1] == "O"):
        return "Computer Win"

    elif (board_array[0][2] == "O") and (board_array[1][2] == "O") and (board_array[2][2] == "O"):
        return "Computer Win"

    elif (board_array[0][0] == "O") and (board_array[1][1] == "O") and (board_array[2][2] == "O"):
        return "Computer Win"

    elif (board_array[0][2] == "O") and (board_array[1][1] == "O") and (board_array[2][0] == "O"):
        return "Computer Win"

    elif count == 9:
        return "Draw!"


###################################################################################################################################### Computer Check

    return "Null"

        
def computer_move():
    global board_array
    global end_game
    if (end_game != "Computer Win") and (end_game != "Player Win"):
        while True:
            #######################################################################################
            if board_array[0][0] == "O" and board_array[2][2] == "O" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "O" and board_array[2][2] == "O" and board_array[0][0] == " ":
                row = 0
                column = 0
            elif board_array[0][0] == "O" and board_array[1][1] == "O" and board_array[2][2] == " ":
                row = 2
                column = 2
                ###################################################################################
            elif board_array[0][2] == "O" and board_array[2][0] == "O" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "O" and board_array[2][0] == "O" and board_array[0][2] == " ":
                row = 0
                column = 2
            elif board_array[0][2] == "O" and board_array[1][1] == "O" and board_array[2][0] == " ":
                row = 2
                column = 0
                ####################################################################################
            elif board_array[0][0] == "O" and board_array[2][0] == "O" and board_array[1][0] == " ":
                row = 1
                column = 0
            elif board_array[0][0] == "O" and board_array[1][0] == "O" and board_array[2][0] == " ":
                row = 2
                column = 0
            elif board_array[1][0] == "O" and board_array[2][0] == "O" and board_array[0][0] == " ":
                row = 0
                column = 0
                ####################################################################################
            elif board_array[0][0] == "O" and board_array[0][2] == "O" and board_array[0][1] == " ":
                row = 0
                column = 1
            elif board_array[0][0] == "O" and board_array[0][1] == "O" and board_array[0][2] == " ":
                row = 0
                column = 2
            elif board_array[0][1] == "O" and board_array[0][2] == "O" and board_array[0][0] == " ":
                row = 0
                column = 0
                ####################################################################################
            elif board_array[0][2] == "O" and board_array[2][2] == "O" and board_array[1][2] == " ":
                row = 1
                column = 2
            elif board_array[0][2] == "O" and board_array[1][2] == "O" and board_array[2][2] == " ":
                row = 2
                column = 2
            elif board_array[1][2] == "O" and board_array[2][2] == "O" and board_array[0][2] == " ":
                row = 0
                column = 2
                ####################################################################################
            elif board_array[2][0] == "O" and board_array[2][2] == "O" and board_array[2][1] == " ":
                row = 2
                column = 1
            elif board_array[2][1] == "O" and board_array[2][2] == "O" and board_array[2][0] == " ":
                row = 2
                column = 0
            elif board_array[2][0] == "O" and board_array[2][1] == "O" and board_array[2][2] == " ":
                row = 2
                column = 2
                ####################################################################################
            elif board_array[0][1] == "O" and board_array[2][1] == "O" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "O" and board_array[2][1] == "O" and board_array[0][1] == " ":
                row = 0
                column = 1
            elif board_array[0][1] == "O" and board_array[1][1] == "O" and board_array[2][1] == " ":
                row = 2
                column = 1
                ###################################################################################

            elif board_array[1][0] == "O" and board_array[1][2] == "O" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "O" and board_array[1][2] == "O" and board_array[1][0] == " ":
                row = 1
                column = 0
            elif board_array[1][0] == "O" and board_array[1][1] == "O" and board_array[1][2] == " ":
                row = 1
                column = 2
            #######################################################################################
            #######################################################################################   
            elif board_array[0][0] == "X" and board_array[2][2] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "X" and board_array[2][2] == "X" and board_array[0][0] == " ":
                row = 0
                column = 0
            elif board_array[0][0] == "X" and board_array[1][1] == "X" and board_array[2][2] == " ":
                row = 2
                column = 2
                ###################################################################################
            elif board_array[0][2] == "X" and board_array[2][0] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "X" and board_array[2][0] == "X" and board_array[0][2] == " ":
                row = 0
                column = 2
            elif board_array[0][2] == "X" and board_array[1][1] == "X" and board_array[2][0] == " ":
                row = 2
                column = 0
                ####################################################################################
            elif board_array[0][0] == "X" and board_array[2][0] == "X" and board_array[1][0] == " ":
                row = 1
                column = 0
            elif board_array[0][0] == "X" and board_array[1][0] == "X" and board_array[2][0] == " ":
                row = 2
                column = 0
            elif board_array[1][0] == "X" and board_array[2][0] == "X" and board_array[0][0] == " ":
                row = 0
                column = 0
                ####################################################################################
            elif board_array[0][0] == "X" and board_array[0][2] == "X" and board_array[0][1] == " ":
                row = 0
                column = 1
            elif board_array[0][0] == "X" and board_array[0][1] == "X" and board_array[0][2] == " ":
                row = 0
                column = 2
            elif board_array[0][1] == "X" and board_array[0][2] == "X" and board_array[0][0] == " ":
                row = 0
                column = 0
                ####################################################################################
            elif board_array[0][2] == "X" and board_array[2][2] == "X" and board_array[1][2] == " ":
                row = 1
                column = 2
            elif board_array[0][2] == "X" and board_array[1][2] == "X" and board_array[2][2] == " ":
                row = 2
                column = 2
            elif board_array[1][2] == "X" and board_array[2][2] == "X" and board_array[0][2] == " ":
                row = 0
                column = 2
                ####################################################################################
            elif board_array[2][0] == "X" and board_array[2][2] == "X" and board_array[2][1] == " ":
                row = 2
                column = 1
            elif board_array[2][1] == "X" and board_array[2][2] == "X" and board_array[2][0] == " ":
                row = 2
                column = 0
            elif board_array[2][0] == "X" and board_array[2][1] == "X" and board_array[2][2] == " ":
                row = 2
                column = 2
                ####################################################################################
            elif board_array[0][1] == "X" and board_array[2][1] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "X" and board_array[2][1] == "X" and board_array[0][1] == " ":
                row = 0
                column = 1
            elif board_array[0][1] == "X" and board_array[1][1] == "X" and board_array[2][1] == " ":
                row = 2
                column = 1
            #########################################################################################
            elif board_array[1][0] == "X" and board_array[1][2] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[1][1] == "X" and board_array[1][2] == "X" and board_array[1][0] == " ":
                row = 1
                column = 0
            elif board_array[1][0] == "X" and board_array[1][1] == "X" and board_array[1][2] == " ":
                row = 1
                column = 2
            ############################################################################################

            elif board_array[0][0] == "O" and board_array[1][1] == "X" and board_array[2][2] == " ":
                row = 2
                column = 2
            elif board_array[2][2] == "O" and board_array[1][1] == "X" and board_array[0][0] == " ":
                row = 0
                column = 0
            elif board_array[0][2] == "O" and board_array[1][1] == "X" and board_array[2][0] == " ":
                row = 2
                column = 0
            elif board_array[2][0] == "O" and board_array[1][1] == "X" and board_array[0][2] == " ":
                row = 0
                column = 2



            ############################################################################################
            elif board_array[0][0] == "O" and board_array[2][2] == "O" and board_array[1][1] == "X":
                if board_array[0][1] == " " and board_array[1][2] == " " and board_array[0][2] == " ":
                    row = 0
                    column = 2
                elif board_array[1][0] == " " and board_array[2][1] == " " and board_array[2][0] == " ":
                    row = 2
                    column = 0
            elif board_array[0][2] == "O" and board_array[2][0] == "O" and board_array[1][1] == "X":
                if board_array[0][1] == " " and board_array[1][0] == " " and board_array[0][0] == " ":
                    row = 0
                    column = 0
                elif board_array[1][2] == " " and board_array[2][1] == " " and board_array[2][2] == " ":
                    row = 2
                    column = 2
                
            
            ##############################################################################################
            elif board_array[0][0] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[0][2] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[2][0] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1
            elif board_array[2][2] == "X" and board_array[1][1] == " ":
                row = 1
                column = 1

            ##############################################################################################

            elif board_array[0][0] == "X":
                if board_array[0][1] == " ":
                    row = 0
                    column = 1
                elif board_array[1][0] == " ":
                    row = 1
                    column = 0
            elif board_array[0][2] == "X":
                if board_array[0][1] == " ":
                    row = 0
                    column = 1
                elif board_array[1][2] == " ":
                    row = 1
                    column = 2
            elif board_array[2][0] == "X":
                if board_array[1][0] == " ":
                    row = 1
                    column = 0
                elif board_array[2][1] == " ":
                    row = 2
                    column = 1

            elif board_array[2][2] == "X":
                if board_array[2][1] == " ":
                    row = 2
                    column = 1
                elif board_array[1][2] == " ":
                    row = 1
                    column = 2


            ###############################################################################################

            

            ############################################################################################


            elif board_array[0][0] == " ":
                row = 0
                column = 0
            elif board_array[0][2] == " ":
                row = 0
                column = 2
            elif board_array[2][0] == " ":
                row = 2
                column = 0
            elif board_array[2][2] == " ":
                row = 2
                column = 2
            ##############################################################################################
            
            
                
            else:
                row = random.randint(0, 2)
                column = random.randint(0, 2)
            if board_array[row][column] == " ":
                board_array[row][column] = "O"
                end_game = check_win()
                print_board()
                if (end_game == "Computer Win"):
                    print("You lose")
                    main()
                elif (end_game == "Player Win"):
                    print("You win!")
                    main()
                elif (end_game == "Draw!"):
                    print("Draw!")
                # or board array full:
                    main()
                user_move()

    else:
        return
        


def play_game():
    choose_first = [1, 2]
    chosen = random.choice(choose_first)
    if chosen == 1:       
        computer_move()
    else:
        user_move()

    #print(end_game)

    
def main():
    if end_game == " ":
        print("Hello Welcome To TTT")
        play_game()
    exit()


main()
