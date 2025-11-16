import random
option=["rock","paper","S\scissor"]
user=input("Enter your choice rock/paper/scissor : ")
computer=random.choice(option)
print("you choose",user,"and computer choose",computer)
if user==computer:
    print("Its a tie")

elif user=="rock" and computer=="scissor":
    print("Rock smashes scissor. You won!!")

elif user=="rock" and computer=="paper":
    print("Paper smashes rock. You won!!")

elif user=="paper" and computer=="scissor":
    print("scissor crushes paper. Computer won!!")

elif user=="paper" and computer=="rock":
    print("Paper crushes rock. Computer won!!")

elif user=="scissor" and computer=="rock":
    print("Rock smashes scissor. Computer won!!")

elif user=="scissor" and computer=="paper":
    print("scissor crushes paper. Computer won!!")

else:
    print("Game")