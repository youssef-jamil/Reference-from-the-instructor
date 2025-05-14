# Start the game
# Ask the player to make a move (r, p, s)
# PC would select a move randomly
# PC == Player -> Tie
# (Player == P and PC == Rock) or (Player == R and PC == Scissors) or (Player == Scissors and PC == Paper)
## User won / You won
# Any other case
## PC won / You lose

import random

# Mphamed
user = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors\n")
pc = random.choice(["r", "p", "s"])

print(f"User played: {user}")
print(f"PC played: {pc}")

if user == pc:
    print("It's a tie!")
elif (
    (user == "p" and pc == "r")
    or (user == "r" and pc == "s")
    or (user == "s" and pc == "p")
):
    print("You won!")
elif (
    (user == "r" and pc == "p")
    or (user == "s" and pc == "r")
    or (user == "p" and pc == "s")
):
    print("PC won!")
else:
    print("You lose!")
