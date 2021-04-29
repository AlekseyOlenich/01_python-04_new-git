import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Реализуем функцию, которая делит промежутки пополам для выявления загаданного числа"""
    count = 1
    # установили верхнюю и нижнюю границу области и сформировали первое предположение по числу
    lower_bound = 1
    # верхняя граница устанавливается на 1-цу больше, чтобы не анализировать получение случайного числа 100
    upper_bound = 101
    predict = lower_bound + (upper_bound-lower_bound) // 2

    # основной цикл по выработке предположений о значении числа
    while number != predict:
        count += 1
        if number > predict:
            lower_bound = predict
        elif number < predict:
            upper_bound = predict
        predict = lower_bound + (upper_bound - lower_bound) // 2

    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=100000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score_game(game_core_v3)
