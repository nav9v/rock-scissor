import random 
def get_choices():


   player_choice =input ("Enter a choice(rock,paper,scissors): ")
   options=["rock","paper","scissors"]
   computer_choice =random.choice(options)
   
   choices={"player": player_choice,"computer":computer_choice}

   return choices

def check_win(player,computer):
   print (f"you chose {player}, computer chose {computer}")
   if player == computer:
    return "it's a tie!"

   elif player == "rock":
     if computer =="sicssors":
       return "you won!"
     else:
       return "you lost!"
   
   elif player == "paper":
     if computer =="rock":
       return "you won!"
     else:
       return "you lost!"
   
   elif player == "scissors":
     if computer =="paper":
       return "you won!"
     else:
       return "you lost!"
   
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

# choices = {"player": "rock", "computer": "paper"}
# p_choices = choices["computer"]





   