import random
from initiative import get_initiative
from gladiator_statistics import gladiator1_special, gladiator2_special, gladiator1, gladiator2, gladiator1_attack, gladiator1_defence, gladiator1_ini, gladiator2_attack, gladiator2_defence, gladiator2_ini, gladiator1_weapon, gladiator2_weapon, gladiator1_armor, gladiator2_armor, gladiator1_add_gear, gladiator2_add_gear
from face_off import player2_consequences, player1_consequences
from player_hit import player1_hit, player2_hit
from player1 import player1_attack, player1_defence
from player2 import player2_attack, player2_defence
from armament import player1_get_axe, player2_get_axe, player1_get_shield, player2_get_shield, player1_get_net, player2_get_net
from gladiator_special import mukatra_ini, danel_1, danel_2
from javelin import player1_get_javelin, player2_get_javelin
from filemon_and_friends import get_filemon
from ninos_syndrom import get_ninos, get_ninos2, get_alard, get_alard2, get_valerius_1, get_valerius_2
from gannikus_hit import gannikus_hit
from gladiator_syndrom import part1, part2
from pyfiglet import Figlet
attack_1 = gladiator1_attack()
defence_1 = gladiator1_defence()
ini_1 = gladiator1_ini()
attack_2 = gladiator2_attack()
defence_2 = gladiator2_defence()
ini_2 = gladiator2_ini()
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
    acube_1 = attack_1 * '🟥 '
    decube_1 = defence_1 * '🟫 '
    incube_1 = ini_1 * '🟦 '
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
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
                    print(f'Player1: {pas} {incube_1}')
                    print(f'Player2: {pds} {incube_2}')
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
                print(f'Player1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                attack_player_1 = input('Player1, can you attack? ').strip(' ').lower()
                j, attack_player_1, m, i, h, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1 = player1_get_javelin(ini_1, javelin_1, attack_player_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player2)
                javelin_1 = j
                use_helmet_2 = h
                mukatra = m
                ingens = i
                if attack_player_1 == 'y':
                    atak_1 -= 1
                    pa = player1_attack(attack_1)
                    pd = player2_defence(defence_2)
                    pa, pd = danel_2(defence_2, ini_2, attack_1)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'\n{gladiator1()} Strikes!\nPlayer1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'Player2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                    print(d.renderText(pds))
                    if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player1_hit(pa, pd)
                    hit = get_ninos2(pd, hit)
                    if hit > 0:
                        print(hit * '🗡️  ')
                    if hit <= 0:
                        print(defence_2 * '🛡️  ')
                    hit,m,i,s,h = part1(pa, pd, hit, mukatra, ingens, use_sword_1, use_helmet_2, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
                    ingens = i
                    mukatra = m
                    use_sword_1 = s
                    use_helmet_2 = h
                    hit, axe = player1_get_axe(hit, axe_1)
                    hit = get_ninos(pd, hit)
                    axe_1 = axe
                    if hit > 0 and shield_2 == 1:
                        hit, shield = player2_get_shield(hit, shield_2)
                        shield_2 = shield
                    get_valerius_1(hit)
                    print(f'Player1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                    a2, d2, i2 = player2_consequences(hit, attack_2, defence_2, ini_2, player2)
                    attack_2 = a2
                    defence_2 = d2
                    ini_2 = i2
                    acube_2 = attack_2 * '🟥 '
                    decube_2 = defence_2 * '🟫 '
                    incube_2 = ini_2 * '🟦 '
                    attack_1, defence_1, ini_1 = get_alard2(pd, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2)
                    print('')
                    if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                        raise ValueError
                    while True:
                        print(f'Player2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                        counter_player_2 = input('Player 2, can you counter attack? ').strip().lower()
                        javelin_2, counter_player_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2 = player2_get_javelin(ini_2, javelin_2, counter_player_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1)
                        if counter_player_2 == 'y':
                            atak_2 -= 1
                            print(f'Player 2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                            pa = player2_attack(attack_2)
                            pd = player1_defence(defence_1)
                            pa, pd = danel_1(defence_1, ini_1, attack_2)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print(f'\n{gladiator2()} Strikes!\nPlayer2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                            print(d.renderText(pas))
                            print(f'Player1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
                            print(d.renderText(pds))
                            if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                                hit = gannikus_hit(pa, pd)
                            else:
                                hit = player2_hit(pa, pd)
                            hit = get_ninos(pd, hit)
                            if hit > 0:
                                print(hit * '🗡️  ')
                            if hit <= 0:
                                print('🛡️')
                            new_hit, m, i, s, h = part2(pa, pd, hit, mukatra, ingens, use_sword_2, use_helmet_1, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
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
                            get_valerius_2(new_hit)
                            print(f'\nPlayer2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                            a, d, i = player1_consequences(new_hit, attack_1, defence_1, ini_1, player1)
                            attack_1 = a
                            defence_1 = d
                            ini_1 = i
                            acube_1 = attack_1 * '🟥 '
                            decube_1 = defence_1 * '🟫 '
                            incube_1 = ini_1 * '🟦 '
                            attack_2, defence_2, ini_2 = get_alard(pd, attack_2, defence_2, ini_2, acube_1, decube_1, incube_1)
                            break
                        elif counter_player_2 == 'n':
                            atak_2 = 0
                            break
                    break
                elif attack_player_1 == 'n':
                    break

            if atak_2 == 1:
                d = Figlet(font='slant')
                while True:
                    print(f'Player 2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                    attack_player_2 = input('Player 2, can you attack? ').strip(' ').lower()
                    javelin_2, attack_player_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2 = player2_get_javelin(ini_2, javelin_2, attack_player_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1)
                    if attack_player_2 == 'y':
                        atak_2 -= 1
                        pa = player2_attack(attack_2)
                        pd = player1_defence(defence_1)
                        pa, pd = danel_1(defence_1, ini_1, attack_2)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator2()} Strikes!\nPlayer2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                        print(d.renderText(pas))
                        print(f'Player1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
                        print(d.renderText(pds))
                        if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                            hit = gannikus_hit(pa, pd)
                        else:
                            hit = player2_hit(pa, pd)
                        hit = get_ninos(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print('🛡️')
                        new_hit, m, i, s, h = part2(pa, pd, hit, mukatra, ingens, use_sword_2, use_helmet_1, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
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
                        get_valerius_2(new_hit)
                        print(f'\nPlayer2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                        a, d, i = player1_consequences(new_hit, attack_1, defence_1, ini_1, player1)
                        attack_1 = a
                        defence_1 = d
                        ini_1 = i
                        acube_1 = attack_1 * '🟥 '
                        decube_1 = defence_1 * '🟫 '
                        incube_1 = ini_1 * '🟦 '
                        attack_1, defence_1, ini_1 = get_alard2(pd, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2)
                        print('')
                        if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                            raise ValueError
                        while True:
                            d = Figlet(font='slant')
                            print(f'Player 1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                            counter_player_1 = input('Player 1, can you counter attack? ').strip().lower()
                            javelin_1, counter_player_1, mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1 = player1_get_javelin(ini_1, javelin_1, counter_player_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player2)
                            if counter_player_1 == 'y':
                                atak_1 -= 1
                                print(f'Player 1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                                pa = player1_attack(attack_1)
                                pd = player2_defence(defence_2)
                                pa, pd = danel_2(defence_2, ini_2, attack_1)
                                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                                print(f'\n{gladiator1()} Strikes!\nPlayer1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                                print(d.renderText(pas))
                                print(f'Player2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                                print(d.renderText(pds))
                                if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                                    hit = gannikus_hit(pa, pd)
                                else:
                                    hit = player1_hit(pa, pd)
                                hit = get_ninos2(pd, hit)
                                if hit > 0:
                                    print(hit * '🗡️  ')
                                if hit <= 0:
                                    print('🛡️')
                                new_hit, m, i, s, h = part1(pa, pd, hit, mukatra, ingens, use_sword_1, use_helmet_2, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
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
                                get_valerius_1(new_hit)
                                print(f'\nPlayer1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                                a2, d2, i2 = player2_consequences(new_hit, attack_2, defence_2, ini_2, player2)
                                attack_2 = a2
                                defence_2 = d2
                                ini_2 = i2
                                acube_2 = attack_2 * '🟥 '
                                decube_2 = defence_2 * '🟫 '
                                incube_2 = ini_2 * '🟦 '
                                attack_1, defence_1, ini_1 = get_alard2(pd, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2)
                                break
                            elif counter_player_1 == 'n':
                                atak_1 = 0
                                break
                        break
                    elif attack_player_2 == 'n':
                        break
        if initiative == 2:
            d = Figlet(font='slant')
            atak_1 = 1
            atak_2 = 1
            while True:
                print(f'Player2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                attack_player_2 = input('Player 2, can you attack? ').strip(' ').lower()
                javelin_2, attack_player_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2 = player2_get_javelin(ini_2, javelin_2, attack_player_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1)
                if attack_player_2 == 'y':
                    atak_2 -= 1
                    pa = player2_attack(attack_2)
                    pd = player1_defence(defence_1)
                    pa, pd = danel_1(defence_1, ini_1, attack_2)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'\n{gladiator2()} Strikes!\nPlayer2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'Player1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
                    print(d.renderText(pds))
                    if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player2_hit(pa, pd)
                    hit = get_ninos(pd, hit)
                    if hit > 0:
                        print(hit * '🗡️  ')
                    if hit <= 0:
                        print('🛡️')
                    new_hit, m, i, s, h = part2(pa, pd, hit, mukatra, ingens, use_sword_2, use_helmet_1, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
                    mukatra = m
                    ingens = i
                    use_sword_2 = s
                    use_helmet_1 = h
                    new_hit, axe = player2_get_axe(new_hit, axe_2)
                    axe_2 = axe
                    new_hit = get_ninos(pd, new_hit)
                    if new_hit > 0 and shield_1 == 1:
                        new_hit, shield = player1_get_shield(new_hit, shield_1)
                        shield_1 = shield
                    get_valerius_2(new_hit)
                    print(f'\nPlayer2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                    a2, d2, i2 = player1_consequences(new_hit, attack_1, defence_1, ini_1, player1)
                    attack_1 = a2
                    defence_1 = d2
                    ini_1 = i2
                    acube_1 = attack_1 * '🟥 '
                    decube_1 = defence_1 * '🟫 '
                    incube_1 = ini_1 * '🟦 '
                    attack_2, defence_2, ini_2 = get_alard(pd, attack_2, defence_2, ini_2, acube_1, decube_1, incube_1)
                    print('')
                    if attack_1 <= 0 or defence_1 <= 0 or ini_1 <= 0:
                        raise ValueError
                    while True:
                        print(f'Player1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                        counter_player_1 = input('Player1, can you counter attack? ').strip().lower()
                        javelin_1, counter_player_1, mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1 = player1_get_javelin(ini_1, javelin_1, counter_player_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player2)
                        if counter_player_1 == 'y':
                            atak_1 -= 1
                            print(f'Player1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                            pa = player1_attack(attack_1)
                            pd = player2_defence(defence_2)
                            pa, pd = danel_2(defence_2, ini_2, attack_1)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print(f'\n{gladiator1()} Strikes!\nPlayer1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                            print(d.renderText(pas))
                            print(f'Player2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                            print(d.renderText(pds))
                            if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                                hit = gannikus_hit(pa, pd)
                            else:
                                hit = player1_hit(pa, pd)
                            hit = get_ninos2(pd, hit)
                            if hit > 0:
                                print(hit * '🗡️  ')
                            if hit <= 0:
                                print('🛡️')
                            new_hit, m, i, h, s = part1(pa, pd, hit, mukatra, ingens, use_sword_1, use_helmet_2, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
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
                            get_valerius_1(new_hit)
                            print(f'\nPlayer1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                            a, d, i = player2_consequences(new_hit, attack_2, defence_2, ini_2, player2)
                            attack_2 = a
                            defence_2 = d
                            ini_2 = i
                            acube_2 = attack_2 * '🟥 '
                            decube_2 = defence_2 * '🟫 '
                            incube_2 = ini_2 * '🟦 '
                            attack_1, defence_1, ini_1 = get_alard2(pd, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2)
                            break
                        elif counter_player_1 == 'n':
                            atak_1 = 0
                            break
                    break
                elif attack_player_2 == 'n':
                    break
            if atak_1 == 1:
                d = Figlet(font='slant')
                while True:
                    print(f'Player1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                    attack_player_1 = input('Player1, can you attack? ').strip(' ').lower()
                    javelin_1, attack_player_1, mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1 = player1_get_javelin(ini_1, javelin_1, attack_player_1, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player2)
                    if attack_player_1 == 'y':
                        atak_1 -= 1
                        pa = player1_attack(attack_1)
                        pd = player2_defence(defence_2)
                        pa, pd = danel_2(defence_2, ini_2, attack_1)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator1()} Strikes!\nPlayer1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                        print(d.renderText(pas))
                        print(f'Player2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                        print(d.renderText(pds))
                        if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                            hit = gannikus_hit(pa, pd)
                        else:
                            hit = player1_hit(pa, pd)
                        hit = get_ninos2(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print('🛡️')
                        new_hit, m, i = part1(pa, pd, hit, mukatra, ingens, use_sword_1, use_helmet_2, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
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
                        get_valerius_1(new_hit)
                        print(f'\nPlayer1:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                        a, d, i = player2_consequences(new_hit, attack_2, defence_2, ini_2, player2)
                        attack_2 = a
                        defence_2 = d
                        ini_2 = i
                        acube_2 = attack_2 * '🟥 '
                        decube_2 = defence_2 * '🟫 '
                        incube_2 = ini_2 * '🟦 '
                        attack_1, defence_1, ini_1 = get_alard2(pd, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2)
                        print('')
                        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
                            raise ValueError
                        while True:
                            print(f'Player2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                            counter_player_2 = input('Player2, can you counter attack? ').strip().lower()
                            javelin_2, counter_player_2, mukatra, ingens, use_helmet_1, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2 = player2_get_javelin(ini_2, javelin_2, counter_player_2, mukatra, ingens, use_helmet_1, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1)
                            if counter_player_2 == 'y':
                                atak_2 -= 1
                                print(f'Player2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                                pa = player2_attack(attack_2)
                                pd = player1_defence(defence_1)
                                pa, pd = danel_1(defence_1, ini_1, attack_2)
                                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                                print(f'\n{gladiator2()} Strikes!\nPlayer2:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                                print(d.renderText(pas))
                                print(f'Player1:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
                                print(d.renderText(pds))
                                if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                                    hit = gannikus_hit(pa, pd)
                                else:
                                    hit = player2_hit(pa, pd)
                                hit = get_ninos(pd, hit)
                                if hit > 0:
                                    print(hit * '🗡️  ')
                                if hit <= 0:
                                    print('🛡️')
                                new_hit, m, i, s, h = part2(pa, pd, hit, mukatra, ingens, use_sword_2, use_helmet_1, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2)
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
                                get_valerius_2(new_hit)
                                print(f'\nPlayer2:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                                a2, d2, i2 = player1_consequences(new_hit, attack_1, defence_1, ini_1, player1)
                                attack_1 = a2
                                defence_1 = d2
                                ini_1 = i2
                                acube_1 = attack_1 * '🟥 '
                                decube_1 = defence_1 * '🟫 '
                                incube_1 = ini_1 * '🟦 '
                                attack_2, defence_2, ini_2 = get_alard(pd, attack_2, defence_2, ini_2, acube_1, decube_1, incube_1)
                                break
                            elif counter_player_2 == 'n':
                                atak_2 = 0
                                break
                        break
                    elif attack_player_1 == 'n':
                        break
    except ValueError:
        if attack_2 <= 0 or defence_2 <= 0 or ini_2 <= 0:
             print(f'{gladiator1()}\nPlayer 1 win!')
             life = [attack_2, defence_2, ini_2]
             if gladiator1_special() == 'gnejusz' and gladiator2_special() != 'oinomaos':
                print("Players 2's gladiator is injured.")
                break
             if gladiator1_special() == 'kakus' and gladiator2_special() != 'oinomaos':
                print("Players 2's gladiator is decapitated!")
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
            print(f'{gladiator2()}\nPlayer 2 win!')
            life = [attack_1, defence_1, ini_1]
            if gladiator2_special() == 'gnejusz' and gladiator1_special != 'oinomaos':
                print("Players 1's gladiator is injured.")
                break
            if gladiator2_special() == 'kakus' and gladiator1_special != 'oinomaos':
                print("Players 1's gladiator is decapitated!")
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

