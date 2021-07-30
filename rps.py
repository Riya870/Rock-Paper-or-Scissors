import random 
# ROCK PAPER SCISSORS
def gameWin(computer,player):
    # if both values are equal then it declare tie
    if computer == player:
            return None
    #check for all possibilities when computer chose R(Rock)
    elif computer == 'R':
        if player == 'P':
            print(player,"covers",computer)
            return True
        elif player =='S':
            print(computer, "smashes",player)
            return False
    #check for all possibilities when computer chose P(Paper)               
    elif computer == 'P':
        if player == 'S':
            print(player,"cut",computer)
            return True
        elif player =='R':
            print(computer, "covers",player)
            return False
    #check for all possibilities when computer chose S(Scissors)
    elif computer == 'S':
        if player == 'R':
            print(player, "smashes",computer)
            return True
        elif player =='P':
            print(computer, "cut",player)
            return False
    
print("Computer Turn: Rock(R) Paper(P) or Scissors(S)? ")
randNo = random.randint(1,3)
if randNo ==1:
    computer ='R'
elif randNo ==2:
    computer ='P'
elif randNo ==3:
    computer ='S'

player =input("Player's Turn: Rock(R),Paper(P) or Scissors(S)? ")

a =gameWin(computer,player)

print(f"Computer chose: {computer}")
print(f"Player chose: {player}")

if a == None:
    print("Game is Tie!")
elif a == True:
    print("player win!")
else:
    print("player lose!")
