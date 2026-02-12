import random
from initiative import get_initiative
from gladiator_statistics import gladiator1_special, gladiator2_special, gladiator1, gladiator2, gladiator1_attack, gladiator1_defence, gladiator1_ini, gladiator2_attack, gladiator2_defence, gladiator2_ini, gladiator1_weapon, gladiator2_weapon, gladiator1_armor, gladiator2_armor, gladiator1_add_gear, gladiator2_add_gear
from face_off import player2_consequences, player1_consequences
from player_hit import player1_hit, player2_hit
from player1 import player1_attack, player1_defence
from player2 import player2_attack, player2_defence
from armament import player1_get_axe, player2_get_axe, player1_get_shield, player2_get_shield
from gladiator_special import mukatra_ini, danel_1, danel_2
from javelin import player1_get_javelin, player2_get_javelin
from filemon_and_friends import get_filemon
from ninos_syndrom import get_ninos, get_ninos2, get_alard, get_alard2, get_valerius_1, get_valerius_2
from gannikus_hit import gannikus_hit
from gladiator_syndrom import part1, part2
from pyfiglet import Figlet

def get_attack_1(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2, player1, player2):
    d = Figlet(font='slant')
    acube_1 = attack_1 * '🟥 '
    decube_1 = defence_1 * '🟫 '
    incube_1 = ini_1 * '🟦 '
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
    pa = player1_attack(attack_1)
    pd = player2_defence(defence_2)
    pa, pd = danel_2(defence_2, ini_2, attack_1)
    pas = str(pa).strip('[').strip(']').replace(',', '  ')
    pds = str(pd).strip('[').strip(']').replace(',', '  ')
    print(f'\n{gladiator1()} Strikes!\n{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nATTACK:')
    print(d.renderText(pas))
    print(f'{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nDEFENCE:')
    print(d.renderText(pds))
    if gladiator1_special() == 'gannikus' and gladiator2_special() != 'oinomaos':
        hit = gannikus_hit(pa, pd)
    else:
        hit = player1_hit(pa, pd)
    if hit > 0:
        print(hit * '🗡️  ')
    if hit <= 0:
        print(defence_2 * '🛡️  ')
    hit,m,i,s,h = part1(pa, pd, hit, mukatra, ingens, use_sword_1, use_helmet_2, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    ingens = i
    mukatra = m
    use_sword_1 = s
    use_helmet_2 = h
    hit, axe = player1_get_axe(hit, axe_1, player1)
    hit = get_ninos2(pd, hit)
    axe_1 = axe
    if hit > 0 and shield_2 == 1:
        hit, shield = player2_get_shield(hit, shield_2, player2)
        shield_2 = shield
    get_valerius_1(hit)
    print(f'{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
    a2, d2, i2 = player2_consequences(hit, attack_2, defence_2, ini_2, player2)
    attack_2 = a2
    defence_2 = d2
    ini_2 = i2
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
    attack_1, defence_1, ini_1 = get_alard2(pd, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2, player1, player2)
    return attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_1, use_helmet_2, axe_1, shield_2

def get_attack_2(attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1, player1, player2):
    d = Figlet(font='slant')
    acube_1 = attack_1 * '🟥 '
    decube_1 = defence_1 * '🟫 '
    incube_1 = ini_1 * '🟦 '
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
    pa = player2_attack(attack_2)
    pd = player1_defence(defence_1)
    pa, pd = danel_1(defence_1, ini_1, attack_2)
    pas = str(pa).strip('[').strip(']').replace(',', '  ')
    pds = str(pd).strip('[').strip(']').replace(',', '  ')
    print(f'\n{gladiator2()} Strikes!\n{player2}:\nATK: {acube_2} DEF: {decube_2} SPD: {incube_2}\nATTACK:')
    print(d.renderText(pas))
    print(f'{player1}:\nATK: {acube_1} DEF: {decube_1} SPD: {incube_1}\nDEFENCE:')
    print(d.renderText(pds))
    if gladiator2_special() == 'gannikus' and gladiator1_special() != 'oinomaos':
        hit = gannikus_hit(pa, pd)
    else:
        hit = player2_hit(pa, pd)
    if hit > 0:
        print(hit * '🗡️  ')
    if hit <= 0:
        print(defence_1 * '🛡️  ')
    new_hit, m, i, s, h = part2(pa, pd, hit, mukatra, ingens, use_sword_2, use_helmet_1, attack_1, attack_2, defence_1, defence_2, ini_1, ini_2, acube_1, decube_1, incube_1, acube_2, decube_2, incube_2, player1, player2)
    mukatra = m
    ingens = i
    use_sword_2 = s
    use_helmet_1 = h
    new_hit, axe = player2_get_axe(new_hit, axe_2, player2)
    new_hit = get_ninos(pd, new_hit)
    axe_2 = axe
    if new_hit > 0 and shield_1 == 1:
        new_hit, shield = player1_get_shield(new_hit, shield_1, player1)
        shield_1 = shield
    get_valerius_2(new_hit)
    print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
    a, d, i = player1_consequences(new_hit, attack_1, defence_1, ini_1, player1)
    attack_1 = a
    defence_1 = d
    ini_1 = i
    acube_1 = attack_1 * '🟥 '
    decube_1 = defence_1 * '🟫 '
    incube_1 = ini_1 * '🟦 '
    attack_2, defence_2, ini_2 = get_alard(pd, attack_2, defence_2, ini_2, acube_1, decube_1, incube_1, player1, player2)
    return attack_1, defence_1, ini_1, attack_2, defence_2, ini_2, ingens, mukatra, use_sword_2, use_helmet_1, axe_2, shield_1

