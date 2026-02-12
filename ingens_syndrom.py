from use_your_weapon import use_your_weapon_player1, use_your_weapon_player2
import random
from gladiator_statistics import gladiator1_special, gladiator2_special, gladiator1_armor, gladiator1_weapon, gladiator2_armor, gladiator2_weapon, gladiator1, gladiator2
from player_hit import player1_hit, player2_hit
from your_helmet import your_helmet_1, your_helmet_2
from your_sword import your_sword_1, your_sword_2
from gannikus_hit import gannikus_hit
from filemon_and_friends import get_ninos, get_ninos2
from pyfiglet import Figlet
d = Figlet(font='slant')

def part1(pa, pd, hit, javelin, mukatra, ingens, use_sword, use_helmet):
    print('FIRST 1111')
    global sword, helmet

    hit, s, h, sword, helmet = use_your_weapon_player1(pa, pd, hit, javelin, use_sword, use_helmet)
    our_helmet = h
    print(f'sword {sword}, helmet {helmet}')

    print(f'our helmet {our_helmet}')
    if gladiator1_special() == 'mukatra' and mukatra == 1 and gladiator2_special != 'oinomaos' or gladiator1_special() == 'ingens' and ingens == 1 and gladiator2_special != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                if gladiator1_special() == 'mukatra':
                    mukatra = 0
                elif gladiator1_special() == 'ingens':
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
                    print('Player1 attack:')
                    print(d.renderText(pas))
                    print('Player2 defence:')
                    print(d.renderText(pds))
                    if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player1_hit(pa, pd)
                    hit = get_ninos2(pd, hit)
                    print(f'mukatra y, hit {hit}')
                    for _ in range(hit):
                        print('HIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    if gladiator1_special() == 'mukatra' and mukatra == 0 and gladiator2_armor() == 'helmet' and helmet == 'n' or gladiator1_special == 'ingens' and ingens == 0 and gladiator2_armor() == 'helmet' and helmet == 'n':
                        hit, s, h, sword, helmet = use_your_weapon_player1(pa, pd, hit, javelin, s, h)
                        print(f'77, mukatra 0, hit {hit}')
                        print(f'hit {hit}, m: {mukatra}m ingens: {ingens}, sword {s}, helmet {h}')
                        return hit, mukatra, ingens, s, h
                    else:
                        return hit, mukatra, ingens, s, h
            elif a == 'n':
                return hit, mukatra, ingens, s, h
    else:
        print(f'else, firstafter weapon {hit}')
        return hit, mukatra, ingens, s, h


def part2(pa, pd, hit, javelin, mukatra, ingens, use_sword, use_helmet):
    print('SECOND 22222')
    global sword, helmet
    print(f'sword {sword}, helmet {helmet}')
    if helmet != 'n' and sword != 'n' or sword != 'y' and helmet != 'n':
        hit, s, h, sword, helmet = use_your_weapon_player1(pa, pd, hit, javelin, use_sword, use_helmet)
    if helmet == 'n':
        h = 1
    else:
        h = 0
    if sword == 'n':
        s = 1
    else:
        s = 0
    if gladiator2_special() == 'mukatra' and mukatra == 1 and gladiator1_special() != 'oinomaos' or gladiator2_special() == 'ingens' and ingens == 1 and gladiator1_special() != 'oinomaos':
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
                        elif cube == '5' and len(pa) == 5:
                            pa[4] = random.randint(1,6)
                            pa.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print('Player1 attack:')
                    print(d.renderText(pas))
                    print('Player2 defence:')
                    print(d.renderText(pds))
                    if gladiator1_special() == 'gannikus' and gladiator2_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player1_hit(pa, pd)
                    hit = get_ninos2(pd, hit)
                    print(f'hit + javelin {hit}')
                    for _ in range(hit):
                        print('HIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    print(f'our sword {use_sword}')
                    print(f'sword: {sword}, {gladiator2()}: {ingens}')
                    if gladiator2_special() == 'mukatra' and mukatra == 0 and gladiator1_weapon() == 'sword' and sword == 'n' or gladiator2_special() == 'ingens' and ingens == 0 and gladiator1_weapon() == 'sword' and sword == 'n':
                        hit, s, h, sword, helmet = use_your_weapon_player1(pa, pd, hit, javelin, s, h)
                        print(f'mukatra 0, after weapon {hit}')
                        print(f'mukatra y {hit}')
                        return hit, mukatra, ingens, s, h
                    else:
                       return hit, mukatra, ingens, s, h

            elif a == 'n':
                return hit, mukatra, ingens, s, h

    else:
        print(f'second, else after weapon {hit}')
        return hit, mukatra, ingens, s, h


def part3(pa, pd, hit, javelin, mukatra, ingens, use_sword, use_helmet):
    print('THIRD 3333')
    global sword, helmet

    hit, s, h, sword, helmet = use_your_weapon_player2(pa, pd, hit, javelin, use_sword, use_helmet)
    print(f'sword {sword}, helmet {helmet}')
    if gladiator2_special() == 'mukatra' and mukatra == 1 and gladiator1_special() != 'oinomaos' or gladiator2_special() == 'ingens' and ingens == 1 and gladiator1_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator2()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                if gladiator2_special() == 'mukatra':
                    mukatra = 0
                elif gladiator2_special() == 'ingens':
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
                    print('Player2 attack:')
                    print(d.renderText(pas))
                    print('Player1 defence:')
                    print(d.renderText(pds))
                    if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player2_hit(pa, pd)
                    hit = get_ninos(pd, hit)
                    print(f'if mukatra y: {hit}')
                    for _ in range(hit):
                        print('HIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    print(f'if mukatra = {mukatra} and gladiator1_armor = {gladiator1_armor()} and use_helmet = {h}')
                    if gladiator2_special() == 'mukatra' and mukatra == 0 and gladiator1_armor() == 'helmet' and h == 1 or gladiator2_special() == 'ingens' and ingens == 0 and gladiator1_armor() == 'helmet' and h == 1:
                        print('all check')
                        hit, s, h, sword, helmet = use_your_weapon_player2(pa, pd, hit, javelin, s, h)
                        print(f'if mukatra 0 and use helmetp1 + javelin: {hit}')
                        return hit, mukatra, ingens, s, h
                    else:
                        if h == 1:
                            hit, s, h, helmet = use_your_weapon_player2(pa, pd, hit, javelin, s, h)
                        return hit, mukatra, ingens, s, h
            elif a == 'n':
                print(f'if mukatra n: {hit}')
                return hit, mukatra, ingens, s, h
    else:
        print(f'third, hit else: {hit}')
        a = None
        return hit, mukatra, ingens, s, h


def part4(pa, pd, hit, javelin, mukatra, ingens, use_sword, use_helmet):
    print('THORTH 4444')
    global sword, helmet
    print(f'sword {sword}, helmet {helmet}')
    if sword != 'n' and helmet != 'n' or sword != 'y' and helmet != 'n':
        hit, s, h, sword, helmet = use_your_weapon_player2(pa, pd, hit, javelin, use_sword, use_helmet)
    if helmet == 'n':
        h = 1
    else:
        h = 0
    if sword == 'n':
        s = 1
    else:
        s = 0
    if gladiator1_special() == 'mukatra' and mukatra == 1 and gladiator2_special() != 'oinomaos' or gladiator1_special() == 'ingens' and ingens == 1 and gladiator2_special() != 'oinomaos':
        while True:
            a = input(f'{gladiator1()} can force your opponent to change the roll of the dice! ')
            if a == 'y':
                if gladiator1_special() == 'mukatra':
                    mukatra = 0
                elif gladiator1_special() == 'ingens':
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
                        elif cube == '5' and len(pa) == 5:
                            pa[4] = random.randint(1,6)
                            pa.sort(reverse=True)
                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                    print('Player2 attack:')
                    print(d.renderText(pas))
                    print('Player1 defence:')
                    print(d.renderText(pds))
                    if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                        hit = gannikus_hit(pa, pd)
                    else:
                        hit = player2_hit(pa, pd)
                    hit = get_ninos(pd, hit)
                    print(f'mukatra y hit: {hit}')
                    for _ in range(hit):
                        print('HIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    if gladiator1_special() == 'mukatra' and mukatra == 0 and gladiator2_weapon() == 'sword' and sword == 'n' or gladiator1_special() == 'ingens' and ingens == 0 and gladiator2_weapon() == 'sword' and sword == 'n':
                        hit, s, h, sword, helmet = use_your_weapon_player2(pa, pd, hit, javelin, s, h)
                        print(f'mukatra 0  {hit}')
                        return hit, mukatra, ingens, s, h
                    else:
                        s = None
                        return hit, mukatra, ingens, s, h

            elif a == 'n':
                print(f'mukatra n: {hit}')
                return hit, mukatra, ingens, s, h
    else:
        print(f'forth hit else: {hit}')
        return hit, mukatra, ingens, s, h
