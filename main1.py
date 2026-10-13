print('''We will make the board using the dictionary
in which the keys will be the positions on the Tic Tac Toe board and the values in them will be either "x" or "o" depending on what character the player has chosen to play with.''')

Gameboard = {'7': '', '8': '', '9': '',
             '4': '', '5': '', '6': '',
             '1': '', '2': '', '3': ''}

board_keys = []
for key in Gameboard:
    board_keys.append(key)
Player_name = input("Enter your username:")
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

    #now we'll write down the main function which has all the gameplay functionality
    def game():

        turn = 'x'
        count = 0

        for i in range(10):
            printBoard(Gameboard)
            print("It's your turn," + Player_name + turn + ".Move to which place?")

            move = input()

            if Gameboard[move] == '':
                Gameboard[move] = turn
                count += 1
            else:
                print("That place is already filled by the other player. \n Move to which place? (Not occupied)")
                continue
            #Now we will check if player x or 0 has won, for every move after 5 moves.
            if count >= 5:
                if Gameboard['7'] == Gameboard['8'] == Gameboard['9'] != '': #across the top
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + " won. ****")
                    break
                elif Gameboard['4'] == Gameboard['5'] == Gameboard['6'] != '': #across the middle
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + "won. ****")
                    break
                elif Gameboard['1'] == Gameboard['2'] == Gameboard['3'] != '': #across the bottom
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + "won. ****")
                    break
                elif Gameboard['1'] == Gameboard['4'] == Gameboard['7'] != '': #In the first column on the left most side
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + "won. ****")
                    break
                elif Gameboard['2'] == Gameboard['5'] == Gameboard['8'] != '': #In the middle column
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + "won. ****")
                    break
                elif Gameboard['3'] == Gameboard['6'] == Gameboard['9'] != '': #In the last column on the right most side
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + "won. ****")
                    break
                elif Gameboard['7'] == Gameboard['5'] == Gameboard['3'] != '': #Diagonal
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + "won. ****")
                    break
                elif Gameboard['1'] == Gameboard['5'] == Gameboard['9'] != '': #Diagonal
                    printBoard(Gameboard)
                    print("\nGame Over! \n")
                    print(" **** " + turn + "won. ****")
                    break
                #if neither x nor 0 wins and the board is full, we'll declare the results as a draw, where no one wins at all.
                if count == 10:
                    print("\nGame Over! \n")
                    print("It's a draw because no one made a winning row or column or diagonal. \n Thanks for playing!")

            #Now we have to add an option for the player to decide if they want to continue playing or not after a round finishes.
            print("Do you want to play again? (y/n)")
            answer = input()
            if answer == "y" or answer == "Y":
                print("Okay! Restarting the game and creating a new board to play on...")
            else:
                print("Okay! Thanks for playing. Hope you had fun!")
                break

            game()

    if __name__ == "__main__":
        game()



        