from random import randint


user = input("rock paper or scissors? ")
print("you chose: " + user)

rand = randint(0,2)

if rand == 0:
    rand = "rock"

elif rand == 1:
    rand = "paper"

else:
    rand = "scissors"
    
print("computer chose: " + rand)


# Stalemate condition

if user == rand:
    print("stalemate")
    
    
# win conditions
    
if user == "rock" and rand == "scissors":
    print("victory")
    
if user == "paper" and rand == "rock":
    print("victory")
    
if user == "scissors" and rand == "paper":
    print("victory")
    
# defeat conditions

if user == "rock" and rand == "paper":
    print("defeat")
    
if user == "paper" and rand == "scissors":
    print("defeat")

if user == "scissors" and rand == "rock":
    print("defeat")

    