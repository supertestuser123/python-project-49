import prompt as prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
