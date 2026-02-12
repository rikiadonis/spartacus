from gladiator_statistics import gladiator1_add_gear, gladiator2_add_gear, gladiator1, gladiator2
from player1 import player1_ini_attack, player1_defence
from player2 import player2_ini_attack, player2_defence
from player_hit import player1_hit_ini, player2_hit_ini
from ninos_syndrom import get_ninos, get_ninos2, get_alard, get_alard2
from javelin_syndrom import get_javelin_ingens_1, get_javelin_ingens_2
from face_off import player2_consequences, player1_consequences
from pyfiglet import Figlet
from your_helmet import your_helmet_1, your_helmet_2
from armament import player1_get_shield, player2_get_shield
from gladiator_special import danel_1, danel_2
j = Figlet(font='speed')
d = Figlet(font='slant')

def player1_get_javelin(ini_1, javelin, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_2, defence_2, ini_2, attack_1, defence_1, player1, player2, shield_2):
    if javelin == 1 and gladiator1_add_gear() == 'javelin':
        javelin -= 1
        pd = player2_defence(defence_2)
        pa, pd = danel_2(defence_2, ini_2, attack_1)
        pa = player1_ini_attack(ini_1)
        pas = str(pa).strip('[').strip(']').replace(',', '  ')
        pds = str(pd).strip('[').strip(']').replace(',', '  ')
        print(f'\n{gladiator1()}\n{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nJAVELIN ATTACK:')
        print(j.renderText(pas))
        print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
        print(d.renderText(pds))
        javelin_hit = player1_hit_ini(pa, pd)
        if javelin_hit > 0:
            print(javelin_hit * '🗡️  ')
        if javelin_hit <= 0:
            print(defence_2 * '🛡️  ')
        javelin_hit, h = your_helmet_2(pa, pd, javelin_hit, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
        javelin_hit, i, m, h = get_javelin_ingens_1(pa, pd, javelin_hit, mukatra, ingens, h, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
        mukatra = m
        ingens = i
        use_helmet_2 = h
        javelin_hit = get_ninos2(pd, javelin_hit)
        if javelin_hit > 0 and shield_2 == 1:
            javelin_hit, shield = player2_get_shield(javelin_hit, shield_2, player2)
            shield_2 = shield
        print(f'\n{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
        a2, d2, i2 = player2_consequences(javelin_hit, attack_2, defence_2, ini_2, player2)
        attack_2 = a2
        defence_2 = d2
        ini_2 = i2
        acube_2 = attack_2 * '🟥 '
        decube_2 = defence_2 * '🟫 '
        incube_2 = ini_2 * '🟦 '
        attack_1, defence_1, ini_1 = get_alard2(pd, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2, player1, player2)
        return  javelin, mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, shield_2

    else:
        return javelin, mukatra, ingens, use_helmet_2, attack_2, defence_2, ini_2, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, shield_2





def player2_get_javelin(ini_2, javelin, mukatra, ingens, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, attack_1, defence_1, ini_1, attack_2, defence_2, player1, player2, shield_1):
    if javelin == 1 and gladiator2_add_gear() == 'javelin':
        javelin -= 1

        pd = player2_defence(defence_1)
        pa, pd = danel_1(defence_1, ini_1, attack_2)
        pa = player1_ini_attack(ini_2)
        pas = str(pa).strip('[').strip(']').replace(',', '  ')
        pds = str(pd).strip('[').strip(']').replace(',', '  ')
        print(f'\n{gladiator2()}\n{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nJAVELIN ATTACK:')
        print(j.renderText(pas))
        print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
        print(d.renderText(pds))
        javelin_hit = player2_hit_ini(pa, pd)
        if javelin_hit > 0:
            print(javelin_hit * '🗡️  ')
        if javelin_hit <= 0:
            print(defence_1 * '🛡️  ')
        javelin_hit, h = your_helmet_1(pa, pd, javelin_hit, use_helmet_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
        javelin_hit, i, m, h = get_javelin_ingens_2(pa, pd, javelin_hit, mukatra, ingens, h, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
        mukatra = m
        ingens = i
        use_helmet_2 = h
        javelin_hit = get_ninos(pd, javelin_hit)
        if javelin_hit > 0 and shield_1 == 1:
            javelin_hit, shield = player1_get_shield(javelin_hit, shield_1, player1)
            shield_1 = shield
        print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
        a2, d2, i2 = player1_consequences(javelin_hit, attack_1, defence_1, ini_1, player1)
        attack_1 = a2
        defence_1 = d2
        ini_1 = i2
        acube_1 = attack_1 * '🟥 '
        decube_1 = defence_1 * '🟫 '
        incube_1 = ini_1 * '🟦 '
        attack_2, defence_2, ini_2 = get_alard(pd, attack_2, defence_2, ini_2, acube_1, decube_1, incube_1, player1, player2)
        return  javelin, mukatra, ingens, use_helmet_2, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2, shield_1

    else:
        return javelin, mukatra, ingens, use_helmet_2, attack_1, defence_1, ini_1, acube_1, decube_1, incube_1, attack_2, defence_2, ini_2, shield_1
