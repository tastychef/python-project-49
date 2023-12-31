import prompt


def run(welcome=""):
    print("Welcome to the Brain Games!")
    if welcome:
        print(f"{welcome}")
    print()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def get_answer(question):
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    return answer
