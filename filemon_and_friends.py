from gladiator_statistics import gladiator1_special, gladiator2_special, gladiator1, gladiator2
from initiative import get_initiative
import random
from gannikus_hit import gannikus_hit
from use_your_weapon import use_your_weapon_player1, use_your_weapon_player2
from ninos_syndrom import get_ninos, get_ninos2
from player_hit import player1_hit, player2_hit
from pyfiglet import Figlet
d = Figlet(font='slant')


def get_filemon(ini_1, ini_2, p1, p2, initiative, filemon):
    if gladiator1_special() == 'filemon' and initiative == 2 and filemon == 1 and gladiator2_special() != 'oinomaos' or gladiator2_special() == 'filemon' and gladiator1_special() != 'oinomaos' and initiative == 1 and filemon == 1:
        while True:
            fil = input('Filemon can reapet the roll for initiative! ')
            if fil == 'y':
                filemon == 1
                initiative, player1, player2 = get_initiative(ini_1, ini_2, p1, p2)
                return initiative, player1, player2
            elif fil == 'n':
                return initiative, p1, p2
    else:
        return initiative, p1, p2


def get_mukatra_1_change_defence(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'mukatra' and mukatra == 1 and gladiator2_special != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
                mukatra = 0
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
                        elif cube == '5' and len(pd) == 5:
                            pd[4] = random.randint(1,6)
                            pd.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, mukatra, counter
            elif a == 'n' or a == 'no':
                return hit, mukatra, counter
    else:
        return hit, mukatra, counter


def get_mukatra_1_change_attack(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'mukatra' and mukatra == 1 and gladiator2_special != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
                mukatra = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '5' and len(pa) == 5:
                            pa[4] = random.randint(1,6)
                            pa.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, mukatra, counter
            elif a == 'n' or a == 'no':
                return hit, mukatra, counter
    else:
        return hit, mukatra, counter

def get_mukatra_2_change_defence(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'mukatra' and mukatra == 1 and gladiator1_special != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
                mukatra = 0
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
                        elif cube == '5' and len(pd) == 5:
                            pd[4] = random.randint(1,6)
                            pd.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, mukatra, counter
            elif a == 'n' or a == 'no':
                return hit, mukatra, counter
    else:
        return hit, mukatra, counter

def get_mukatra_2_change_attack(pa, pd, hit, mukatra, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'mukatra' and mukatra == 1 and gladiator1_special != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
                mukatra = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '5' and len(pa) == 5:
                            pa[4] = random.randint(1,6)
                            pa.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, mukatra, counter
            elif a == 'n' or a == 'no':
                return hit, mukatra, counter
    else:
        return hit, mukatra, counter




def get_ingens_1_change_defence(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'ingens' and ingens == 1 and gladiator2_special != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
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
                        elif cube == '5' and len(pd) == 5:
                            pd[4] = random.randint(1,6)
                            pd.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, ingens, counter
            elif a == 'n' or a == 'yes':
                return hit, ingens, counter
    else:
        return hit, ingens, counter

def get_ingens_1_change_attack(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator1_special() == 'ingens' and ingens == 1 and gladiator2_special != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '5' and len(pa) == 5:
                            pa[4] = random.randint(1,6)
                            pa.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, ingens, counter
            elif a == 'n' or a == 'no':
                return hit, ingens, counter
    else:
        return hit, ingens, counter

def get_ingens_2_change_defence(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'ingens' and ingens == 1 and gladiator1_special != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
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
                        elif cube == '5' and len(pd) == 5:
                            pd[4] = random.randint(1,6)
                            pd.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, ingens, counter
            elif a == 'n' or a == 'no':
                return hit, ingens, counter
    else:
        return hit, ingens, counter

def get_ingens_2_change_attack(pa, pd, hit, ingens, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    counter = 'no'
    if gladiator2_special() == 'ingens' and ingens == 1 and gladiator1_special != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} He can force your opponent to change the roll of the dice! ')
            if a == 'y' or a == 'yes':
                ingens = 0
                while True:
                    if len(pd) == 1:
                        pa[0] = random.randint(1,6)
                    else:
                        cube = input('Which cube do you want to change? ')
                        if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                            pa[0] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '2' and len(pd) <= 5 and len(pa) >= 2:
                            pa[1] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                            pa[2] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '4' and len(pd) <= 5 and len(pa) >= 4:
                            pa[3] = random.randint(1,6)
                            pa.sort(reverse=True)
                        elif cube == '5' and len(pa) == 5:
                            pa[4] = random.randint(1,6)
                            pa.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                    print(d.renderText(pas))
                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
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
                    counter = 'yes'
                    return hit, ingens, counter
            elif a == 'n' or a == 'no':
                return hit, ingens, counter
    else:
        return hit, ingens, counter
