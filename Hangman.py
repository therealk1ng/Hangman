import random
Game = "HANGMAN By ASAD."
Game_Bold = '\033[1;4m' + Game + '\033[0m' 
print(f"Welcome To {Game_Bold}")
print("---------------------------")
print("\n")

def Hangman(Wrong):
    if Wrong == 0:
        print(" +-----+")
        print("       |")
        print("       |")
        print("       |")
        print("      ===")
    elif Wrong == 1:
        print(" +-----+")
        print(" O     |")
        print("       |")
        print("       |")
        print("      ===")
    elif Wrong == 2:
        print(" +-----+")
        print(" O     |")
        print(" |     |")
        print("       |")
        print("      ===")
    elif Wrong == 3:
        print(" +-----+")
        print(" O     |")
        print(" |\    |")
        print("       |")
        print("      ===")
    elif Wrong == 4:
        print(" +-----+")
        print(" O     |")
        print("/|\    |")
        print("       |")
        print("      ===")
    elif Wrong == 5:
        print(" +-----+")
        print(" O     |")
        print("/|\    |")
        print("  \    |")
        print("      ===")
    elif Wrong == 6:
        print(" +-----+")
        print(" O     |")
        print("/|\    |")
        print("/ \    |")
        print("      ===")

Exit = "False"
while Exit == "False":
    Wrong = 0
    Guessed_Letters = []
    from words import words
    Random_Word = random.choice(words).upper()
    Letters2 = list(Random_Word)
    Letters = set(Letters2)
    Word = ['_'] * len(Letters2)
    print(f"The Word is {len(Random_Word)} characters Long.")
    while Wrong < 6:
        Word_Blank = ' '.join(Word)
        Hangman(Wrong)
        print(Word_Blank)
        Valid2 = "No"
        Valid3 = "No"
        alphabets = ['A','B','C','D','E','F','G','H','I','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            
        while Valid3 == "No":
            try:
                Player_Guess = str(input("Enter an alphabet : ")).upper()
            except Exception:
                print("Enter Alphabets ONLY.")
            if Player_Guess in alphabets:
                Valid3 = "Yes"
            elif Player_Guess not in alphabets:
                Valid3 = "No"
        while Valid2 == "No":
            if len(Player_Guess) == 1:
                if Player_Guess in Guessed_Letters:
                    print("You already Guessed it Once, try Again.")
                    Player_Guess = input("Enter another Alphabet : ")
                    Valid2 = "No"
                elif Player_Guess not in Guessed_Letters and Player_Guess in Letters:
                    print(f"Correct, {Player_Guess} is in the word  ")
                    Guessed_Letters.append(Player_Guess)
                    Letters.remove(Player_Guess)
                    Valid2 = "Yes"
                    for i in range(len(Random_Word)):
                        if Letters2[i] == Player_Guess:
                            Word[i] = Player_Guess
                elif Player_Guess not in Guessed_Letters and Player_Guess not in Letters:
                    print(f"Wrong, {Player_Guess} is not in the word.")
                    Guessed_Letters.append(Player_Guess)
                    Valid2 = "Yes"
                    Wrong += 1
            elif len(Player_Guess) > 1 or len(Player_Guess) == 0:
                Valid2 = "No"
                Player_Guess = input("Enter a Single Alphabet Only : ") 
        if len(Letters) == 0:
            break


    Hangman(Wrong)
    print(Word_Blank)
    print("\n")
    print("\n")
    if Wrong < 6:
        print("You Won.")
    elif Wrong >= 6:
        print("You Lost")
        print(f"the word was {Random_Word}.")
    print("\n")
    Valid4 = "No"
    print("Do You want to Play More?")
    try:
        Exit2 = input("'y' for Yes, 'n' for No : ").lower()
    except Exception:
        print("Enter y/n ONLY.")
    while Valid4 == "No":
        if Exit2 == "y":
            Exit = "False"
            Valid4 = "Yes"
        elif Exit2 == "n":
            Exit = "True"
            Valid4 = "Yes"
        else:
            Valid4 = "No"
            
print("\n")
print("Goodbye, tysm for Playing..")