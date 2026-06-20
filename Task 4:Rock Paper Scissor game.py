import random
print("Hello user! Welcome to the rock paper and scissors game")
print("Game instructions:\n\
      1. Enter your choice (Rock,Paper or scissors).\n\
      2. The computer will generate an entity from the sample (rock,paper,scissors).\n\
      3. Each round's result will be determined by the player's and Computer's choice\n\
         \t\'rock beats scissors\'\n\
         \t\'paper beats rock\'\n\
         \t\'scissors beats paper\'\n\
      4. 3 points is awarded for a win, both you and computer get 1 for a draw and none for a loss.\n\
      5. The final result is displayed after analysing ech game's results.")
sample=['rock','paper','scissors']
player_score=0
comp_score=0
round_num=1
while True:
    player_choice=input("Enter your choice (rock or paper or scissors):")
    comp_choice=random.choice(sample)
    print("Round:",round_num)
    print("Player's choice:",player_choice)
    print("Computer's choice:",comp_choice)
    if player_choice=='rock':
        if comp_choice=='paper':
            print("Oops! you lost")
            comp_score+=3
        elif comp_choice=='scissors':
            print("Hurray! You won")
            player_score+=3
    elif player_choice=='paper':
        if comp_choice=='rock':
            print("Hurray! you won")
            player_score+=3
        elif comp_choice=='scissors':
            print("Oops! you lost")
            comp_score+=3
    elif player_choice=='scissors':
        if comp_choice=='rock':
            print("Oops! You lost")
            comp_score+=3
        elif comp_choice=='paper':
            print("Hurray! you won")
            player_score+=3
    else:
        print("Invalid choice")
        continue
    if player_choice==comp_choice:
        print("You are so close! it's a tie")
        player_score+=1
        comp_score+=1
    round_num+=1
    c=input("Do you want to continue(y/n):").lower()
    if c=='n':
        break
print("\t\t\tFinal results\t\t\t")
print("\tPlayer score\t\t\tComputer score")
print("\t\t",player_score,"\t\t\t\t",comp_score)
if player_score>comp_score:
    print("Congratulations!!! You have won")
elif player_score<comp_score:
    print("Oops!! You lost. Better luck next time")
elif player_score==comp_score:
    print("You are so close!! It's a draw")
print("Thank you for playing!!!")



