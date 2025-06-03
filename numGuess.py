#Ask user to guess a number between 1 and 100
# If number is too high, tell them it is too high after each guess
# similarly for too low
import random
def numGuessGame():
    num = random.randint(1,101)

    print("Welcome to the number guessing game!")
    print("I have selected an integer between 1 and 100.")
    print("Try to guess it!")

    timesGuessed = 0

    guess = 0 

    while guess != num:
        guess = int(input("What is your guess: "))
        timesGuessed +=1
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high")


    if guess == num:
        print("Congratulations! You guessed the number in " + str(timesGuessed) + " tries!")
        print("The number was " + str(num) + ".")
        play_again = input("Would you like to play again? (yes/no)")
        if play_again.lower() == 'yes':
            print()
            print()
            numGuessGame()
        if play_again.lower() == 'no':
            print("Thanks for playing!")
        else: print ("Invalid input. Please enter 'yes' or 'no'.")
        return
        
numGuessGame()
        

