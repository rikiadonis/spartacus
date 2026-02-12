from gladiator_statistics import gladiator2_attack, gladiator2_defence, gladiator2_ini, gladiator1, gladiator2
import inflect
p = inflect.engine()
attack_2 = gladiator2_attack()
defence_2 = gladiator2_defence()
ini_2 = gladiator2_ini

def player2_consequences(hit, attack_2, defence_2, ini_2, player2):
    acube_2 = attack_2 * '🟥 '
    decube_2 = defence_2 * '🟫 '
    incube_2 = ini_2 * '🟦 '
    if hit <= 0:
        print(f'{player2}! The exellent defence!')
        return attack_2, defence_2, ini_2
    else:
        if hit > attack_2 + defence_2 + ini_2:
            print(f'\n{player2} has to remove {attack_2 + defence_2 + ini_2} {p.plural('cube', hit)}')
        else:
            print(f'\n{player2} has to remove {hit} {p.plural('cube', hit)}')
        print(f"What {p.plural('cube', hit)} do want to remove? ")
        print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
        while True:
            try:
                a_2 = (input('Attack:   '))
                d_2 = (input('Deffence: '))
                i_2 = (input('Speed:    '))
                if a_2 in ['0','1','2','3', '4', '5'] and d_2 in ['0','1','2','3', '4', '5'] and i_2 in ['0','1','2','3', '4', '5']:
                    a_2 = int(a_2)
                    d_2 = int(d_2)
                    i_2 = int(i_2)
                    g_attack = attack_2 - a_2
                    g_defence = defence_2 - d_2
                    g_ini = ini_2 - i_2
                    while g_attack == 0 and g_defence == 0 and g_ini == 0 or a_2 > attack_2 or d_2 > defence_2 or i_2 > ini_2 or g_attack > 1 and g_defence <= 0 and g_ini <= 0 or g_attack <= 0 and g_defence > 1 and g_ini <= 0 or g_attack <= 0 and g_defence <= 0 and g_ini > 1 or g_attack <= 0 and g_defence > 1 and g_ini > 1 or g_attack > 1 and g_defence <= 0 and g_ini > 1 or g_attack > 1 and g_defence > 1 and g_ini <= 0 or g_attack <= 0 and g_defence > 1 and g_ini >= 1 or g_attack == 0 and g_defence >= 1 and g_ini > 1 or g_attack > 1 and g_defence == 0 and g_ini >= 1 or g_attack > 1 and g_defence <= 0 and g_ini >= 1 or g_attack >= 1 and g_defence > 1 and g_ini <= 0 or g_attack > 1 and g_defence >= 1 and g_ini <= 0:
                        if g_attack == 0 and g_defence == 0 and g_ini == 0 and hit >= attack_2 + defence_2 + ini_2:
                            raise ValueError
                        a_2 = int(input('Attack:   '))
                        d_2 = int(input('Deffence: '))
                        i_2 = int(input('Speed:    '))
                        g_attack = attack_2 - a_2
                        g_defence = defence_2 - d_2
                        g_ini = ini_2 - i_2
                    if a_2 + d_2 + i_2 == hit:
                        attack_2 -= a_2
                        defence_2 -= d_2
                        ini_2 -= i_2
                        return attack_2, defence_2, ini_2
            except ValueError:
                attack_2 = 0
                defence_2 = 0
                ini_2 = 0
                return attack_2, defence_2, ini_2


def player1_consequences(hit, attack_2, defence_2, ini_2, player1):
    acube_1 = attack_2 * '🟥 '
    decube_1 = defence_2 * '🟫 '
    incube_1 = ini_2 * '🟦 '
    if hit <= 0:
        print(f'{player1}! The exellent defence!')
        return attack_2, defence_2, ini_2
    else:
        if hit > attack_2 + defence_2 + ini_2:
            print(f'\n{player1} has to remove {attack_2 + defence_2 + ini_2} {p.plural('cube', hit)}')
        else:
            print(f'\n{player1} has to remove {hit} {p.plural('cube', hit)}')
        print(f"What {p.plural('cube', hit)} do want to remove? ")
        print(f'\n{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
        while True:
            try:
                a_2 = (input('Attack:   '))
                d_2 = (input('Deffence: '))
                i_2 = (input('Speed:    '))
                if a_2 in ['0','1','2','3', '4', '5'] and d_2 in ['0','1','2','3', '4', '5'] and i_2 in ['0','1','2','3', '4', '5']:
                    a_2 = int(a_2)
                    d_2 = int(d_2)
                    i_2 = int(i_2)
                    g_attack = attack_2 - a_2
                    g_defence = defence_2 - d_2
                    g_ini = ini_2 - i_2
                    while g_attack == 0 and g_defence == 0 and g_ini == 0 or a_2 > attack_2 or d_2 > defence_2 or i_2 > ini_2 or g_attack > 1 and g_defence <= 0 and g_ini <= 0 or g_attack <= 0 and g_defence > 1 and g_ini <= 0 or g_attack <= 0 and g_defence <= 0 and g_ini > 1 or g_attack <= 0 and g_defence > 1 and g_ini > 1 or g_attack > 1 and g_defence <= 0 and g_ini > 1 or g_attack > 1 and g_defence > 1 and g_ini <= 0 or g_attack <= 0 and g_defence > 1 and g_ini >= 1 or g_attack <= 0 and g_defence >= 1 and g_ini > 1 or g_attack > 1 and g_defence <= 0 and g_ini >= 1 or g_attack > 1 and g_defence <= 0 and g_ini >= 1 or g_attack >= 1 and g_defence > 1 and g_ini <= 0 or g_attack > 1 and g_defence >= 1 and g_ini <= 0:
                        if g_attack == 0 and g_defence == 0 and g_ini == 0 and hit >= attack_2 + defence_2 + ini_2:
                            raise ValueError
                        a_2 = int(input('Attack: '))
                        d_2 = int(input('Deffence: '))
                        i_2 = int(input('Speed: '))
                        g_attack = attack_2 - a_2
                        g_defence = defence_2 - d_2
                        g_ini = ini_2 - i_2
                    if a_2 + d_2 + i_2 == hit:
                        attack_2 -= a_2
                        defence_2 -= d_2
                        ini_2 -= i_2
                        return attack_2, defence_2, ini_2
            except ValueError:
                attack_2 = 0
                defence_2 = 0
                ini_2 = 0
                return attack_2, defence_2, ini_2
