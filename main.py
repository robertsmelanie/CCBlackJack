# First, import the logo from art.py using the from/import syntax
from art import logo

# Next we will import the rest of our modules that will be used in this project
import os
import random

# There is not a command in VS Code to clear the console when we want, so this is a work around
# Using the os module we imported above, we will create the following function
def clear():
    """Clears the console across Operating Systems""" # Note this is the proper use of a Docstring, to inform other programmers of what something does
    command = 'clear'
    # If statement to check to see what OS the computer is running. The "clear" command in Windows is "cls", so if the computer is running Windows it changes the command so it works
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    # inputs the command variable into the system function from the os module, this executes the command in the console/terminal
    os.system(command)

# function to "pull a card" or deal from the deck at random
def deal_card():
    # Create the docstring
    """Returns a random card from the deck"""
    # Create a cards list for each card, Ace through King
    # Note royalty cars are all 10
    # Note enter Ace as 11; rules state it can also be 1 but we will take care of that later
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Use the random module with the choice method passing in the cards list and set it to a variable
    card = random.choice(cards)
    # Use the return keyword to return the card variable
    return card
# print(deal_card())
# Function to score our cards that are pulled from the deck
def calculate_score(cards): # Note this "cards" argument is separate from the cards variable in the above function because of scope
    """Takes a list of cards and returns the score calculated from the cards"""
    #  Create an if statement to check to see if a player has a black jack hand (2 cards, an ace and a 10)
    if sum(cards) == 21 and len(cards) == 2:   #sum() and len() are both built in python functions
        # return 0 to represent a blackjack hand, we will use this instead of 21 to differentiate it from a normal score of 12
        return 0
    # Create an if statement that says if 11 is in the cards list, and the sum is less than 21, change 11 to 1 so as ot not bust
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # Return the sum of the cards after all the above if statements have been checked
    return sum(cards)

# Create a function that compares the scores and returns an outcome
def compare(user_score, computer_score): 
    """# Pass in both the user's score and the computer's as arguments"""
    # User if/elif/else statements for each outcome
    # Draw
    if user_score == computer_score:
        return "Draw"
    # Computer has blackjack
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    # User has Blackjack
    elif user_score == 0:
        return "Win with a Blackjack"
    # User Bust
    elif user_score > 21:
        return "You went over. You lose"
    # Computer Bust
    elif computer_score > 21:
        return "Opponent went over. You win"
    # User wins
    elif user_score > computer_score:
        return "You win"
    # Computer wins
    else:
        return "You Lose"

# Create game function, this function will be run so the game begins
def playgame():
    """This function will be run so the game begins"""
    # Print the logo in the terminal
    print(logo)

    # Create empty lists for user's and computer's cards, this is where the cards are drawn by each 'player' will be stored and how each of the above functions will make their calculations
    user_cards = []
    computer_cards = []

    # Create a variable to note if the game should continue and use a Boolean value of False
    is_game_over = False
    # This will be used in conjunction with a while loop below to keep the game running as long as the value reads false

    # Blackjack starts with 2 cards being dealt so we need to start the game with two cards being added to the user_cards and computer_cards lists
    # Use a for loop using the built in range function to run the loop just twice
    for _ in range(2): # the underscore indicates an un-needed variable and is just a placeholder
        # Use the append method with each empty list and pass in our deal_card function
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # Our loop will run only twice, and each time our deal_card() function will output a random card. The append() method will then add that card to the appropriate lists
    # Each player will now have two starting cards
    # Testing print(user_cards, computer_cards)

    # Create a while loop to "play the game", this is also known as a "Game Loop": https://realpython.com/lessons/setting-game-loop/
    while not is_game_over: 
        # We use the "not" keyword to indicate state this loop will continue to run while is_game_over=False

        #Using the calculate_score() function, create two new variables to store the scores by passing in our lists as arguments
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        


        # Using print statements and f-strings, have the current score of the user and the first card of the computer's hand
        # Note in Blackjack you can always see the first card dealt to your opponent but not the second one 
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        # Create an if/else statement that states if either player has a Blackjack hand, or the user goes over 21 the game ends
        # Remember to indicate Blackjack we had the calculate_score   function return a value of 0
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
            # Ends the game loop
        else: 
            # Create an input stored to a variable that asks the user to "hit" or "pass"
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            # Nest an if/else statement for the outcomes of the input
            if user_should_deal == "y":
                user_cards.append(deal_card()) # Deals another card and stores it in our list
            else: 
                is_game_over = True # user ended the game

    # Create a while loop outside of our main game loop that keeps the computer playing as well as long as its score is not equal to 0 and is under 17
    while computer_score != 0 and computer_score < 17:
        # Within this while loop we will have a card dealt and the computer score updated and stored to the computer_score variable
        computer_cards.append(deal_card()) 
        computer_score = calculate_score(computer_cards)

    # Have print statements and f-strings that print our the users and computers final hands and scores
    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    # Add one final print statement that shows the output of our compare() function created above
    print(compare(user_score, computer_score))

# One final while loop that takes the user's input to start or leave the program, this also will be the first thing that will show when the program is run
while input("Want to play Blackjack? Type 'y' to start, hit enter to leave: "):
    # use the clear() function we created to clear all old output and hides the command line from view
    clear()
    # Start the game over
    playgame()