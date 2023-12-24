---

# Rock Paper Scissors Game

This Python-based application enables users to engage in the timeless game of Rock Paper Scissors against a computer opponent.

## Overview

This program simulates the classic game, allowing users to input their choice and compete against the computer's randomly generated selection. The outcome is determined by standard game rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.

## How to Play

1. **Getting Started**
   - Execute the Python file in a compatible Python environment.
   - Follow the on-screen instructions to commence gameplay.

2. **Gameplay Instructions**
   - Users are prompted to input their choice: Rock, Paper, or Scissors.
   - Input the corresponding number (1 for Rock, 2 for Paper, 3 for Scissors).
   - The program will randomly generate the computer's choice.
   - Both selections (user and computer) will be displayed.

3. **Outcome**
   - The program will determine the game winner based on the rules and display the result.
   - "Computer Wins" if the computer emerges victorious.
   - "You Win" if the user triumphs.
   - "Match Draw" if both sides make identical choices.

## Code Explanation

Here is the Python code for the Rock Paper Scissors game:

```python
import random

def who_win(computer, user):
    if computer == user:
        return 0
    elif (computer == "Rock" and user == "Paper") or \
         (computer == "Paper" and user == "Scissor") or \
         (computer == "Scissor" and user == "Rock"):
        return 2
    else:
        return 1

print('1) Rock \n2) Paper\n3) Scissor')
user = "0"
while user not in ["1", "2", "3"]:
    user = input("Enter Choice :- ")
    if user == "1":
        user = "Rock"
        break
    elif user == '2':
        user = "Paper"
        break
    elif user == '3':
        user = "Scissor"
        break
    else:
        print("Wrong Choice, Choose Again.")

options = ["Rock", "Paper", "Scissor"]
computer = options[random.randint(0, 2)]

print("GAME:  Computer Choice : ", computer, " & Your Choice : ", user)
score = who_win(computer, user)
if score == 1:
    print("Computer Wins")
elif score == 2:
    print("You Win")
else:
    print("Match Draw")
```

## Contributions

Contributions to this project are welcome! If you have suggestions, identified issues, or wish to introduce new features, fork this repository, make your modifications, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).

---
