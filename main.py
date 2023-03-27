import random

def getChoices():
  playerChoices = input( "Enter a choice(rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computerChoices = random.choice(options)
  choices = {"player": playerChoices, "computer": computerChoices} 
  return choices

def checkWin(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You Lose"
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cuts paper! You lose"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
       return 'Rock smashes scissors! You lose'

choices = getChoices()
result = checkWin(choices["player"], choices["computer"])
print(result)
