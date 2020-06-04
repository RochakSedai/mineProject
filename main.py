import random

def design(guesses,word):
    if (guesses == 0):
        print("________\n"
              "|    |\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|_______")
    elif (guesses == 1):
        print("________\n"
              "|    |\n"
              "|    O\n"
              "|\n"
              "|\n"
              "|\n"
              "|_______")
    elif (guesses == 2):
        print("________\n"
              "|    |\n"
              "|    O\n"
              "|    |\n"
              "|    |\n"
              "|\n"
              "|_______")
    elif (guesses == 3):
        print("________\n"
              "|    |\n"
              "|    O\n"
              "|   \|\n"
              "|    |\n"
              "|\n"
              "|_______")
    elif (guesses == 4):
        print("________\n"
              "|    |\n"
              "|    O\n"
              "|   \|/\n"
              "|    |\n"
              "|\n"
              "|_______")
    elif (guesses == 5):
        print("________\n"
              "|    |\n"
              "|    O\n"
              "|   \|/\n"
              "|    |\n"
              "|   /\n"
              "|_______")     
    elif (guesses == 6):
        print("________\n"
              "|    |\n"
              "|    O\n"
              "|   \|/\n"
              "|    |\n"
              "|   / \\n"
              "|_______")  
        print("\n")
        print("The word is %s.\n" % word)
        print("YOU LOST TRY AGAIN!")
        print("\nDo you like to play again,type y foy yes and n for no::")
        again = input("-> ")
        again = again.lower()
        if again == 'y':
            hangman()
        return 
                          


    

    
def randomword():
    file = open("letter.txt")
    words = file.readlines()
    myword = random.choice(words)
    myword = str(myword).strip("")
    myword = str(myword).strip("''")
    myword = str(myword).strip("\n")
    myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword
    
def hangman():
    guesses = 0
    word = randomword()
    wordlist = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []
    print("Lets play hangman...!\n")
    design(guesses,word)
    print("\n" +'  '.join(blanks_list)) #row of dashes

    print("Guess a letter!!")
    while guesses < 6:
        guess = input("-> ")
        guess = guess.lower()

    # if the player enters more than one letter at a time
        if len(guess)>1:
            print("Please enter one letter at a time....!")

    # if the player hits enter without entering any letter
        elif guess == "":
            print("Enter a letter::")

    # if the player hits the letter that he has already guessed,then display the list of guessed letters
        elif guess in guess_list:
            print("Already guessed..list of letter you have guessed are:::")
            print(' '.join(guess_list))

    # if all the above conditions fail,use an else block to append the
    # guessed letter to the list of guessed letters
        else:
            guess_list.append(guess)
            i = 0
            while i<len(word):
                if guess == word[i]: #if guessed letter is in the given word
                    new_blanks_list[i] = wordlist[i]
                i = i + 1

        # if the guess letter is wrong ask the user to guess again
            if new_blanks_list == blanks_list:
                print("Your letter is wrong...")
                guesses = guesses + 1
                design(guesses,word)

                if guesses < 6:
                    print("Guess again!")
                    print(''.join(blanks_list))

        # if the guessed letter is correct , insert that letter in a correct position
            elif wordlist != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

            # finally if the whole word is guessed correctly , the player wins
                if wordlist == blanks_list:
                    print("\n YOU WIN 'HURRAY' \n")
                    print("Do you want to play again? press y for yes and n for no::")
                    again = input("-> ")
                    again = again.lower()
                    if again == "y":
                        hangman()
                    quit()

            #or if only the guessed letter is correct , ask the user to guess the next letter
                else:
                    print("Great guess!!Guess the next letter..")
hangman()
                    