"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint as rdi

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUMBER_OF_ATTEMPTS = 10

count = 0
hidden_number = rdi(LOWER_LIMIT, UPPER_LIMIT)
while count < NUMBER_OF_ATTEMPTS:
    user_number = int(input('Введите число: '))
    count += 1
    if user_number < hidden_number:
        print("Загаданое число больше")
    elif user_number > hidden_number:
        print("Загаданое число меньше")
    else:
        print(f'Поздравляю вы угадали! {hidden_number}')
        break
else:
    print(f'Не угадали, загаданное число {hidden_number}')
