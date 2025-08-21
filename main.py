# Simple Python Quiz Game

def quiz():
    score = 0

    # Questions and answers
    questions = {
        "What is the capital of France? ": "paris",
        "Which language is used for web apps? ": "python",
        "What is 5 + 7? ": "12",
        "Who developed Python? ": "guido van rossum",
        "What is the color of the sky on a clear day? ": "blue"
    }

    print("\nWelcome to the Quiz Game!")
    print("Type your answers (not case sensitive). Let's start!\n")

    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}\n")

    print(f"Your final score is {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent! You got all correct!")
    elif score >= 3:
        print("👍 Good job, keep practicing!")
    else:
        print("😅 Better luck next time!")


# Run the game
quiz()
