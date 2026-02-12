from filemon_and_friends import get_ingens_1_change_attack, get_ingens_1_change_defence, get_ingens_2_change_attack, get_ingens_2_change_defence, get_mukatra_1_change_attack, get_mukatra_1_change_defence, get_mukatra_2_change_attack, get_mukatra_2_change_defence
from use_your_weapon import use_your_weapon_player1, use_your_weapon_player2

def part1(pa, pd, hit, mukatra, ingens, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    hit, use_sword, use_helmet = use_your_weapon_player1(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)

    hit, ingens, counter = get_ingens_1_change_defence(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player1(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)


    hit, mukatra, counter = get_mukatra_1_change_defence(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player1(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)


    hit, ingens, counter = get_ingens_2_change_attack(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player1(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)


    hit, mukatra, counter = get_mukatra_2_change_attack(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player1(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)

    return hit, mukatra, ingens, use_sword, use_helmet

def part2(pa, pd, hit, mukatra, ingens, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    hit, use_sword, use_helmet = use_your_weapon_player2(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)

    hit, ingens, counter = get_ingens_2_change_defence(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player2(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)

    hit, mukatra, counter = get_mukatra_2_change_defence(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player2(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)

    hit, ingens, counter = get_ingens_1_change_attack(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player2(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)

    hit, mukatra, counter = get_mukatra_1_change_attack(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_sword, use_helmet = use_your_weapon_player2(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2)
    return hit, mukatra, ingens, use_sword, use_helmet
