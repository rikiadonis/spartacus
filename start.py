import random
from initiative import get_initiative
from net import player1_get_net, player2_get_net
from filemon_and_friends import get_filemon
from gladiator_special import mukatra_ini
from pyfiglet import Figlet
d = Figlet(font='slant')

def get_start(ini_1, ini_2, ingens, mukatra, player1, player2, net_1, net_2, filemon):
    incube_1 = ini_1 * '🟦 '
    incube_2 = ini_2 * '🟦 '
    s_1, use_1, net1 = player1_get_net(net_1, player1, player2, ini_1, ini_2)
    s_2, use_2, net2 = player2_get_net(net_2, player1, player2, ini_1, ini_2)
    if use_1 == 'y' and use_2 == 'y':
        net_1 = net1
        net_2 = net2
        while True:
            cube_1 = [random.randint(1,6)]
            cube_2 = [random.randint(1,6)]
            pas = str(cube_1).strip('[').strip(']')
            pds = str(cube_2).strip('[').strip(']')
            print(f'{player1}: {pas} {incube_1}')
            print(f'{player2}: {pds} {incube_2}')
            if cube_1 > cube_2:
                initiative = 1
                return initiative, ingens, mukatra, net_1, net_2
            elif cube_2 > cube_1:
                initiative = 2
                return initiative, ingens, mukatra, net_1, net_2
    elif use_1 == 'y' and use_2 == None:
        net_1 = net1
        initiative = s_1
        return initiative, ingens, mukatra, net_1, net_2
    elif use_1 == None and use_2 == 'y':
        net_2 = net2
        initiative = s_2
        return initiative, ingens, mukatra, net_1, net_2
    elif use_1 == None and use_2 == None:
        initiative, p1, p2 = get_initiative(ini_1, ini_2, player1, player2)
        initiative, p1, p2 = get_filemon(ini_1, ini_2, p1, p2, initiative, filemon)
        initiative, m, i = mukatra_ini(p1, p2, initiative, mukatra, ingens, player1, player2)
        mukatra = m
        ingens = i
        return initiative, ingens, mukatra, net_1, net_2

