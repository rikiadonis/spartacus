from gladiator_statistics import gladiator1_armor, gladiator2_weapon, gladiator2_armor, gladiator1_weapon, gladiator1_special, gladiator2_special
from armament import get_sword, get_helmet
from player_hit import player1_hit, player2_hit
from player1 import player1_attack
from player2 import player2_defence
from ninos_syndrom import get_ninos, get_ninos2
from gannikus_hit import gannikus_hit
from pyfiglet import Figlet
d = Figlet(font='slant')

def main():
    pass


def use_your_weapon_player1(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2):
    acube_1 = attack_1 * '🟥 '
    decube_1 = defence_1 * '🟫 '
    incube_1 = ini_1 * '🟦 '
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
    if gladiator1_weapon() == 'sword' and use_sword == 1:
        while True:
            sword = input(f'{player1}, do you want use a sword? ').strip().lower()
            if sword == 'y' or sword == 'yes':
                use_sword = 0
                pa = get_sword(pa)
                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK WITH A SWORD:')
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
                    print(defence_2 * '🛡️  ')
                if gladiator2_armor() == 'helmet'and use_helmet == 1:
                    while True:
                        helmet = input(f'{player2}, do you want use a helmet? ').strip().lower()
                        if helmet == 'y':
                            use_helmet = 0
                            pd = get_helmet(pd)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK WITH A SWORD:')
                            print(d.renderText(pas))
                            print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE WITH A HELMET:')
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
                            return hit, use_sword, use_helmet
                        elif helmet == 'n' or sword == 'no':
                            return hit, use_sword, use_helmet
                else:
                    return hit, use_sword, use_helmet
            elif sword == 'n' or sword == 'no':
                if gladiator2_armor() == 'helmet' and use_helmet == 1:
                    while True:
                        helmet = input(f'{player2}, do you want use a helmet? ').strip().lower()
                        if helmet == 'y' or helmet == 'yes':
                            use_helmet = 0
                            pd = get_helmet(pd)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                            print(d.renderText(pas))
                            print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE WITH A HELMET:')
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
                            if gladiator1_weapon() == 'sword' and use_sword == 1:
                                sword = input(f'{player1}, do you want use a sword? ').strip().lower()
                                if sword == 'y' or sword == 'yes':
                                    use_sword = 0
                                    pa = get_sword(pa)
                                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK WITH A SWORD:')
                                    print(d.renderText(pas))
                                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE WITH A HELMET:')
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
                                    return hit, use_sword, use_helmet
                                elif sword == 'n' or sword == 'no':
                                    return hit, use_sword, use_helmet
                            else:
                                return hit, use_sword, use_helmet
                        elif helmet == 'n' or helmet == 'no':
                            return hit, use_sword, use_helmet
                else:
                    return hit, use_sword, use_helmet

    if gladiator2_armor() == 'helmet' and use_helmet == 1:
        acube_1 = attack_1 * '🟥 '
        decube_1 = defence_1 * '🟫 '
        incube_1 = ini_1 * '🟦 '
        acube_2 = attack_2 * '🟥 '
        decube_2 = defence_2 * '🟫 '
        incube_2 = ini_2 * '🟦 '
        while True:
            helmet = input(f'{player2}, do you want use a helmet? ').strip().lower()
            if helmet == 'y' or helmet == 'yes':
                use_helmet = 0
                pd = get_helmet(pd)
                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
                print(d.renderText(pas))
                print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE WITH A HELMET:')
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
                return hit, use_sword, use_helmet
            elif helmet == 'n' or helmet == 'no':
                return hit, use_sword, use_helmet
    else:
        return hit, use_sword, use_helmet


def use_your_weapon_player2(pa, pd, hit, use_sword, use_helmet, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, player1, player2):
    acube_1 = attack_1 * '🟥 '
    decube_1 = defence_1 * '🟫 '
    incube_1 = ini_1 * '🟦 '
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
    if gladiator2_weapon() == 'sword' and use_sword == 1:
        while True:
            sword = input(f'{player2}, do you want use a sword? ').strip().lower()
            if sword == 'y' or sword == 'yes':
                use_sword = 0
                pa = get_sword(pa)
                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK WITH A SWORD:')
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
                    print(defence_1 * '🛡️  ')
                if gladiator1_armor() == 'helmet' and use_helmet == 1:
                    while True:
                        helmet = input(f'{player1}, do you want use a helmet? ').strip().lower()
                        if helmet == 'y' or helmet == 'yes':
                            use_helmet = 0
                            pd = get_helmet(pd)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK WITH A SWORD:')
                            print(d.renderText(pas))
                            print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE WITH A HELMET:')
                            print(d.renderText(pds))
                            if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                                hit = gannikus_hit(pa, pd)
                            else:
                                hit = player2_hit(pa, pd)
                            hit = get_ninos(pd, hit)
                            if hit > 0:
                                print(hit * '🗡️  ')
                            if hit <= 0:
                                print(defence_1 * '🛡️  ')
                            return hit, use_sword, use_helmet
                        elif helmet == 'n' or helmet == 'no':
                            return hit, use_sword, use_helmet
                else:
                    return hit, use_sword, use_helmet
            elif sword == 'n' or sword == 'no':
                if gladiator1_armor() == 'helmet' and use_helmet == 1:
                    while True:
                        helmet = input(f'{player1}, do you want use a helmet? ').strip().lower()
                        if helmet == 'y' or helmet == 'yes':
                            use_helmet = 0
                            pd = get_helmet(pd)
                            pas = str(pa).strip('[').strip(']').replace(',', '  ')
                            pds = str(pd).strip('[').strip(']').replace(',', '  ')
                            print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                            print(d.renderText(pas))
                            print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE WITH A HELMET:')
                            print(d.renderText(pds))
                            if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                                hit = gannikus_hit(pa, pd)
                            else:
                                hit = player2_hit(pa, pd)
                            hit = get_ninos(pd, hit)
                            if hit > 0:
                                print(hit * '🗡️  ')
                            if hit <= 0:
                                print(defence_1 * '🛡️  ')
                            if gladiator2_weapon() == 'sword' and use_sword == 1:
                                sword = input(f'{player2}, do you want use a sword? ').strip().lower()
                                if sword == 'y' or sword == 'yes':
                                    use_sword = 0
                                    pa = get_sword(pa)
                                    pas = str(pa).strip('[').strip(']').replace(',', '  ')
                                    pds = str(pd).strip('[').strip(']').replace(',', '  ')
                                    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK WITH A SWORD:')
                                    print(d.renderText(pas))
                                    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE WITH A HELMET:')
                                    print(d.renderText(pds))
                                    if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                                        hit = gannikus_hit(pa, pd)
                                    else:
                                        hit = player2_hit(pa, pd)
                                    hit = get_ninos(pd, hit)
                                    if hit > 0:
                                        print(hit * '🗡️  ')
                                    if hit <= 0:
                                        print(defence_1 * '🛡️  ')
                                    return hit, use_sword, use_helmet
                                elif sword == 'n' or sword == 'no':
                                    return hit, use_sword, use_helmet
                            else:
                                return hit, use_sword, use_helmet
                        elif helmet == 'n' or helmet == 'no':
                            return hit, use_sword, use_helmet
                else:
                    return hit, use_sword, use_helmet

    if gladiator1_armor() == 'helmet' and use_helmet == 1:
        while True:
            helmet = input(f'{player1}, do you want use a helmet? ').strip().lower()
            if helmet == 'y' or helmet == 'yes':
                use_helmet = 0
                pd = get_helmet(pd)
                pas = str(pa).strip('[').strip(']').replace(',', '  ')
                pds = str(pd).strip('[').strip(']').replace(',', '  ')
                print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
                print(d.renderText(pas))
                print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE WITH A HELMET:')
                print(d.renderText(pds))
                if gladiator2_special() == 'gannikus' and gladiator1_special != 'oinomaos':
                    hit = gannikus_hit(pa, pd)
                else:
                    hit = player2_hit(pa, pd)
                hit = get_ninos(pd, hit)
                if hit > 0:
                    print(hit * '🗡️  ')
                if hit <= 0:
                    print(defence_1 * '🛡️  ')
                return hit, use_sword, use_helmet
            elif helmet == 'n' or helmet == 'no':
                return hit, use_sword, use_helmet
    else:
        return hit, use_sword, use_helmet

if __name__=='__main__':
    main()
