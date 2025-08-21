import requests

# open trivia database API URL
response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data = response.json()


def quiz():
    score = 0
    print("\n")
    print("Welcome to Quiz Game!\n")
    print("Type your answers True / False and if you want to exit just type exit from game (not case sensitive). Let's start!\n")

    for i in range(len(data["results"])):
        questions = (data["results"][i]["question"])
        correct_answer = data["results"][i]["correct_answer"]
        incorrect_answers =  data["results"][i]["incorrect_answers"][0]

        answer = input(f"{questions}? ").title()

        if answer == correct_answer:
            print("✅ Correct!")
            score += 1
        elif answer == "Exit":
            break
        else:
            print(f"❌ Wrong! It was {correct_answer}")


    print(f"Your final score is {score}/{len(data["results"])}")
    if score == len(data["results"]):
        print("🎉 Excellent! You got all correct!")
    elif score >= 3:
        print("👍 Good job, keep practicing!")
    else:
        print("😅 Better luck next time!")



quiz()