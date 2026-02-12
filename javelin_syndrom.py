from gladiator_special import ingens_1_change_attack_javelin, ingens_1_change_defence_javelin, ingens_2_change_attack_javelin, ingens_2_change_defence_javelin, mukatra_1_change_attack_javelin, mukatra_1_change_defence_javelin, mukatra_2_change_attack_javelin, mukatra_2_change_defence_javelin
from your_helmet import your_helmet_1, your_helmet_2

def get_javelin_ingens_1(pa, pd, hit, ingens, mukatra, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):

    hit, ingens, counter = ingens_1_change_defence_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_helmet = your_helmet_2(pa, pd, hit, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    hit, mukatra, counter = mukatra_1_change_defence_javelin(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_helmet = your_helmet_2(pa, pd, hit, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    hit, ingens, counter = ingens_2_change_attack_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    hit, mukatra, counter = mukatra_2_change_attack_javelin(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    return hit, ingens, mukatra, use_helmet

def get_javelin_ingens_2(pa, pd, hit, ingens, mukatra, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):

    hit, ingens, counter = ingens_2_change_defence_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_helmet = your_helmet_1(pa, pd, hit, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    hit, mukatra, counter = mukatra_2_change_defence_javelin(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    if counter == 'yes':
        hit, use_helmet = your_helmet_1(pa, pd, hit, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    hit, mukatra, counter = mukatra_1_change_attack_javelin(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    hit, ingens, counter = ingens_1_change_attack_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)

    return hit, ingens, mukatra, use_helmet
