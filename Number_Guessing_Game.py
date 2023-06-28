#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# player_lose=False

print("""
 _____ _     _____ ____  ____      _____  _     _____     _      _     _     
/  __// \ /\/  __// ___\/ ___\    /__ __\/ \ /|/  __/    / \  /|/ \ /\/ \__/|
| |  _| | |||  \  |    \|    \      / \  | |_|||  \      | |\ ||| | ||| |\/||
| |_//| \_/||  /_ \___ |\___ |      | |  | | |||  /_     | | \||| \_/|| |  ||
\____\\____/\____\\____/\____/      \_/  \_/ \|\____\    \_/  \|\____/\_/  \|
""")
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
level=input("Choose a difficulty.Type 'easy' or 'hard':")
number=random.randint(1,100)
print(number)
if level=="easy":
    player_lose=False
    print("You have 10 attempts remaining to guess the number.")
    player_life=10
    while player_lose==False:
        guess=int(input("Make a guess: "))
        if guess==number:
            print(f"You got it! The answer was {number}")
        elif guess!=number:
            if guess<number:
                print("""Too low.
                Guess again""")
            elif guess>number:
                print("""Too high.
                Guess again""")
            player_life=player_life-1
            print(f"You have {player_life} attempts remaining to guess the number.")
            if player_life==0:
                player_lose=True
                print("You've run out of guesses, you lose.")
if level=="hard":
    player_lose=False
    print("You have 5 attempts remaining to guess the number.")
    player_life=5
    while player_lose==False:
        guess=int(input("Make a guess: "))
        if guess==number:
            print(f"You got it! The answer was {number}")
        elif guess!=number:
            if guess<number:
                print("""Too low.
                Guess again""")
            elif guess>number:
                print("""Too high.
                Guess again""")
            player_life=player_life-1
            print(f"You have {player_life} attempts remaining to guess the number.")
            if player_life==0:
                player_lose=True
                print("You've run out of guesses, you lose.")