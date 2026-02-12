from gladiator_statistics import gladiator1_add_gear, gladiator2_add_gear, gladiator1_attack, gladiator1_defence, gladiator1_ini, gladiator2_attack, gladiator2_defence, gladiator2_ini, gladiator1_special, gladiator2_special
from start import get_start
from attack import get_attack_1, get_attack_2
from javelin import player1_get_javelin, player2_get_javelin

attack_1 = gladiator1_attack()
defence_1 = gladiator1_defence()
ini_1 = gladiator1_ini()
attack_2 = gladiator2_attack()
defence_2 = gladiator2_defence()
ini_2 = gladiator2_ini()
from pyfiglet import Figlet
d = Figlet(font='slant')
player1 = input('Player1 name: ')
player2 = input('Player2 name: ')
axe_1 = 1
axe_2 = 1
shield_1 = 1
shield_2 = 1
net_1 = 1
net_2 = 1
javelin_1 = 1
javelin_2 = 1
ingens = None
mukatra = None
if gladiator1_special() == 'mukatra':
    mukatra = 1
if gladiator1_special() == 'ingens':
    ingens = 1
if gladiator2_special() == 'mukatra':
    mukatra = 1
if gladiator2_special() == 'ingens':
    ingens = 1

while True:
    d = Figlet(font='slant')
    use_sword_1 = 1
    use_helmet_1 = 1
    use_helmet_2 = 1
    use_sword_2 = 1
    filemon = 1
    move_1 = 1
    move_2 = 1
    atak_1 = 1
    atak_2 = 1
    give_1 = 1
    give_2 = 1
    acube_1 = attack_1 * '🟥 '
    decube_1 = defence_1 * '🟫 '
    incube_1 = ini_1 * '🟦 '
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
    end_1 = 1
    end_2 = 1
    try:
        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
            print(f'{player1} win!')
            life = [attack_2, defence_2, ini_2]
            if gladiator1_special() == 'gnejusz' and gladiator2_special() != 'oinomaos':
                print(f"{player2}'s gladiator is injured.")
                break
            if gladiator1_special() == 'kakus' and gladiator2_special != 'oinomaos':
                print(f"{player2}'s gladiator is decapitated!")
                break
            if sum(life) <= 0:
                print(f"{player2}'s gladiator is decapitated!")
                break
            elif sum(life) ==  1:
                print(f"{player2}'s gladiator is injured.")
                break
            elif sum(life) == 2:
                print(f"{player2}'s gladiator gave up.")
                break
        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
            print(f'{player2} win!')
            life = [attack_1, defence_1, ini_1]
            if gladiator2_special() == 'gnejusz' and gladiator1_special() != 'oinomaos':
                print(f"{player1}'s gladiator is injured.")
                break
            if gladiator2_special() == 'kakus' and gladiator1_special != 'oinomaos':
                print(f"{player1}'s gladiator is decapitated!")
                break
            if sum(life) <= 0:
                print(f"{player1}'s gladiator is decapitated!")
                break
            elif sum(life) ==  1:
                print(f"{player1}'s gladiator is injured.")
                break
            elif sum(life) == 2:
                print(f"{player1}'s gladiator gave up.")
                break

        initiative, ingens, mukatra, net_1, net_2 = get_start(ini_1, ini_2, ingens, mukatra, player1, player2, net_1, net_2, filemon)
        if initiative == 1:
            while True:
                print(f'\n{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                attack_player_1 = input(f'{player1}, your move: {atak_1 * '⚔️'}  {move_1 * '🏃'} ').strip(' ').lower()
                if attack_player_1 == 'g' and give_1 == 1 and move_1 == 1 and atak_1 == 1:
                    if gladiator1_add_gear() != 'javelin':
                        give_1 = 0
                        give_2 = 0
                        initiative = 2
                        print('\n🔄')
                        break
                    elif javelin_1 == 1:
                        give_1 = 0
                        give_2 = 0
                        initiative = 2
                        print('\n🔄')
                        break
                    else:
                        print(f"{player1}, you can't do this!")
                if attack_player_1 == 'j':
                    if gladiator1_add_gear() != 'javelin':
                        print(f"{player1}, you can't do this!")
                    elif javelin_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif javelin_1 == 1:
                        javelin_1 , mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, shield_2 = player1_get_javelin(ini_1, javelin_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player1, player2, shield_2)
                if attack_player_1 == 'a':
                    if atak_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif atak_1 == 1:
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2 = get_attack_1(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2, player1, player2)
                        atak_1 = 0
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                            raise ValueError
                if attack_player_1 == 'm':
                    if move_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif move_1 == 1:
                        move_1 = 0
                        print('🏃  ' * ini_1)
                if move_1 == 1 and ini_1 > ini_2 and atak_1 == 0 and javelin_1 == 0:
                    while True:
                        j = input(f'{player1}, do you want jump back? ')
                        if j == 'y':
                            move_1 = 0
                            print('🏃  ' * ini_1)
                            break
                        elif j == 'n':
                            break
                    break
                if atak_1 == 0 and move_1 == 0:
                    if gladiator1_add_gear() == 'javelin' and javelin_1 == 0:
                        break
                    else:
                        break
                if attack_player_1 == 'p':
                    break
                if attack_player_1 == 'e':
                    end_1 = 0
                    break
                if attack_player_1 == 'g' and give_1 == 0:
                    print(f"{player1}, you can't do this!")
                if attack_player_1 != 'm' and attack_player_1 != 'j' and attack_player_1 != 'a' and attack_player_1 != 'g' and attack_player_1 != 'e':
                    print(f"{player1}, you can't do this!")

        if initiative == 1:
            while True:
                print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                attack_player_2 = input(f'{player2}, your move: {atak_2 * '⚔️'}  {move_2 * '🏃'} ').strip().lower()
                if attack_player_2 == 'j':
                    if gladiator2_add_gear() != 'javelin':
                        print(f"{player2}, you can't do this!")
                    if javelin_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif javelin_2 == 1:
                        javelin_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2, shield_1 = player2_get_javelin(ini_2, javelin_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1, player2, shield_1)
                if attack_player_2 == 'a':
                    if atak_2 == 0:
                       print(f"{player2}, you can't do this!")
                    elif atak_2 == 1:
                        atak_2 = 0
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1 = get_attack_2(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1, player1, player2)
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                            raise ValueError
                if attack_player_2 == 'm':
                    if move_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif move_2 == 1:
                        print('🏃  ' * ini_2)
                        move_2 = 0
                if move_2 == 0 and javelin_2 == 0 and atak_2 == 0:
                    break
                if move_2 == 1 and ini_2 > ini_1 and atak_2 == 0 and javelin_2 == 0:
                    while True:
                        j = input(f'{player2}, do you want jump back? ')
                        if j == 'y':
                            move_2 = 0
                            print('🏃  ' * ini_2)
                            break
                        elif j == 'n':
                            break
                    break
                if atak_2 == 0 and move_2 == 0:
                    if gladiator2_add_gear() == 'javelin' and javelin_2 == 0:
                        break
                    else:
                        break
                if attack_player_2 == 'p':
                    break
                if attack_player_2 == 'e':
                    end_2 = 0
                    break
                if attack_player_2 == 'g':
                    print(f"{player2}, you can't do this!")
                if attack_player_2 != 'm' and attack_player_2 != 'j' and attack_player_2 != 'a' and attack_player_2 != 'g' and attack_player_2 != 'e':
                    print(f"{player2}, you can't do this!")





        if initiative == 2:
            while True:
                print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                attack_player_2 = input(f'{player2}, your move: {atak_2 * '⚔️'}  {move_2 * '🏃'} ').strip().lower()
                if attack_player_2 == 'g' and give_2 == 1 and move_2 == 1 and atak_2 == 1:
                    if gladiator2_add_gear() != 'javelin':
                        give_1 = 0
                        give_2 = 0
                        initiative = 3
                        print('\n🔄')
                        break
                    elif javelin_2 == 1:
                        give_1 = 0
                        give_2 = 0
                        initiative = 3
                        print('\n🔄')
                        break
                    else:
                        print(f"{player2}, you can't do this!")
                if attack_player_2 == 'j':
                    if gladiator2_add_gear() != 'javelin':
                        print(f"{player2}, you can't do this!")
                    if javelin_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif javelin_2 == 1:
                        javelin_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2, shield_1 = player2_get_javelin(ini_2, javelin_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1, player2, shield_1)
                if attack_player_2 == 'a':
                    if atak_2 == 0:
                       print(f"{player2}, you can't do this!")
                    elif atak_2 == 1:
                        atak_2 = 0
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1 = get_attack_2(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1, player1, player2)
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                            raise ValueError
                if attack_player_2 == 'm':
                    if move_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif move_2 == 1:
                        move_2 = 0
                        print('🏃  ' * ini_2)
                if move_2 == 0 and javelin_2 == 0 and atak_2 == 0:
                    break
                if move_2 == 1 and ini_2 > ini_1 and atak_2 == 0 and javelin_2 == 0:
                    while True:
                        j = input(f'{player2}, do you want jump back? ')
                        if j == 'y':
                            move_2 = 0
                            print('🏃  ' * ini_2)
                            break
                        elif j == 'n':
                            break
                if atak_2 == 0 and move_2 == 0:
                    if gladiator2_add_gear() == 'javelin' and javelin_2 == 0:
                        break
                    else:
                        break
                    break
                if attack_player_2 == 'p':
                    break
                if attack_player_2 == 'e':
                    end_2 = 0
                    break
                if attack_player_2 == 'g' and give_2 == 0:
                    print(f"{player2}, you can't do this!")
                if attack_player_2 != 'm' and attack_player_2 != 'j' and attack_player_2 != 'a' and attack_player_2 != 'g' and attack_player_2 != 'e':
                    print(f"{player2}, you can't do this!")

        if initiative == 2:
            while True:
                print(f'\n{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                attack_player_1 = input(f'{player1}, your move: {atak_1 * '⚔️'}  {move_1 * '🏃'} ').strip(' ').lower()
                if attack_player_1 == 'j':
                    if gladiator1_add_gear() != 'javelin':
                        print(f"{player1}, you can't do this!")
                    if javelin_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif javelin_1 == 1:
                        javelin_1 , mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, shield_2 = player1_get_javelin(ini_1, javelin_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1,player1, player2, shield_2)
                if attack_player_1 == 'a':
                    if atak_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif atak_1 == 1:
                        atak_1 = 0
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2 = get_attack_1(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2, player1, player2)
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                            raise ValueError
                if attack_player_1 == 'm':
                    if move_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif move_1 == 1:
                        print('🏃  ' * ini_1)
                        move_1 = 0
                if move_1 == 0 and javelin_1 == 0 and atak_1 == 0:
                    break
                if move_1 == 1 and ini_1 > ini_2 and atak_1 == 0 and javelin_1 == 0:
                    while True:
                        j = input(f'{player1}, do you want jump back? ')
                        if j == 'y':
                            move_1 = 0
                            print('🏃  ' * ini_1)
                            break
                        elif j == 'n':
                            break
                    break
                if atak_1 == 0 and move_1 == 0:
                    if gladiator1_add_gear() == 'javelin' and javelin_1 == 0:
                        break
                    else:
                        break
                if attack_player_1 == 'p':
                    break
                if attack_player_1 == 'e':
                    end_1 = 0
                    break
                if attack_player_1 == 'g':
                    print(f"{player1}, you can't do this!")
                if attack_player_1 != 'm' and attack_player_1 != 'j' and attack_player_1 != 'a' and attack_player_1 != 'g' and attack_player_1 != 'e':
                    print(f"{player1}, you can't do this!")








        if initiative == 3:
            while True:
                print(f'\n{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                attack_player_3 = input(f'{player1}, your move: {atak_1 * '⚔️'}  {move_1 * '🏃'} ').strip(' ').lower()
                if attack_player_3 == 'p':
                    break
                if attack_player_3 == 'j':
                    if gladiator1_add_gear() != 'javelin':
                        print(f"{player1}, you can't do this!")
                    elif javelin_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif javelin_1 == 1:
                        javelin_1 , mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, shield_2 = player1_get_javelin(ini_1, javelin_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player1, player2, shield_2)
                if attack_player_3 == 'a':
                    if atak_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif atak_1 == 1:
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2 = get_attack_1(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2, player1, player2)
                        atak_1 = 0
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                            raise ValueError
                if attack_player_3 == 'm':
                    if move_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif move_1 == 1:
                        print('🏃  ' * ini_1)
                        move_1 = 0
                if move_1 == 0 and javelin_1 == 0 and atak_1 == 0:
                    break
                if move_1 == 1 and ini_1 > ini_2 and atak_1 == 0 and javelin_1 == 0:
                    while True:
                        j = input(f'{player1}, do you want jump back? ')
                        if j == 'y':
                            move_1 = 0
                            print('🏃  ' * ini_1)
                            break
                        elif j == 'n':
                            break
                    break
                if atak_1 == 0 and move_1 == 0:
                    if gladiator1_add_gear() == 'javelin' and javelin_1 == 0:
                        break
                    else:
                        break
                if attack_player_3 == 'e':
                    end_1 = 0
                    break
                if attack_player_3 == 'g':
                    print(f"{player1}, you can't do this!")
                if attack_player_3 != 'm' and attack_player_3 != 'j' and attack_player_3 != 'a' and attack_player_3 != 'g' and attack_player_3 != 'e':
                    print(f"{player1}, you can't do this!")


        if initiative == 3:
            while True:
                print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                attack_player_4 = input(f'{player2}, your move: {atak_2 * '⚔️'}  {move_2 * '🏃'} ').strip().lower()
                if attack_player_4 == 'j':
                    if gladiator2_add_gear() != 'javelin':
                        print(f"{player2}, you can't do this!")
                    if javelin_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif javelin_2 == 1:
                        javelin_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2, shield_1 = player2_get_javelin(ini_2, javelin_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1, player2, shield_1)
                if attack_player_4 == 'a':
                    if atak_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif atak_2 == 1:
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1 = get_attack_2(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1, player1, player2)
                        atak_2 = 0
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                            raise ValueError
                if attack_player_4 == 'm':
                    if move_2 == 0:
                        print(f"{player2}, you can't do this!")
                    move_2 = 0
                    print('🏃  ' * ini_2)
                if move_2 == 0 and javelin_2 == 0 and atak_2 == 0:
                    break
                if move_2 == 1 and ini_2 > ini_1 and atak_2 == 0 and javelin_2 == 0:
                    while True:
                        j = input(f'{player2}, do you want jump back? ')
                        if j == 'y':
                            move_2 = 0
                            print('🏃  ' * ini_2)
                            break
                        elif j == 'n':
                            break
                    break
                if atak_2 == 0 and move_2 == 0:
                    if gladiator2_add_gear() == 'javelin' and javelin_2 == 0:
                        break
                    else:
                        break
                if attack_player_4 == 'p':
                    break
                if attack_player_4 == 'e':
                    end_2 = 0
                    break
                if attack_player_4 == 'g':
                    print(f"{player2}, you can't do this!")
                if attack_player_4 != 'm' and attack_player_4 != 'j' and attack_player_4 != 'a' and attack_player_4 != 'g' and attack_player_4 != 'e':
                    print(f"{player2}, you can't do this!")


        if atak_1 == 1 and end_1 == 1:
           initiative = 4
        elif ini_1 > ini_2 and move_1 == 1 and end_1 == 1:
           initiative = 4
        elif gladiator1_add_gear() == 'javelin' and javelin_1 == 1 and end_1 == 1:
            initiative = 4
        elif move_1 == 1 and end_1 == 1:
            initiative = 4






        if initiative == 4:
            while True:
                print(f'\n{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                attack_player_3 = input(f'{player1}, your move: {atak_1 * '⚔️'}  {move_1 * '🏃'} ').strip(' ').lower()
                if attack_player_3 == 'p':
                    break
                if attack_player_3 == 'j':
                    if gladiator1_add_gear() != 'javelin':
                        print(f"{player1}, you can't do this!")
                    elif javelin_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif javelin_1 == 1:
                        javelin_1 , mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, shield_2 = player1_get_javelin(ini_1, javelin_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player1, player2, shield_2)
                if attack_player_3 == 'a':
                    if atak_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif atak_1 == 1:
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2 = get_attack_1(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2, player1, player2)
                        atak_1 = 0
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                            raise ValueError
                if attack_player_3 == 'm':
                    if move_1 == 0:
                        print(f"{player1}, you can't do this!")
                    elif move_1 == 1:
                        print('🏃  ' * ini_1)
                        move_1 = 0
                if move_1 == 0 and javelin_1 == 0 and atak_1 == 0:
                    break
                if move_1 == 1 and ini_1 > ini_2 and atak_1 == 0 and javelin_1 == 0:
                    while True:
                        j = input(f'{player1}, do you want jump back? ')
                        if j == 'y':
                            move_1 = 0
                            print('🏃  ' * ini_1)
                            break
                        elif j == 'n':
                            break
                    break
                if atak_1 == 0 and move_1 == 0:
                    if gladiator1_add_gear() == 'javelin' and javelin_1 == 0:
                        break
                    else:
                        break
                if attack_player_3 == 'e':
                    end_1 = 0
                    break
                if attack_player_3 == 'g':
                    print(f"{player1}, you can't do this!")
                if attack_player_3 != 'm' and attack_player_3 != 'j' and attack_player_3 != 'a' and attack_player_3 != 'g' and attack_player_3 != 'e':
                    print(f"{player1}, you can't do this!")


        if atak_2 == 1 and end_2 == 1:
            initiative = 5
        elif ini_2 > ini_1 and move_2 == 1 and end_2 == 1:
            initiative = 5
        elif move_2 == 1 and end_2 == 1:
            initiative = 5
        elif gladiator2_add_gear() == 'javelin' and javelin_2 == 1 and end_2 == 1:
            inititaive = 5

        if initiative == 5:
            while True:
                print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                attack_player_4 = input(f'{player2}, your move: {atak_2 * '⚔️'}  {move_2 * '🏃'} ').strip().lower()
                if attack_player_4 == 'j':
                    if gladiator2_add_gear() != 'javelin':
                        print(f"{player2}, you can't do this!")
                    if javelin_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif javelin_2 == 1:
                        javelin_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2, shield_1 = player2_get_javelin(ini_2, javelin_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1, player2, shield_1)
                if attack_player_4 == 'a':
                    if atak_2 == 0:
                        print(f"{player2}, you can't do this!")
                    elif atak_2 == 1:
                        attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1 = get_attack_2(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1, player1, player2)
                        atak_2 = 0
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                            raise ValueError
                if attack_player_4 == 'm':
                    if move_2 == 0:
                        print(f"{player2}, you can't do this!")
                    move_2 = 0
                    print('🏃  ' * ini_2)
                if move_2 == 0 and javelin_2 == 0 and atak_2 == 0:
                    break
                if move_2 == 1 and ini_2 > ini_1 and atak_2 == 0 and javelin_2 == 0:
                    while True:
                        j = input(f'{player2}, do you want jump back? ')
                        if j == 'y':
                            move_2 = 0
                            print('🏃  ' * ini_2)
                            break
                        elif j == 'n':
                            break
                    break
                if atak_2 == 0 and move_2 == 0:
                    if gladiator2_add_gear() == 'javelin' and javelin_2 == 0:
                        break
                    else:
                        break
                if attack_player_4 == 'p':
                    break
                if attack_player_1 == 'e':
                    end_1 = 0
                    break
                if attack_player_4 == 'g':
                    print(f"{player2}, you can't do this!")
                if attack_player_4 != 'm' and attack_player_4 != 'j' and attack_player_4 != 'a' and attack_player_4 != 'g' and attack_player_4 != 'e':
                    print(f"{player2}, you can't do this!")








    except ValueError:
        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
            print(f'{player1} win!')
            life = [attack_2, defence_2, ini_2]
            if gladiator1_special() == 'gnejusz' and gladiator2_special() != 'oinomaos':
                print(f"{player2}'s gladiator is injured.")
                break
            if gladiator1_special() == 'kakus' and gladiator2_special != 'oinomaos':
                print(f"{player2}'s gladiator is decapitated!")
                break
            if sum(life) <= 0:
                print(f"{player2}'s gladiator is decapitated!")
                break
            elif sum(life) ==  1:
                print(f"{player2}'s gladiator is injured.")
                break
            elif sum(life) == 2:
                print(f"{player2}'s gladiator gave up.")
                break
        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
            print(f'{player2} win!')
            life = [attack_1, defence_1, ini_1]
            if gladiator2_special() == 'gnejusz' and gladiator1_special() != 'oinomaos':
                print(f"{player1}'s gladiator is injured.")
                break
            if gladiator2_special() == 'kakus' and gladiator1_special != 'oinomaos':
                print(f"{player1}'s gladiator is decapitated!")
                break
            if sum(life) <= 0:
                print(f"{player1}'s gladiator is decapitated!")
                break
            elif sum(life) ==  1:
                print(f"{player1}'s gladiator is injured.")
                break
            elif sum(life) == 2:
                print(f"{player1}'s gladiator gave up.")
                break

