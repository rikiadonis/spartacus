from gladiator_statistics import gladiator1_weapon, gladiator2_weapon, gladiator1_armor, gladiator2_armor, gladiator1_add_gear, gladiator2_add_gear
import random
from player1 import player1_ini_attack, player1_defence
from player2 import player2_ini_attack, player2_defence
from gladiator_statistics import gladiator1, gladiator2
from player_hit import player1_hit_ini, player2_hit_ini
from initiative import get_initiative
from pyfiglet import Figlet
d = Figlet(font='slant')
def main():
    pass

def get_sword(pa):
     while True:
        if len(pa) == 1:
            pa[0] = random.randint(1,6)
            return pa
        else:
            cube = input('Which cube do you want to change? ')
            if cube == '1' and len(pa) <= 5 and len(pa) >= 1:
                pa[0] = random.randint(1,6)
                pa.sort(reverse=True)
                return pa
            elif cube == '2' and len(pa) <= 5 and len(pa) >= 2:
                pa[1] = random.randint(1,6)
                pa.sort(reverse=True)
                return pa
            elif cube == '3' and len(pa) <= 5 and len(pa) >= 3:
                pa[2] = random.randint(1,6)
                pa.sort(reverse=True)
                return pa
            elif cube == '4' and len(pa) <= 5 and len(pa) >= 4:
                pa[3] = random.randint(1,6)
                pa.sort(reverse=True)
                return pa
            elif cube == '5' and len(pa) == 5:
                pa[4] = random.randint(1,6)
                pa.sort(reverse=True)
                return pa

def get_helmet(pd):
    while True:
        if len(pd) == 1:
            pd[0] = random.randint(1,6)
            return pd
        else:
            cube_2 = input('Which cube do you want to change? ')
            if cube_2 == '1' and len(pd) <= 5 and len(pd) >= 1:
                pd[0] = random.randint(1,6)
                pd.sort(reverse=True)
                return pd
            elif cube_2 == '2' and len(pd) <= 5 and len(pd) >= 2:
                pd[1] = random.randint(1,6)
                pd.sort(reverse=True)
                return pd
            elif cube_2 == '3' and len(pd) <= 5 and len(pd) >= 3:
                pd[2] = random.randint(1,6)
                pd.sort(reverse=True)
                return pd
            elif cube_2 == '4' and len(pd) <= 5 and len(pd) >= 4:
                pd[3] = random.randint(1,6)
                pd.sort(reverse=True)
                return pd
            elif cube_2 == '5' and len(pd) == 5:
                pd[4] = random.randint(1,6)
                pd.sort(reverse=True)
                return pd

def player1_get_axe(hit, axe, player1):
    if gladiator1_weapon() == 'axe' and axe == 1:
        while True:
            a = input(f'{player1}, do you want use an axe? ').strip().lower()
            if a == 'y' or a == 'yes' and axe == 1:
                hit += 1
                axe -= 1
                if hit > 0:
                   print(hit * '🗡️  ')
                return hit, axe
            elif a == 'n' or a == 'no':
                return hit, axe
    else:
        return hit, axe

def player1_get_shield(hit, shield, player1):
    if gladiator1_armor() == 'shield' and shield == 1:
        while True:
            a = input(f'{player1}, do you want use a shield? ').strip().lower()
            if a == 'y' or a == 'yes' and shield == 1:
                hit -= 1
                shield -= 1
                if hit > 0:
                    print(hit * '🗡️  ')
                if hit <= 0:
                    print('🛡️')
                return hit, shield
            elif a == 'n' or a == 'no':
                return hit, shield
    else:
        return hit, shield

def player2_get_shield(hit, shield, player2):
    if gladiator2_armor() == 'shield' and shield == 1:
        while True:
            a = input(f'{player2}, do you want use a shield? ').strip().lower()
            if a == 'y' or a == 'yes' and shield == 1:
                hit -= 1
                shield -= 1
                if hit > 0:
                    print(hit * '🗡️  ')
                if hit <= 0:
                    print('🛡️')
                return hit, shield
            elif a == 'n' or a == 'no':
                return hit, shield
    else:
        return hit, shield

def player2_get_axe(hit, axe, player2):
    if gladiator2_weapon() == 'axe' and axe == 1:
        while True:
            a = input(f'{player2}, do you want use an axe? ').strip().lower()
            if a == 'y' or a == 'yes' and axe == 1:
                hit += 1
                axe -= 1
                print(hit * '🗡️  ')
                return hit, axe
            elif a == 'n' or a == 'no':
                return hit, axe
    else:
        return hit, axe



if __name__=='__main__':
    main()
