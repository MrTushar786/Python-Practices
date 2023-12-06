import random

ran = random.randint(1, 20)
a = input("Think of a number (y or n): ")

if a == 'y':
    b = input("Add the same number to it (y or n): ")
    
    if b == 'y':
        c = input(f"Add {ran} to it (y or n): ")
        
        if c == 'y':
            d = input("Halve the number (y or n): ")
            
            if d == 'y':
                e = input("Subtract the number you first thought of (y or n): ")
                
                if e == 'y':
                    print(f"You originally thought of the number: {ran}")
                else:
                    print("Enter valid and try again")
            else:
                print("Enter valid and try again")
        else:
            print("Enter valid and try again")
    else:
        print("Enter valid and try again")
else:
    print("Enter valid and try again")
