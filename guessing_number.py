import random

number = random.randint(0,100)
count = 0
run = True

while run:
    guess =  input("Guess the number: ")
    guess =int(guess)
    if guess < number:
        print(f"{guess} is too low")
        count+=1
    elif guess > number:
        print(f"{guess} larger than the number")
        count +=1
    elif guess == number:
        count+=1
        
        if count == 1:
            print(f"Got it on the first try, WOWW!!!!!\n")
            print("Alright mate, you are HOT CAKE!!!")
            break

        if count > 1:

            print(f"\nTook you {count} guess(es)\n" )
            print("\nAlright mate, you are HOT CAKE!!!")
            break
        