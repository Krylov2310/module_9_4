import random

print('\033[30m\033[47mДомашнее задание по теме "Создание функций на лету"\033[0m')
print('\033[30m\033[47mЗадача "Функциональное разнообразие":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()

# Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data_write in data_set:
                file.write(str(data_write) + '\n')
        file.close()
    return write_everything


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print()
print(thanks)
