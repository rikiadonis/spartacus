import random
from initiative import get_initiative
from gladiator_statistics import gladiator1_special, gladiator2_special, gladiator1, gladiator2, gladiator1_attack, gladiator1_defence, gladiator1_ini, gladiator2_attack, gladiator2_defence, gladiator2_ini, gladiator1_weapon, gladiator2_weapon, gladiator1_armor, gladiator2_armor, gladiator1_add_gear, gladiator2_add_gear
from face_off import player2_consequences, player1_consequences
from player_hit import player1_hit, player2_hit, player1_hit_ini, player2_hit_ini
from player1 import player1_attack, player1_defence, player1_ini_attack
from player2 import player2_attack, player2_defence, player2_ini_attack
from armament import player1_get_axe, player2_get_axe, player1_get_shield, player2_get_shield, player1_get_net, player2_get_net
from gladiator_special import mukatra_ini, danel_1, danel_2, mukatra_change_attack_player1_or_defence_player2, mukatra_change_attack_player2_or_defence_player1
from javelin import player1_get_javelin, player2_get_javelin
from filemon_and_friends import get_filemon, get_ninos, get_ninos2
from your_helmet import your_helmet_1, your_helmet_2
from gannikus_hit import gannikus_hit
from pyfiglet import Figlet
attack_1 = gladiator1_attack()
defence_1 = gladiator1_defence()
ini_1 = gladiator1_ini()
attack_2 = gladiator2_attack()
defence_2 = gladiator2_defence()
ini_2 = gladiator2_ini()
d = Figlet(font='slant')
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
    javelin_hit = 0
    try:
        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
            print('Player 1 win!')
            life = [attack_2, defence_2, ini_2]
            if gladiator1_special() == 'gnejusz' and gladiator2_special() != 'oinomaos':
                print("Players 2's gladiator is injured.")
                break
            if gladiator1_special() == 'kakus' and gladiator2_special != 'oinomaos':
                print("Players 1's gladiator is decapitated.")
                break
            if sum(life) <= 0:
                print("Players 2's gladiator is decapitate!")
                break
            elif sum(life) ==  1:
                print("Players 2's gladiator is injured.")
                break
            elif sum(life) == 2:
                print("Players 2's gladiator gave up.")
                break
        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
            print('Player 2 win!')
            life = [attack_1, defence_1, ini_1]
            if gladiator2_special() == 'gnejusz' and gladiator1_special() != 'oinomaos':
                print("Players 1's gladiator is injured.")
                break
            if gladiator2_special() == 'kakus' and gladiator1_special != 'oinomaos':
                print("Players 1's gladiator is decapitated.")
                break
            if sum(life) <= 0:
                print("Players 1's gladiator is decapitated!")
                break
            elif sum(life) ==  1:
                print("Players 1's gladiator is injured.")
                break
            elif sum(life) == 2:
                print("Players 1's gladiator gave up.")
                break

        s_1, use_1, net1 = player1_get_net(net_1)
        s_2, use_2, net2 = player2_get_net(net_2)
        while True:
            if use_1 == 'y' and use_2 == 'y':
                net_1 = net1
                net_2 = net2
                while True:
                    cube_1 = [random.randint(1,6)]
                    cube_2 = [random.randint(1,6)]
                    pas = str(cube_1).strip('[').strip(']')
                    pds = str(cube_2).strip('[').strip(']')
                    print(f'Player1: {pas}')
                    print(f'Player2: {pds}')
                    if cube_1 > cube_2:
                        initiative = 1
                        break
                    elif cube_2 > cube_1:
                        initiative = 2
                        break
                break
            elif use_1 == 'y' and use_2 == 'n' or use_1 == 'y' and use_2 == None:
                net_1 = net1
                initiative = s_1
                break
            elif use_1 == 'n' and use_2 == 'y' or use_1 == None and use_2 == 'y':
                net_2 = net2
                initiative = s_2
                break
            elif use_1 == None and use_2 == None or use_1 == 'n' and use_2 == None or use_1 == None and use_2 == 'n' or use_1 == 'n' and use_2 == 'n':
                initiative, p1, p2 = get_initiative(ini_1, ini_2)
                initiative, p1, p2 = get_filemon(ini_1, ini_2, p1, p2, initiative, filemon)
                initiative, m, i = mukatra_ini(p1, p2, initiative, mukatra, ingens)
                mukatra = m
                ingens = i
                break


        if initiative == 1:
            atak_1 = 1
            atak_2 = 1
            while True:
                print(f'Player1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                attack_player_1 = input('Player 1, can you attack? ').strip(' ').lower()
                j_hit, javelin, m, i, h = player1_get_javelin(ini_1, defence_2, javelin_1, attack_player_1, mukatra, ingens, use_helmet_2)
                mukatra = m
                ingens = i
                use_helmet_2 = h
                if attack_player_1 == 'j':
                    javelin_1 = javelin
                    javelin_hit += j_hit
                else:
                    javelin_hit += 0
                if attack_player_1 == 'n' and javelin_hit > 0:
                    print(f'\nPlayer1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                    a2, d2, i2 = player2_consequences(javelin_hit, attack_2, defence_2, ini_2)
                    attack_2 = a2
                    defence_2 = d2
                    ini_2 = i2
                    javelin_hit = 0
                if attack_player_1 == 'y':
                    atak_1 -= 1
                    pa = player1_attack(attack_1)
                    pd = player2_defence(defence_2)
                    pa, pd = danel_2(defence_2, ini_2, attack_1)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print('\n')
                    print(gladiator1())
                    print('Player1 attack:')
                    print(d.renderText(pas))
                    print('Player2 defence:')
                    print(d.renderText(pds))
                    if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player1_hit(pa, pd)
                    hit = get_ninos2(pd, hit)
                    print(f'javelin hit {javelin_hit}')
                    print(type(javelin_hit))
                    hit += javelin_hit
                    for _ in range(hit):
                        print('HIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    hit, m, i, s, h = mukatra_change_attack_player1_or_defence_player2(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_1, use_helmet_2)
                    mukatra = m
                    ingens = i
                    print(f'ingens {ingens}')
                    use_sword_1 = s
                    use_helmet_2 = h
                    hit, axe = player1_get_axe(hit, axe_1)
                    hit = get_ninos(pd, hit)
                    axe_1 = axe
                    if hit > 0 and shield_2 == 1:
                        hit, shield = player2_get_shield(hit, shield_2)
                        shield_2 = shield
                    print(f'\nPlayer1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                    a2, d2, i2 = player2_consequences(hit, attack_2, defence_2, ini_2)
                    attack_2 = a2
                    defence_2 = d2
                    ini_2 = i2
                    javelin_hit = 0
                    print('\n')
                    if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                        raise ValueError
                    while True:
                        print(f'Player2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                        counter_player_2 = input('Player 2, can you counter attack? ').strip().lower()
                        j_hit, javelin, m, i, h = player2_get_javelin(ini_2, defence_1, javelin_2, counter_player_2, mukatra, ingens, use_helmet_1)
                        mukatra = m
                        ingens = i
                        use_helmet_1 = h
                        if counter_player_2 == 'j':
                            javelin_2 = javelin
                            javelin_hit += j_hit
                        else:
                            javelin_hit += 0
                        if counter_player_2 == 'n' and javelin_hit > 0:
                            print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                            a, d, i = player1_consequences(javelin_hit, attack_1, defence_1, ini_1)
                            attack_1 = a
                            defence_1 = d
                            ini_1 = i
                            javelin_hit = 0
                        if counter_player_2 == 'y':
                            atak_2 -= 1
                            print(f'Player 2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                            pa = player2_attack(attack_2)
                            pd = player1_defence(defence_1)
                            pa, pd = danel_1(defence_1, ini_1, attack_2)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print('\n')
                            print(gladiator2())
                            print('Player2 attack:')
                            print(d.renderText(f'{pas}'))
                            print('Player1 defence:')
                            print(d.renderText(f'{pds}'))
                            if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                                hit = gannikus_hit(pa, pd)
                            else:
                                hit = player2_hit(pa, pd)
                            hit = get_ninos(pd, hit)
                            hit += javelin_hit
                            for _ in range(hit):
                                print('HIT!')
                            if hit <= 0:
                                print('YOU MISSED!')
                            new_hit, m, i, s, h = mukatra_change_attack_player2_or_defence_player1(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_2, use_helmet_1)
                            mukatra = m
                            ingens = i
                            use_sword_2 = s
                            use_helmet_1 = h
                            new_hit, axe = player2_get_axe(new_hit, axe_2)
                            new_hit = get_ninos(pd, new_hit)
                            axe_2 = axe
                            if new_hit > 0 and shield_1 == 1:
                                new_hit, shield = player1_get_shield(new_hit, shield_1)
                                shield_1 = shield
                            print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                            a, d, i = player1_consequences(new_hit, attack_1, defence_1, ini_1)
                            attack_1 = a
                            defence_1 = d
                            ini_1 = i
                            javelin_hit = 0
                            break
                        elif counter_player_2 == 'n':
                            atak_2 = 0
                            break
                    break
                elif attack_player_1 == 'n':
                    break

            if atak_2 == 1:
                while True:
                    print(f'Player 2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                    attack_player_2 = input('Player 2, can you attack? ').strip(' ').lower()
                    j_hit, javelin, m, i, h = player2_get_javelin(ini_2, defence_1, javelin_2, attack_player_2, mukatra, ingens, use_helmet_1)
                    mukatra = m
                    ingens = i
                    use_helmet_1 = h
                    if attack_player_2 == 'j':
                        javelin_2 = javelin
                        javelin_hit += j_hit
                    else:
                        javelin_hit += 0
                    if attack_player_2 == 'n' and javelin_hit > 0:
                        print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                        a, d, i = player1_consequences(javelin_hit, attack_1, defence_1, ini_1)
                        attack_1 = a
                        defence_1 = d
                        ini_1 = i
                        javelin_hit = 0
                    if attack_player_2 == 'y':
                        atak_2 -= 1
                        pa = player2_attack(attack_2)
                        pd = player1_defence(defence_1)
                        pa, pd = danel_1(defence_1, ini_1, attack_2)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print('\n')
                        print(gladiator2())
                        print('Player2 attack:')
                        print(d.renderText(f'{pas}'))
                        print('Player1 defence:')
                        print(d.renderText(f'{pds}'))
                        if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                            hit = gannikus_hit(pa, pd)
                        else:
                            hit = player2_hit(pa, pd)
                        hit = get_ninos(pd, hit)
                        hit += javelin_hit
                        for _ in range(hit):
                            print('HIT!')
                        if hit <= 0:
                            print('YOU MISSED!')
                        new_hit, m, i, s, h = mukatra_change_attack_player2_or_defence_player1(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_2, use_helmet_1)
                        mukatra = m
                        ingens = i
                        use_sword_2 = s
                        use_helmet_1 = h
                        new_hit, axe = player2_get_axe(new_hit, axe_2)
                        new_hit = get_ninos(pd, new_hit)
                        axe_2 = axe
                        if new_hit > 0 and shield_1 == 1:
                            new_hit, shield = player1_get_shield(new_hit, shield_1)
                            shield_1 = shield
                        print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                        a, d, i = player1_consequences(new_hit, attack_1, defence_1, ini_1)
                        attack_1 = a
                        defence_1 = d
                        ini_1 = i
                        javelin_hit = 0
                        print('\n')
                        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                            raise ValueError
                        while True:
                            print(f'Player 1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                            counter_player_1 = input('Player 1, can you counter attack? ').strip().lower()
                            j_hit, javelin, m, i, h = player1_get_javelin(ini_1, defence_2, javelin_1, counter_player_1, mukatra, ingens, use_helmet_2)
                            mukatra = m
                            ingens = i
                            use_helmet_2 = h
                            if counter_player_1 == 'j':
                                javelin_1 = javelin
                                javelin_hit += j_hit
                            else:
                                javelin_hit += 0
                            if counter_player_1 == 'n' and javelin_hit > 0:
                                print(f'\nPlayer1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                                a2, d2, i2 = player2_consequences(javelin_hit, attack_2, defence_2, ini_2)
                                attack_2 = a2
                                defence_2 = d2
                                ini_2 = i2
                                javelin_hit = 0
                            if counter_player_1 == 'y':
                                atak_1 -= 1
                                print(f'Player 1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                                pa = player1_attack(attack_1)
                                pd = player2_defence(defence_2)
                                pa, pd = danel_2(defence_2, ini_2, attack_1)
                                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                                print('\n')
                                print(gladiator1())
                                print('Player1 attack:')
                                print(d.renderText(f'{pas}'))
                                print('Player2 defence:')
                                print(d.renderText(f'{pds}'))
                                if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                                    hit = gannikus_hit(pa, pd)
                                else:
                                    hit = player1_hit(pa, pd)
                                hit = get_ninos2(pd, hit)
                                hit += javelin_hit
                                for _ in range(hit):
                                    print('HIT!')
                                if hit <= 0:
                                    print('YOU MISSED!')
                                new_hit, m, i, s, h = mukatra_change_attack_player1_or_defence_player2(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_1, use_helmet_2)
                                mukatra = m
                                ingens = i
                                use_sword_1 = s
                                use_helmet_2 = h
                                new_hit, axe = player1_get_axe(new_hit, axe_1)
                                new_hit = get_ninos(pd, new_hit)
                                axe_1 = axe
                                if new_hit > 0 and shield_2 == 1:
                                    new_hit, shield = player2_get_shield(new_hit, shield_2)
                                    shield_2 = shield
                                print(f'\nPlayer1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                                a2, d2, i2 = player2_consequences(new_hit, attack_2, defence_2, ini_2)
                                attack_2 = a2
                                defence_2 = d2
                                ini_2 = i2
                                javelin_hit = 0
                                break
                            elif counter_player_1 == 'n':
                                atak_1 = 0
                                break
                        break
                    elif attack_player_2 == 'n':
                        break
        if initiative == 2:
            atak_1 = 1
            atak_2 = 1
            while True:
                print(f'Player2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                attack_player_2 = input('Player 2, can you attack? ').strip(' ').lower()
                j_hit, javelin, m, i, h = player2_get_javelin(ini_2, defence_1, javelin_2, attack_player_2, mukatra, ingens, use_helmet_1)
                mukatra = m
                ingens = i
                use_helmet_1 = h
                if attack_player_2 == 'j':
                    javelin_2 = javelin
                    javelin_hit += j_hit
                else:
                    javelin_hit += 0
                print(f'j hit: {javelin_hit}')
                if attack_player_2 == 'n' and javelin_hit > 0:
                    print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                    a2, d2, i2 = player1_consequences(javelin_hit, attack_1, defence_1, ini_1)
                    attack_1 = a2
                    defence_1 = d2
                    ini_1 = i2
                    javelin_hit = 0
                if attack_player_2 == 'y':
                    atak_2 -= 1
                    pa = player2_attack(attack_2)
                    pd = player1_defence(defence_1)
                    pa, pd = danel_1(defence_1, ini_1, attack_2)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print('\n')
                    print(gladiator2())
                    print('Player2 attack:')
                    print(d.renderText(f'{pas}'))
                    print('Player1 defence:')
                    print(d.renderText(f'{pds}'))
                    if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player2_hit(pa, pd)
                    hit = get_ninos(pd, hit)
                    hit += javelin_hit
                    for _ in range(hit):
                        print('HIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    new_hit, m, i, s, h = mukatra_change_attack_player2_or_defence_player1(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_2, use_helmet_1)
                    mukatra = m
                    ingens = i
                    use_sword_2 = s
                    use_helmet_1 = h
                    print(f'hit in plan: {new_hit}')
                    new_hit, axe = player2_get_axe(new_hit, axe_2)
                    axe_2 = axe
                    new_hit = get_ninos(pd, new_hit)
                    if new_hit > 0 and shield_1 == 1:
                        new_hit, shield = player1_get_shield(new_hit, shield_1)
                        shield_1 = shield
                    print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                    a2, d2, i2 = player1_consequences(new_hit, attack_1, defence_1, ini_1)
                    attack_1 = a2
                    defence_1 = d2
                    ini_1 = i2
                    javelin_hit = 0
                    print('\n')
                    if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                        raise ValueError
                    while True:
                        print(f'Player1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                        counter_player_1 = input('Player1, can you counter attack? ').strip().lower()
                        j_hit, javelin, m, i, h = player1_get_javelin(ini_1, defence_2, javelin_1, counter_player_1, mukatra, ingens, use_helmet_2)
                        mukatra = m
                        ingens = i
                        use_helmet_2 = h
                        if counter_player_1 == 'j':
                            javelin_1 = javelin
                            javelin_hit += j_hit
                        else:
                            javelin_hit += 0
                        if counter_player_1 == 'n' and javelin_hit > 0:
                            print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                            a, d, i = player2_consequences(javelin_hit, attack_2, defence_2, ini_2)
                            attack_2 = a
                            defence_2 = d
                            ini_2 = i
                            javelin_hit = 0
                        if counter_player_1 == 'y':
                            atak_1 -= 1
                            print(f'Player1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                            pa = player1_attack(attack_1)
                            pd = player2_defence(defence_2)
                            pa, pd = danel_2(defence_2, ini_2, attack_1)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print('\n')
                            print(gladiator1())
                            print('Player1 attack:')
                            print(d.renderText(f'{pas}'))
                            print('Player2 defence:')
                            print(d.renderText(f'{pds}'))
                            if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                                hit = gannikus_hit(pa, pd)
                            else:
                                hit = player1_hit(pa, pd)
                            hit = get_ninos2(pd, hit)
                            hit += javelin_hit
                            for _ in range(hit):
                                print('HIT!')
                            if hit <= 0:
                                print('YOU MISSED!')
                            new_hit, m, i, h, s = mukatra_change_attack_player1_or_defence_player2(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_1, use_helmet_2)
                            mukatra = m
                            ingens = i
                            use_sword_1 = s
                            use_helmet_2 = h
                            new_hit, axe = player1_get_axe(new_hit, axe_1)
                            axe_1 = axe
                            new_hit = get_ninos(pd, new_hit)
                            if new_hit > 0 and shield_2 == 1:
                                new_hit, shield = player2_get_shield(new_hit, shield_2)
                                shield_2 = shield
                            print(f'\nPlayer1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                            a, d, i = player2_consequences(new_hit, attack_2, defence_2, ini_2)
                            attack_2 = a
                            defence_2 = d
                            ini_2 = i
                            javelin_hit = 0
                            break
                        elif counter_player_1 == 'n':
                            atak_1 = 0
                            break
                    break
                elif attack_player_2 == 'n':
                    break
            if atak_1 == 1:
                while True:
                    print(f'Player1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                    attack_player_1 = input('Player1, can you attack? ').strip(' ').lower()
                    j_hit, javelin, m, i, h = player1_get_javelin(ini_1, defence_2, javelin_1, attack_player_1, mukatra, ingens, use_helmet_2)
                    mukatra = m
                    ingens = i
                    use_helmet_2 = h
                    if attack_player_1 == 'j':
                        javelin_1 = javelin
                        javelin_hit += j_hit
                    else:
                        javelin_hit += 0
                    if attack_player_1 == 'n' and javelin_hit > 0:
                        print(f'\nPlayer1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                        a, d, i = player2_consequences(javelin_hit, attack_2, defence_2, ini_2)
                        attack_2 = a
                        defence_2 = d
                        ini_2 = i
                        javelin_hit = 0
                    if attack_player_1 == 'y':
                        atak_1 -= 1
                        pa = player1_attack(attack_1)
                        pd = player2_defence(defence_2)
                        pa, pd = danel_2(defence_2, ini_2, attack_1)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print('\n')
                        print(gladiator1())
                        print('Player1 attack:')
                        print(d.renderText(f'{pas}'))
                        print('Player2 defence:')
                        print(d.renderText(f'{pds}'))
                        if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                            hit = gannikus_hit(pa, pd)
                        else:
                            hit = player1_hit(pa, pd)
                        hit = get_ninos2(pd, hit)
                        hit += javelin_hit
                        for _ in range(hit):
                            print('HIT!')
                        if hit <= 0:
                            print('YOU MISSED!')
                        new_hit, m, i = mukatra_change_attack_player1_or_defence_player2(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_1, use_helmet_2)
                        mukatra = m
                        ingens = i
                        use_sword_1 = s
                        use_helmet_2 = h
                        new_hit, axe = player1_get_axe(new_hit, axe_1)
                        axe_1 = axe
                        new_hit = get_ninos(pd, new_hit)
                        if new_hit > 0 and shield_2 == 1:
                            new_hit, shield = player2_get_shield(new_hit, shield_2)
                            shield_2 = shield
                        print(f'\nPlayer1:\nAttack: {attack_1}, Defence: {defence_1}, Initiative: {ini_1}')
                        a, d, i = player2_consequences(new_hit, attack_2, defence_2, ini_2)
                        attack_2 = a
                        defence_2 = d
                        ini_2 = i
                        javelin_hit = 0
                        print('\n')
                        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                            raise ValueError
                        while True:
                            print(f'Player2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                            counter_player_2 = input('Player2, can you counter attack? ').strip().lower()
                            j_hit, javelin, m, i, h = player2_get_javelin(ini_2, defence_1, javelin_2, counter_player_2, mukatra, ingens, use_helmet_1)
                            mukatra = m
                            ingens = i
                            use_helmet_1 = h
                            if counter_player_2 == 'j':
                                javelin_2 = javelin
                                javelin_hit += j_hit
                            else:
                                javelin_hit += 0
                            if counter_player_2 == 'n' and javelin_hit > 0:
                                print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                                a2, d2, i2 = player1_consequences(javelin_hit, attack_1, defence_1, ini_1)
                                attack_1 = a2
                                defence_1 = d2
                                ini_1 = i2
                                javelin_hit = 0
                            if counter_player_2 == 'y':
                                atak_2 -= 1
                                print(f'Player2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                                pa = player2_attack(attack_2)
                                pd = player1_defence(defence_1)
                                pa, pd = danel_1(defence_1, ini_1, attack_2)
                                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                                print('\n')
                                print(gladiator2())
                                print('Player2 attack:')
                                print(d.renderText(f'{pas}'))
                                print('Player1 defence:')
                                print(d.renderText(f'{pds}'))
                                if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                                    hit = gannikus_hit(pa, pd)
                                else:
                                    hit = player2_hit(pa, pd)
                                hit = get_ninos(pd, hit)
                                hit += javelin
                                for _ in range(hit):
                                    print('HIT!')
                                if hit <= 0:
                                    print('YOU MISSED!')
                                new_hit, m, i, s, h = mukatra_change_attack_player2_or_defence_player1(pa, pd, hit, javelin_hit, mukatra, ingens, use_sword_2, use_helmet_1)
                                mukatra = m
                                ingens = i
                                use_sword_2 = s
                                use_helmet_1 = h
                                new_hit, axe = player2_get_axe(new_hit, axe_2)
                                axe_2 = axe
                                new_hit = get_ninos(pd, new_hit)
                                if new_hit > 0 and shield_1 == 1:
                                    new_hit, shield = player2_get_shield(new_hit, shield_1)
                                    shield_1 = shield
                                print(f'\nPlayer2:\nAttack: {attack_2}, Defence: {defence_2}, Initiative: {ini_2}')
                                a2, d2, i2 = player1_consequences(new_hit, attack_1, defence_1, ini_1)
                                attack_1 = a2
                                defence_1 = d2
                                ini_1 = i2
                                javelin_hit = 0
                                break
                            elif counter_player_2 == 'n':
                                atak_2 = 0
                                break
                        break
                    elif attack_player_1 == 'n':
                        break
    except ValueError:
        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
             print(f'{gladiator1()}\nPlayer 1 win! by error')
             life = [attack_2, defence_2, ini_2]
             if gladiator1_special() == 'gnejusz' and gladiator2_special() != 'oinomaos':
                print("Players 2's gladiator is injured.")
                break
             if gladiator1_special() == 'kakus' and gladiator2_special() != 'oinomaos':
                print("Players 2's gladiator is decapitated.")
                break
             if sum(life) <= 0:
                 print("Players 2's gladiator is decapitated!")
                 break
             elif sum(life) ==  1:
                 print("Players 2's gladiator is injured.")
                 break
             elif sum(life) == 2:
                 print("Players 2's gladiator gave up.")
                 break
        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
            print(f'{gladiator2()}\nPlayer 2 win by error!')
            life = [attack_1, defence_1, ini_1]
            if gladiator2_special() == 'gnejusz' and gladiator1_special != 'oinomaos':
                print("Players 1's gladiator is injured.")
                break
            if gladiator2_special() == 'kakus' and gladiator1_special != 'oinomaos':
                print("Players 1's gladiator is decapitated.")
                break
            if sum(life) <= 0:
                print("Players 1's gladiator is decapitate!")
                break
            elif sum(life) ==  1:
                print("Players 1's gladiator is injured.")
                break
            elif sum(life) == 2:
                print("Players 1's gladiator gave up.")
                break

