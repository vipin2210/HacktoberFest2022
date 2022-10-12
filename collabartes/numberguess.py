import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")

'''
Output- 
Enter any number: 2
Too low
Enter number again: 5
Too low
Enter number again: 8
you guessed it right!!

'''
