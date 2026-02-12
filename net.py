from gladiator_statistics import gladiator1_add_gear, gladiator2_add_gear

def player1_get_net(net, player1, player2, ini_1, ini_2):
    ini = None
    use = None
    if len(player1) > len(player2):
        space_2 = len(player1) - len(player2)
        space_1 = 0
    elif len(player2) > len(player1):
        space_1 = len(player2) - len(player1)
        space_2 = 0
    else:
        space_1 = 0
        space_2 = 0
    incube_1 = ini_1 * '🟦 '
    incube_2 = ini_2 * '🟦 '
    if gladiator1_add_gear() == 'net' and net == 1:
        while True:
            print(f'\n{player1}{' '*space_1}: {incube_1}\n{player2}{' '*space_2}: {incube_2}')
            a = input(f'\n 🕸️  {player1}, do you want use a net? Input [y] for yes, [n] for no: ').strip().lower()
            if a == 'y':
                net = 0
                ini = 1
                use = 'y'
                return ini, use, net
            elif a == 'n':
                use = None
                return ini, use, net
    else:
        return ini, use, net

def player2_get_net(net, player1, player2, ini_1, ini_2):
    if len(player1) > len(player2):
        space_2 = len(player1) - len(player2)
        space_1 = 0
    elif len(player2) > len(player1):
        space_1 = len(player2) - len(player1)
        space_2 = 0
    else:
        space_1 = 0
        space_2 = 0
    ini = None
    use = None
    incube_1 = ini_1 * '🟦 '
    incube_2 = ini_2 * '🟦 '
    if gladiator2_add_gear() == 'net' and net == 1:
        while True:
            print(f'\n{player1}{' '*space_1}: {incube_1}\n{player2}{' '*space_2}: {incube_2}')
            a = input(f'\n 🕸️  {player2}, do you want use a net? Input [y] for yes, [n] for no: ').strip().lower()
            if a == 'y':
                use = 'y'
                net = 0
                ini = 2
                return ini, use, net
            elif a == 'n':
                use = None
                return ini, use, net
    else:
        return ini, use, net
