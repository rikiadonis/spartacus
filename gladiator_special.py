import random
from gladiator_statistics import gladiator1, gladiator2, gladiator1_special, gladiator2_special, gladiator1_armor, gladiator2_armor, gladiator1_weapon, gladiator2_weapon
from player1 import player1_attack
from player_hit import player1_hit, player2_hit, player1_hit_ini, player2_hit_ini
from gladiator_syndrom import part1, part2
from ninos_syndrom import get_ninos, get_ninos2
from pyfiglet import Figlet
d = Figlet(font='slant')

def danel_1(defence, ini, attack):
    if gladiator1_special() == 'danel' and gladiator2_special() != 'oinomaos':
        if defence >= ini:
            pa = player1_attack(attack)
            pd = player1_attack(defence)
            return pa, pd
        else:
            pa = player1_attack(attack)
            pd = player1_attack(ini)
            return pa, pd
    else:
        pa = player1_attack(attack)
        pd = player1_attack(defence)
        return pa, pd


def danel_2(defence, ini, attack):
    if gladiator2_special() == 'danel' and gladiator1_special() != 'oinomaos':
        if defence >= ini:
            pa = player1_attack(attack)
            pd = player1_attack(defence)
            return pa, pd
        else:
            pa = player1_attack(attack)
            pd = player1_attack(ini)
            return pa, pd
    else:
        pa = player1_attack(attack)
        pd = player1_attack(defence)
        return pa, pd

def ingens_2_change_defence_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'ingens' and ingens == 1 and gladiator1_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pd[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pd) <= 5 and len(pd) >= 1:
                            pd[0] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pd) >= 2:
                            pd[1] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '3' and len(pd) <= 5 and len(pd) >= 3:
                            pd[2] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pd) >= 4:
                            pd[3] = random.randint(1,6)
                            pd.sort(reverse=True)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator1()}\n{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nJAVELIN ATTACK:')
                        print(d.renderText(pas))
                        print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                        print(d.renderText(pds))
                        hit = player2_hit_ini(pa, pd)
                        hit = get_ninos(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print(len(pd) * '🛡️  ')
                        counter = 'yes'
                        return hit, ingens, counter
            elif a == 'n':
                hit = player2_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        return hit, ingens, counter

def ingens_1_change_attack_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'ingens' and ingens == 1 and gladiator2_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pa) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pa) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator2()}\n{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nJAVELIN ATTACK:')
                        print(d.renderText(pas))
                        print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
                        print(d.renderText(pds))
                        hit = player2_hit_ini(pa, pd)
                        hit = get_ninos(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print(len(pd) * '🛡️  ')
                        return hit, ingens, counter
            elif a == 'n':
                hit = player2_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        hit = player2_hit_ini(pa,pd)
        return hit, ingens, counter



def ingens_1_change_defence_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'ingens' and ingens == 1 and gladiator2_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pd[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pd) <= 5 and len(pd) >= 1:
                            pd[0] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pd) >= 2:
                            pd[1] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '3' and len(pd) <= 5 and len(pd) >= 3:
                            pd[2] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pd) >= 4:
                            pd[3] = random.randint(1,6)
                            pd.sort(reverse=True)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator1()}\n{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nJAVELIN ATTACK:')
                        print(d.renderText(pas))
                        print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                        print(d.renderText(pds))
                        hit = player1_hit_ini(pa, pd)
                        hit = get_ninos2(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print(len(pd) * '🛡️  ')
                        counter = 'yes'
                        return hit, ingens, counter
            elif a == 'n':
                hit = player1_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        return hit, ingens, counter

def ingens_2_change_attack_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'ingens' and ingens == 1 and gladiator1_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                if gladiator2_special() == 'mukatra':
                    mukatra = 0
                elif gladiator2_special() == 'ingens':
                    ingens = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pa) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pa) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator1()}\n{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nJAVELIN ATTACK:')
                        print(d.renderText(pas))
                        print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                        print(d.renderText(pds))
                        hit = player1_hit_ini(pa, pd)
                        hit = get_ninos2(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print(len(pd) * '🛡️  ')
                        counter = 'yes'
                        return hit, ingens, counter
            elif a == 'n':
                hit = player1_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        hit = player1_hit_ini(pa,pd)
        return hit, ingens, counter




def mukatra_2_change_defence_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'mukatra' and ingens == 1 and gladiator1_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pd[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pd) <= 5 and len(pd) >= 1:
                            pd[0] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pd) >= 2:
                            pd[1] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '3' and len(pd) <= 5 and len(pd) >= 3:
                            pd[2] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pd) >= 4:
                            pd[3] = random.randint(1,6)
                            pd.sort(reverse=True)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator2()}\n{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nJAVELIN ATTACK:')
                        print(d.renderText(pas))
                        print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
                        print(d.renderText(pds))
                        hit = player2_hit_ini(pa, pd)
                        hit = get_ninos(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print(len(pd) * '🛡️  ')
                        counter = 'yes'
                        return hit, ingens, counter
            elif a == 'n':
                hit = player2_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        return hit, ingens, counter
def mukatra_1_change_attack_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'mukatra' and ingens == 1 and gladiator2_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pa) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pa) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator2()}\n{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nJAVELIN ATTACK:')
                        print(d.renderText(pas))
                        print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
                        print(d.renderText(pds))
                        hit = player2_hit_ini(pa, pd)
                        hit = get_ninos(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print(len(pd) * '🛡️  ')
                        return hit, ingens, counter
            elif a == 'n':
                hit = player2_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        hit = player2_hit_ini(pa,pd)
        return hit, ingens, counter

def mukatra_1_change_defence_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'mukatra' and ingens == 1 and gladiator2_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pd[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pd) <= 5 and len(pd) >= 1:
                            pd[0] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pd) >= 2:
                            pd[1] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '3' and len(pd) <= 5 and len(pd) >= 3:
                            pd[2] = random.randint(1,6)
                            pd.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pd) >= 4:
                            pd[3] = random.randint(1,6)
                            pd.sort(reverse=True)
                        pas = str(pa).strip('[').strip(']').replace(',', '  ')
                        pds = str(pd).strip('[').strip(']').replace(',', '  ')
                        print(f'\n{gladiator1()}\n{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nJAVELIN ATTACK:')
                        print(d.renderText(pas))
                        print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                        print(d.renderText(pds))
                        hit = player1_hit_ini(pa, pd)
                        hit = get_ninos2(pd, hit)
                        if hit > 0:
                            print(hit * '🗡️  ')
                        if hit <= 0:
                            print(len(pd) * '🛡️  ')
                        counter = 'yes'
                        return hit, ingens, counter
            elif a == 'n':
                hit = player1_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        return hit, ingens, counter

def mukatra_2_change_attack_javelin(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'mukatra' and ingens == 1 and gladiator1_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} can force your opponent to change the roll of the dice! ').lower().strip()
            if a == 'y':
                if gladiator2_special() == 'mukatra':
                    mukatra = 0
                elif gladiator2_special() == 'ingens':
                    ingens = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pa) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pa) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'\n{gladiator1()}\n{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nJAVELIN ATTACK:')
                    print(d.renderText(pas))
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
                    print(d.renderText(pds))
                    hit = player1_hit_ini(pa, pd)
                    hit = get_ninos2(pd, hit)
                    if hit > 0:
                        print(hit * '🗡️  ')
                    if hit <= 0:
                        print(len(pd) * '🛡️  ')
                    counter = 'yes'
                    return hit, ingens, counter
            elif a == 'n':
                hit = player1_hit_ini(pa,pd)
                return hit, ingens, counter
    else:
        hit = player1_hit_ini(pa,pd)
        return hit, ingens, counter


def mukatra_ini(p1, p2, initiative, mukatra, ingens, player1, player2):
    if gladiator1_special() == 'mukatra' and mukatra == 1 and initiative == 2 and gladiator2_special() != 'oinomaos' or gladiator1_special() == 'ingens' and ingens == 1 and initiative == 2 and gladiator2_special() != 'oinomaos':
        pas = str(p1).strip('[').strip(']').replace(',', '  ')
        pds = str(p2).strip('[').strip(']').replace(',', '  ')
        print(f'{player1} roll: ')
        print(d.renderText(f'{pas}'))
        print(f'{player2} roll: ')
        print(d.renderText(f'{pds}'))
        while True:
            mu = input(f'{player1}, {gladiator1()} He can force your opponent to change the roll of the dice! ').lower().strip()
            if mu == 'y':
                if gladiator1_special() == 'mukatra':
                    mukatra = 0
                elif gladiator1_special() == 'ingens':
                    ingens = 0
                if len(p2) == 1:
                    p2[0] = random.randint(1,6)
                else:
                    while True:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(p2) <= 5 and len(p2) >= 1:
                            p2[0] = random.randint(1,6)
                            p2.sort(reverse=True)
                        elif cube == '2' and len(p2) <= 5 and len(p2) >= 2:
                            p2[1] = random.randint(1,6)
                            p2.sort(reverse=True)
                        elif cube == '3' and len(p2) <= 5 and len(p2) >= 3:
                            p2[2] = random.randint(1,6)
                            p2.sort(reverse=True)
                        elif cube == '4' and len(p2) <= 5 and len(p2) >= 4:
                            p2[3] = random.randint(1,6)
                            p2.sort(reverse=True)
                        pas = str(p1).strip('[').strip(']').replace(',', '  ')
                        pds = str(p2).strip('[').strip(']').replace(',', '  ')
                        print(f'{player1} roll: ')
                        print(d.renderText(f'{pas}'))
                        print(f'{player2} roll: ')
                        print(d.renderText(f'{pds}'))
                        if sum(p1) == sum(p2):
                            initiative = None
                            return initiative, mukatra, ingens
                        if sum(p1) > sum(p2):
                            initiative = 1
                            if gladiator2_special() == 'ingens' and ingens == 1 or gladiator2_special() == 'mukatra' and mukatra == 1:
                                while True:
                                    mu = input(f'{player2}, {gladiator2()} He can force your opponent to change the roll of the dice! ').lower().strip()
                                    if mu == 'y':
                                        if gladiator2_special() == 'mukatra':
                                            mukatra = 0
                                        elif gladiator2_special() == 'ingens':
                                            ingens = 0
                                        if len(p2) == 1:
                                            p2[0] = random.randint(1,6)
                                        else:
                                            while True:
                                                cube = input('Which cube do you want to change? ')
                                                if cube == '1' and len(p1) <= 5 and len(p1) >= 1:
                                                    p1[0] = random.randint(1,6)
                                                    p1.sort(reverse=True)
                                                elif cube == '2' and len(p1) <= 5 and len(p1) >= 2:
                                                    p1[1] = random.randint(1,6)
                                                    p1.sort(reverse=True)
                                                elif cube == '3' and len(p1) <= 5 and len(p1) >= 3:
                                                    p1[2] = random.randint(1,6)
                                                    p1.sort(reverse=True)
                                                elif cube == '4' and len(p1) <= 5 and len(p1) >= 4:
                                                    p1[3] = random.randint(1,6)
                                                    p1.sort(reverse=True)
                                                pas = str(p1).strip('[').strip(']').replace(',', '  ')
                                                pds = str(p2).strip('[').strip(']').replace(',', '  ')
                                                print(f'{player2} roll: ')
                                                print(d.renderText(f'{pas}'))
                                                print(f'{player1} roll: ')
                                                print(d.renderText(f'{pds}'))
                                                if sum(p1) > sum(p2):
                                                    initiative = 1
                                                    return initiative, mukatra, ingens
                                                elif sum(p1) < sum(p2):
                                                    initiative = 2
                                                    return initiative, mukatra, ingens
                                    elif mu == 'n':
                                        return initiative, mukatra, ingens
                            else:
                                return initiative, mukatra, ingens

                        elif sum(p1) < sum(p2):
                            initiative = 2
                            return initiative, mukatra, ingens
            elif mu == 'n':
                return initiative, mukatra, ingens

    if gladiator2_special() == 'mukatra' and mukatra == 1 and initiative == 1 and gladiator1_special != 'oinomaos' or gladiator2_special() == 'ingens' and ingens == 1 and initiative == 1 and gladiator1_special() != 'oinomaos':
        pas = str(p1).strip('[').strip(']').replace(',', '  ')
        pds = str(p2).strip('[').strip(']').replace(',', '  ')
        print(f'{player1} roll: ')
        print(d.renderText(f'{pas}'))
        print(f'{player2} roll: ')
        print(d.renderText(f'{pds}'))
        while True:
            mu = input(f'{player1}, {gladiator2()} He can force your opponent to change the roll of the dice! ').lower().strip()
            if mu == 'y':
                if gladiator2_special() == 'mukatra':
                    mukatra = 0
                elif gladiator2_special() == 'ingens':
                    ingens = 0
                if len(p2) == 1:
                    p2[0] = random.randint(1,6)
                else:
                    while True:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(p1) <= 5 and len(p1) >= 1:
                            p1[0] = random.randint(1,6)
                            p1.sort(reverse=True)
                        elif cube == '2' and len(p1) <= 5 and len(p1) >= 2:
                            p1[1] = random.randint(1,6)
                            p1.sort(reverse=True)
                        elif cube == '3' and len(p1) <= 5 and len(p1) >= 3:
                            p1[2] = random.randint(1,6)
                            p1.sort(reverse=True)
                        elif cube == '4' and len(p2) <= 5 and len(p1) >= 4:
                            p1[3] = random.randint(1,6)
                            p1.sort(reverse=True)
                        pas = str(p1).strip('[').strip(']').replace(',', '  ')
                        pds = str(p2).strip('[').strip(']').replace(',', '  ')
                        print(f'{player1} roll: ')
                        print(d.render.Text(f'{pas}'))
                        print(f'{player2} roll: ')
                        print(d.render.Text(f'{pds}'))
                        if sum(p1) == sum(p2):
                            initiative = None
                            return initiative, mukatra, ingens
                        if sum(p2) > sum(p1):
                            initiative = 2
                            if gladiator1_special() == 'ingens' and ingens == 1 or gladiator1_special() == 'mukatra' and mukatra == 1:
                                while True:
                                    mu = input(f'{player1}, {gladiator1()} He can force your opponent to change the roll of the dice! ').lower().strip()
                                    if mu == 'y':
                                        if gladiator1_special() == 'mukatra':
                                            mukatra = 0
                                        elif gladiator1_special() == 'ingens':
                                            ingens = 0
                                        if len(p2) == 1:
                                            p2[0] = random.randint(1,6)
                                        else:
                                            while True:
                                                cube = input('Which cube do you want to change? ')
                                                if cube == '1' and len(p2) <= 5 and len(p2) >= 1:
                                                    p2[0] = random.randint(1,6)
                                                    p2.sort(reverse=True)
                                                elif cube == '2' and len(p1) <= 5 and len(p2) >= 2:
                                                    p2[1] = random.randint(1,6)
                                                    p2.sort(reverse=True)
                                                elif cube == '3' and len(p2) <= 5 and len(p2) >= 3:
                                                    p2[2] = random.randint(1,6)
                                                    p2.sort(reverse=True)
                                                elif cube == '4' and len(p2) <= 5 and len(p2) >= 4:
                                                    p2[3] = random.randint(1,6)
                                                    p2.sort(reverse=True)
                                                pas = str(p1).strip('[').strip(']').replace(',', '  ')
                                                pds = str(p2).strip('[').strip(']').replace(',', '  ')
                                                print(f'{player1} roll: ')
                                                print(d.renderText(f'{pas}'))
                                                print(f'{player2} roll: ')
                                                print(d.renderText(f'{pds}'))
                                                if sum(p1) > sum(p2):
                                                    initiative = 1
                                                    return initiative, mukatra, ingens
                                                elif sum(p1) < sum(p2):
                                                    initiative = 2
                                                    return initiative, mukatra, ingens
                                    elif mu == 'n':
                                        return initiative, mukatra, ingens
                            else:
                                return initiative, mukatra, ingens
                        elif sum(p2) < sum(p1):
                            initiative = 1
                            return initiative, mukatra, ingens
            elif mu == 'n':
                return initiative, mukatra, ingens
    else:
        return initiative, mukatra, ingens

