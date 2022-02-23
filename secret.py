# homework 1.2: Guess the secret number
secret = 66
guess = int(input("Choose a number between 0 and 100! "))


if guess != secret:
    print("Sorry! You haven't found the secret number!")
else:
    print("Congratulations! You have found the secret number!")
