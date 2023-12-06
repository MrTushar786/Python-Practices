import random

a = random.randint(1, 10)

while True:
    b = int(input("Enter Your Guess: "))
    
    if a == b:
        print("Congratulations, correct!")
        break  
    else:
        print("Better Luck next time")
