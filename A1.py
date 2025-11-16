import random
play=True
guess_count=0
n=str(random.randint(10,20))
print("Welcome to the random maths game!")
print("Guess the number and win points!")
print("The game will end when you guess correct number.")
while play:
    guess=str(input("Enter your guess: "))
    if guess==n:
        print("Correct!you won.")
        print("The number was, ",n)
        break
    else:
        print("Incorrect!!")
        print("Try again! \n")
        print(guess_count=guess_count+1,"Guess count")
        