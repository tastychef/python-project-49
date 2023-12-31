import prompt

INCORRECT_ANSWER = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.'''


def run_game(condition: str, generate_game_data: tuple):
    """Приветствие"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    # Принтуем правила игры и генерируем циклы
    print(condition)
    game_loop = 0

    while game_loop < 3:
        question, correct_result = generate_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        # Получаем результат
        corect_result = str(correct_result) == user_answer.lower()

        # Ответ в зависимости корректности ответа
        if not corect_result:
            # Итого: неправильный ответ
            print(INCORRECT_ANSWER.format(user_answer, correct_result))
            print(f'Let\'s try again, {name}!')
            break

        # Итого: правильный ответ
        print('Correct!')

        game_loop += 1

    print(f'Congratulations, {name}!')
