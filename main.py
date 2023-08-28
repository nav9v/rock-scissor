import random 
def get_choices():


   player_choice =input ("Enter a choice(rock,paper,scissors): ")
   options=["rock","paper","scissors"]
   computer_choice =random.choice(options)
   
   choices={"player": player_choice,"computer":"computer_choice"}

   return choices

def get_win(player,computer):
   print ("you chose {player}, computer chose{computer}")
   if player == computer:
    return "it's a tie!"

   elif player == "rock" 
     if computer =="sicssors":
         return "you won!"
       else:
         return "you lost!"
   elif player == "paper"
       if computer =="rock":
         return "you won!"
       else:
         return "you lost!"
   elif player == "scissors"  
         if computer =="paper":
            return "you won!"
         else:
            return "you lost!"
check_win("rock","paper")  





   