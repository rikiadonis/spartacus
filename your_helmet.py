from gladiator_statistics import gladiator1_armor, gladiator2_armor, gladiator1_special, gladiator2_special
from armament import get_helmet
from player_hit import player1_hit_ini, player2_hit_ini
from ninos_syndrom import get_ninos, get_ninos2
from pyfiglet import Figlet
d = Figlet(font='slant')
j = Figlet(font='speed')
def your_helmet_2(pa, pd, hit, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    if gladiator2_armor() == 'helmet' and use_helmet == 1:
        while True:
            helmet = input(f'{player2}, do you want use a helmet? ').strip().lower()
            if helmet == 'y' or helmet == 'yes':
                use_helmet = 0
                pd = get_helmet(pd)
                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nJAVELIN ATTACK:')
                print(j.renderText(pas))
                print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE WITH A HELMET:')
                print(d.renderText(pds))
                hit = player1_hit_ini(pa, pd)
                hit = get_ninos2(pd, hit)
                if hit > 0:
                    print(hit * '🗡️  ')
                if hit <= 0:
                    print(len(pd) * '🛡️  ')
                return hit, use_helmet
            elif helmet == 'n' or helmet == 'no':
                return hit, use_helmet
    else:
        return hit, use_helmet

def your_helmet_1(pa, pd, hit, use_helmet, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2):
    if gladiator1_armor() == 'helmet' and use_helmet == 1:
        while True:
            helmet = input(f'{player1}, do you want use a helmet? ').strip().lower()
            if helmet == 'y' or helmet == 'yes':
                use_helmet = 0
                pd = get_helmet(pd)
                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nJAVELIN ATTACK:')
                print(j.renderText(pas))
                print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE WITH A HELMET:')
                print(d.renderText(pds))
                hit = player2_hit_ini(pa, pd)
                hit = get_ninos(pd, hit)
                if hit > 0:
                    print(hit * '🗡️  ')
                if hit <= 0:
                    print(len(pd) * '🛡️  ')
                return hit, use_helmet
            elif helmet == 'n' or helmet == 'no':
                return hit, use_helmet
    else:
        return hit, use_helmet
