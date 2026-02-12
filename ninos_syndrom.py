from gladiator_statistics import gladiator1_special, gladiator2_special
from face_off import player2_consequences, player1_consequences
from pyfiglet import Figlet
d = Figlet(font='slant')

def get_valerius_1(hit):
    if hit >= 3 and gladiator1_special() == 'valerius' and gladiator2_special() != 'oinomaos':
        print('🪙 '*31)
        print(d.renderText(f'Player1\nyou get 1 coin.\nImmediately!'))
        print('🪙 '*31)

def get_valerius_2(hit):
    if hit >= 3 and gladiator2_special() == 'valerius' and gladiator1_special() != 'oinomaos':
        print('🪙 '*31)
        print(d.renderText(f'Player2\nyou get 1 coin.\nImmediately!'))
        print('🪙 '*31)




def get_ninos(pa, hit):
    if gladiator1_special() == 'ninos' and gladiator2_special() != 'oinomaos':
        if len(pa) == 4:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 0
                print(d.renderText('NINOSSS POWER!!!'))
                return hit
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    return hit
                else:
                    hit = 0
                    print(d.renderText('NINOSSS POWER!!!'))
                    return hit
            else:
                return hit
        if len(pa) == 3:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 0
                print(d.renderText('NINOSSS POWER!!!'))
                return hit
            else:
                return hit
        else:
            return hit
    else:
        return hit

def get_ninos2(pa, hit):
    if gladiator2_special() == 'ninos' and gladiator1_special() != 'oinomaos':
        if len(pa) == 4:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 0
                print(d.renderText('NINOSSS POWER!!!'))
                return hit
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    return hit
                else:
                    hit = 0
                    print(d.renderText('NINOSSS POWER!!!'))
                    return hit
            else:
                return hit
        if len(pa) == 3:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 0
                print(d.renderText('NINOSSS POWER!!!'))
                return hit
            else:
                return hit
        else:
            return hit
    else:
        return hit


def get_alard(pa, attack_2, defence_2, ini_2, acube_1, decube_1, incube_1, player1, player2):
    hit = 0
    if gladiator1_special() == 'alard' and gladiator2_special() != 'oinomaos':
        if len(pa) == 4:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 1
                print(d.renderText('ALARD POWER!!!'))
                print(f'{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                attack_2, defence_2, ini_2 = player2_consequences(hit, attack_2, defence_2, ini_2, player2)
                return attack_2, defence_2, ini_2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    return attack_2, defence_2, ini_2
                else:
                    hit = 1
                    print(d.renderText('ALARD POWER!!!'))
                    print(f'{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                    attack_2, defence_2, ini_2 = player2_consequences(hit, attack_2, defence_2, ini_2, player2)
                    return attack_2, defence_2, ini_2
            else:
                return attack_2, defence_2, ini_2
        if len(pa) == 3:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 1
                print(d.renderText('ALARD POWER!!!'))
                print(f'{player1}:\nATK: {acube_1}\nDEF: {decube_1}\nSPD: {incube_1}')
                attack_2, defence_2, ini_2 = player2_consequences(hit, attack_2, defence_2, ini_2, player2)
                return attack_2, defence_2, ini_2
            else:
                return attack_2, defence_2, ini_2
        else:
            return attack_2, defence_2, ini_2
    else:
        return attack_2, defence_2, ini_2


def get_alard2(pa, attack_1, defence_1, ini_1, acube_2, decube_2, incube_2, player1, player2):
    hit = 0
    if gladiator2_special() == 'alard' and gladiator1_special() != 'oinomaos':
        if len(pa) == 4:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 1
                print(d.renderText('ALARD POWER!!!'))
                print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                attack_1, defence_1, ini_1 = player1_consequences(hit, attack_1, defence_1, ini_1, player1)
                return attack_1, defence_1, ini_1
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    return attack_1, defence_1, ini_1
                else:
                    hit = 1
                    print(d.renderText('ALARD POWER!!!'))
                    print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                    attack_1, defence_1, ini_1 = player1_consequences(hit, attack_1, defence_1, ini_1, player1)
                    return attack_1, defence_1, ini_1
            else:
                return attack_1, defence_1, ini_1

        if len(pa) == 3:
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit = 1
                print(d.renderText('ALARD POWER!!!'))
                print(f'\n{player2}:\nATK: {acube_2}\nDEF: {decube_2}\nSPD: {incube_2}')
                attack_1, defence_1, ini_1 = player1_consequences(hit, attack_1, defence_1, ini_1, player1)
                return attack_1, defence_1, ini_1
            else:
                return attack_1, defence_1, ini_1
        else:
            return attack_1, defence_1, ini_1
    else:
        return attack_1, defence_1, ini_1
