import random
from utils import candy_can_take

def player_vs_player(candy_count, max_for_step):
    player1 = input('игрок 1, пожалуйста, представьтесь: ')
    player2 = input('игрок 2, пожалуйста, представьтесь: ')
    players = ['победа игрока: ', player1, player2]
    turn = random.choice([-1, 1])

    while candy_count > 0:
        print(f'на столе конфеты в количестве {candy_count}')
        print(f'ход игрока {players[turn]}')
        candy = candy_can_take('сколько конфет берем: ', candy_count)
        if candy > max_for_step:
            print(f'так нельзя, можно взять максимум {max_for_step}')
            continue
        candy_count = candy_count - candy
        turn = turn *-1
    players.remove(players[-turn])
    print(''.join(players))

def player_vs_computer (candy_count, max_for_step):
    player1 = input('игрок 1, пожалуйста, представьтесь: ')
    computer = input('за игрока 2 играет компьютер, дайте ему имя: ')
    players = ['победа игрока: ', player1, computer]
    turn = random.choice([-1, 1])

    while candy_count > 0:
        print(f'\nна столе конфеты в количестве {candy_count}')
        print(f'ход игрока {players[turn]}')
        if turn == 1:
            candy = candy_can_take('сколько конфет берем: ', candy_count)
            if candy > max_for_step:
                print(f'так нельзя, можно взять максимум {max_for_step}')
                continue
        else:
            candy = random.randint(1, max_for_step if max_for_step < candy_count else candy_count)
            print(f'компьютер берет {candy}')
        candy_count = candy_count - candy
        turn = turn *-1
    players.remove(players[-turn])
    print(''.join(players))