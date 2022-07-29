# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота


from game_modes import player_vs_player, player_vs_computer
from utils import give_number, candy_can_take
import random

print('''
    привет, давай поиграем в конфеты. Правила такие: на столе будут лежать конфеты. 
    В свой ход можно забрать от 1 до 28 конфет. Тот, кто берет последнюю конфету - проиграл''')

candy_count = give_number('введите количество конфет на столе: ')
max_for_step = candy_can_take('сколько можно брать за 1 ход: ', candy_count)


while True:
    type_game = input('''
    выбери режим игры: 
    1 - игрок против игрока
    2 - игрок против компа
    3 - выход из игры 
    ''')
    if not type_game.isdigit():
        print('Вы ввели не число')
    elif type_game not in '123':
        print('такого режима нет')
    elif type_game == '1':
        print ('запускаю режим: игрок против игрока')
        player_vs_player(candy_count, max_for_step)
    elif type_game == '2':
        print ('запускаю режим: игрок против компа')
        player_vs_computer (candy_count, max_for_step) 
    else:
        print('пока! надеюсь скоро увидеться снова')
        break
    input('нажмите enter для продолжения')    