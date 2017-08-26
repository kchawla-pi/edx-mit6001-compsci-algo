low = 0
high = 100
eps = 0.001
num = 100
print("Please think of a number between 0 and 100!")
guess = -10000
while not (num - eps <= guess <= num + eps):
    guess = int((low + high) / 2)
    print("Is your secret number {}?".format(guess))
    resp = input("Enter 'h' to indicate the guess is too high."
                 "Enter 'l' to indicate the guess is too low."
                 "Enter 'c' to indicate I guessed correctly. "
                 )
    if resp.lower() == 'c':
        break
    elif resp.lower() == 'l':
        low = guess
    elif resp.lower() == 'h':
        high = guess
    else:
        print("Sorry, I did not understand your input.")
        
print("Game over. Your secret number was:", guess)
