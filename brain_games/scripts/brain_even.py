import random
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def ask_question(user_name):
    correct_answers = 0
    for i in range(3):
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        user_answer = input("Your answer: ")

        if (is_even(number) and user_answer.lower() == 'yes') or (
                not is_even(number) and user_answer.lower() == 'no'):
            print("Correct!")
            correct_answers += 1
            if correct_answers == 3:
                print("Congratulations, " + user_name + "!")
                break
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + user_name + "!")
            break


def main():
    print("Welcome to the Brain Games!")
    user_name = str(welcome_user())
    print("Hello, " + user_name + "!")

    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    ask_question(user_name)


if __name__ == "__main__":
    main()
