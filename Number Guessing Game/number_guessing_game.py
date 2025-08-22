from random import randint


def play():
    print("Welcome To Number Guessing Game!")
    score = 0
    play_again = True
    while play_again:
        number = randint(1, 10)
        while True:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess == number:
                score += 1
                print("Congratulations! You got it!")
                break
            elif guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            play_again = False
    print(f"Your final score: {score}")
play()