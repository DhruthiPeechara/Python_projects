import random 
playing = True 
number = str(random.randint(10,20))

print("I will generate a number from 0 to 9, and you need to guess the digit one at a time.")
print ("The game ends when you get one hero! ")

while playing:
    guess = int(input("Give me your best guess! \n "))
    if number == guess:
        print ("You win the game ")
        print ("The number was, number  ")
        break

    