import random
from player1 import player1_ini_attack
from player2 import player2_ini_attack
def get_initiative(ini_1, ini_2, player1, player2):
    print('🚧'*15)
    while True:
        incube_1 = ini_1 * '🟦 '
        incube_2 = ini_2 * '🟦 '
        player_1 = player1_ini_attack(ini_1)
        player_2 = player2_ini_attack(ini_2)
        player_1_ini = sum(player_1)
        player_2_ini = sum(player_2)
        print(f'\n{player1}:\n{incube_1}\nInitiative: {player_1_ini}\n')
        print(f'{player2}:\n{incube_2}\nInitiative: {player_2_ini}\n')
        if player_1_ini > player_2_ini:
            return 1, player_1, player_2
        if player_1_ini < player_2_ini:
            return 2, player_1, player_2

