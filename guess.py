import random
secret = random.randint(1, 100)
print("I am thinking a number between 1 and 100")
print("you have 7 attempts left")
count = 0
while count < 7:
    num = int(input("Guess: "))
    if    num == secret:
        print("correct")
        print(f"you finished this in {count + 1} attempts")
        break
    elif num <= secret :
        print("Too Low")
        print(f"you have {6 - count} attempts left")
    elif num >= secret:
        print("Too High")
        print(f"you have {6 - count} attempts left")
    count = count + 1
