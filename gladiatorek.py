def gladiatorek1():
    print('''
    g - switch the player who won the initiative
    m - move
    a - attack(Prepare to strike: -> y/n)
    j - javelin attack
    p - pass, after move or attack
    2x p - end turn
    e - end turn
      ''')
    while True:
        my_gladiator_2 = input(f'\n{'🧝  '} Gladiator no. 1: ').lower().strip()
        print()
        if my_gladiator_2 == 'oin' or my_gladiator_2 == 'oinomaos':
            player2 = 'oin'
            return player2
        elif my_gladiator_2 == 'syr' or my_gladiator_2 == 'syryjski wojownik':
            player2 = 'syr'
            return player2
        elif my_gladiator_2 == 'gal' or my_gladiator_2 == 'galijski wojownik':
            player2 = 'gal'
            return player2
        elif my_gladiator_2 == 'tra' or my_gladiator_2 == 'tracki wojownik':
            player2 = 'tra'
            return player2
        elif my_gladiator_2 == 'muk' or my_gladiator_2 == 'mukatra':
            player2 = 'muk'
            return player2
        elif my_gladiator_2 == 'ing' or my_gladiator_2 == 'ingens':
            player2 = 'ing'
            return player2
        elif my_gladiator_2 == 'gne' or my_gladiator_2 == 'gnejusz':
            player2 = 'gne'
            return player2
        elif my_gladiator_2 == 'val' or my_gladiator_2 == 'valerius':
            player2 = 'val'
            return player2
        elif my_gladiator_2 == 'nin' or my_gladiator_2 == 'ninos':
            player2 = 'nin'
            return player2
        elif my_gladiator_2 == 'ala' or my_gladiator_2 == 'alard':
            player2 = 'ala'
            return player2
        elif my_gladiator_2 == 'kak' or my_gladiator_2 == 'kakus':
            player2 = 'kak'
            return player2
        elif my_gladiator_2 == 'ter' or my_gladiator_2 == 'teron':
            player2 = 'ter'
            if my_gladiator_2 == 'ter':
                print(f'Attention! The program accepted "{my_gladiator_2}" as Teron.\n')
            return player2
        elif my_gladiator_2 == 'spa' or my_gladiator_2 == 'spartakus':
            player2 = 'spa'
            return player2
        elif my_gladiator_2 == 'kri' or my_gladiator_2 == 'kriksos':
            player2 = 'kri'
            return player2
        elif my_gladiator_2 == 'gan' or my_gladiator_2 == 'gannikus':
            player2 = 'gan'
            return player2
        elif my_gladiator_2 == 'fil' or my_gladiator_2 == 'filemon':
            player2 = 'fil'
            return player2
        elif my_gladiator_2 == 'dan' or my_gladiator_2 == 'danel':
            player2 = 'dan'
            return player2
        elif my_gladiator_2 == 'asz' or my_gladiator_2 == 'aszur':
            player2 = 'asz'
            return player2
        elif my_gladiator_2 == 'dur' or my_gladiator_2 == 'duro':
            player2 = 'dur'
            return player2
        elif my_gladiator_2 == 'cae' or my_gladiator_2 == 'caenis':
            player2 = 'cae'
            return player2
        elif my_gladiator_2 == 'aur' or my_gladiator_2 == 'aureola':
            player2 = 'cae'
            return player2
        elif my_gladiator_2 == 'apt' or my_gladiator_2 == 'aptekarz':
            player2 = 'apt'
            return player2
        elif my_gladiator_2 == 'med' or my_gladiator_2 == 'medyk':
            player2 = 'med'
            return player2
        elif my_gladiator_2 == 'cra' or my_gladiator_2 == 'cratusa':
            player2 = 'cra'
            return player2
        elif my_gladiator_2 == 'sym' or my_gladiator_2 == 'symbiusa':
            player2 = 'sym'
            return player2
        elif my_gladiator_2 == 'aga' or my_gladiator_2 == 'agapetus':
            player2 = 'aga'
            return player2
        elif my_gladiator_2 == 'gly' or my_gladiator_2 == 'glyptus':
            player2 = 'gly'
            return player2
        elif my_gladiator_2 == 'egl' or my_gladiator_2 == 'eglectus':
            player2 = 'egl'
            return player2
        elif my_gladiator_2 == 'mel' or my_gladiator_2 == 'mellusa':
            player2 = 'mel'
            return player2
        elif my_gladiator_2 == 'dez' or my_gladiator_2 == 'dezerter':
            player2 = 'dez'
            return player2
        elif my_gladiator_2 == 'slu' or my_gladiator_2 == 'sluga' or my_gladiator_2 == 'sługa':
            player2 = 'slu'
            return player2
        elif my_gladiator_2 == 'ska' or my_gladiator_2 == 'skazaniec':
            player2 = 'ska'
            return player2
        elif my_gladiator_2 == 'zam' or my_gladiator_2 == 'zamaskowana kurtyzana':
            player2 = 'zam'
            return player2
        elif my_gladiator_2 == 'ant' or my_gladiator_2 == 'antusa':
            player2 = 'ant'
            return player2
        elif my_gladiator_2 == 'terp' or my_gladiator_2 == 'terpusa':
            player2 = 'terp'
            return player2
        elif my_gladiator_2 == 'pri' or my_gladiator_2 == 'pristus':
            player2 = 'pri'
            return player2
        elif my_gladiator_2 == 'chr' or my_gladiator_2 == 'chrestus':
            player2 = 'chr'
            return player2
        elif my_gladiator_2 == 'lal' or my_gladiator_2 == 'laletus':
            player2 = 'lal'
            return player2
        else:
            print("Write the full name or first three letters of the warrior from your card\n")


def weaponek1():
    while True:
        my_weapon = input(f"{'⚔️  '} Galadiator's weapon no. 1: ").lower().strip()
        print()
        if my_weapon == 'm' or my_weapon == 'miecz':
            weapon = 'sword'
            return weapon
        elif my_weapon == 't' or  my_weapon == 'topór' or my_weapon == 'topor':
            if my_weapon == 't':
                print(f'Attention! The program accepted "{my_weapon}" as Topór.\n')
            weapon = 'axe'
            return weapon
        elif my_weapon == 'trójząb' or my_weapon == 'tro' or my_weapon == 'none' or my_weapon == 'trojzab' or my_weapon == 'n':
            weapon = ''
            return weapon
        else:
            print("Write the full name or first letter of the weapon from your weapon's card, or 'None' or 'N', if you don't have it.\n")



def armorek1():
    while True:
        my_armor = input(f"{'🛡️  '} Galadiator's armor no. 1 ").lower().strip()
        print()
        if my_armor == 'h' or my_armor == 'helm' or my_armor == 'hełm':
            armor = 'helmet'
            return armor
        elif my_armor == 't' or my_armor == 'tarcza':
            armor = 'shield'
            return armor
        elif my_armor == 'none' or my_armor == 'n':
            armor = ''
            return armor
        else:
            print("Write the full name or first letter of the armor from your armor's card, or 'None' or 'N', if you don't have it.\n")

def specialek1():
    while True:
        my_special = input(f"{'🕸️  '} Galadiator's special no. 1: ").lower().strip()
        print()
        if my_special == 'sieć' or my_special == 's' or my_special == 'siec':
            special = 'net'
            return special
        elif my_special == 'oszczep' or my_special == 'o':
            special = 'javelin'
            return special
        elif my_special == 'none' or my_special == 'n':
            special = ''
            return special
        else:
            print("Write the full name or first letter of the special from your special's card, or 'None' or 'N', if you don't have it.\n")



def gladiatorek2():
    while True:
        my_gladiator_2 = input(f'\n\n{'🧝  '} Gladiator no. 2: ').lower().strip()
        print()
        if my_gladiator_2 == 'oin' or my_gladiator_2 == 'oinomaos':
            player2 = 'oin'
            return player2
        elif my_gladiator_2 == 'syr' or my_gladiator_2 == 'syryjski wojownik':
            player2 = 'syr'
            return player2
        elif my_gladiator_2 == 'gal' or my_gladiator_2 == 'galijski wojownik':
            player2 = 'gal'
            return player2
        elif my_gladiator_2 == 'tra' or my_gladiator_2 == 'tracki wojownik':
            player2 = 'tra'
            return player2
        elif my_gladiator_2 == 'muk' or my_gladiator_2 == 'mukatra':
            player2 = 'muk'
            return player2
        elif my_gladiator_2 == 'ing' or my_gladiator_2 == 'ingens':
            player2 = 'ing'
            return player2
        elif my_gladiator_2 == 'gne' or  my_gladiator_2 == 'gnejusz':
            player2 = 'gne'
            return player2
        elif my_gladiator_2 == 'val' or my_gladiator_2 == 'valerius':
            player2 = 'val'
            return player2
        elif my_gladiator_2 == 'nin' or my_gladiator_2 == 'ninos':
            player2 = 'nin'
            return player2
        elif my_gladiator_2 == 'ala' or my_gladiator_2 == 'alard':
            player2 = 'ala'
            return player2
        elif my_gladiator_2 == 'kak' or my_gladiator_2 == 'kakus':
            player2 = 'kak'
            return player2
        elif my_gladiator_2 == 'ter' or my_gladiator_2 == 'teron':
            player2 = 'ter'
            if my_gladiator_2 == 'ter':
                print(f'Attention! The program accepted "{my_gladiator_2}" as Teron.\n')
            return player2
        elif my_gladiator_2 == 'spa' or my_gladiator_2 == 'spartakus':
            player2 = 'spa'
            return player2
        elif my_gladiator_2 == 'kri' or my_gladiator_2 == 'kriksos':
            player2 = 'kri'
            return player2
        elif my_gladiator_2 == 'gan' or my_gladiator_2 == 'gannikus':
            player2 = 'gan'
            return player2
        elif my_gladiator_2 == 'fil' or my_gladiator_2 == 'filemon':
            player2 = 'fil'
            return player2
        elif my_gladiator_2 == 'dan' or my_gladiator_2 == 'danel':
            player2 = 'dan'
            return player2
        elif my_gladiator_2 == 'asz' or my_gladiator_2 == 'aszur':
            player2 = 'asz'
            return player2
        elif my_gladiator_2 == 'dur' or my_gladiator_2 == 'duro':
            player2 = 'dur'
            return player2
        elif my_gladiator_2 == 'cae' or my_gladiator_2 == 'caenis':
            player2 = 'cae'
            return player2
        elif my_gladiator_2 == 'aur' or my_gladiator_2 == 'aureola':
            player2 = 'cae'
            return player2
        elif my_gladiator_2 == 'apt' or my_gladiator_2 == 'aptekarz':
            player2 = 'apt'
            return player2
        elif my_gladiator_2 == 'med' or my_gladiator_2 == 'medyk':
            player2 = 'med'
            return player2
        elif my_gladiator_2 == 'cra' or my_gladiator_2 == 'cratusa':
            player2 = 'cra'
            return player2
        elif my_gladiator_2 == 'sym' or my_gladiator_2 == 'symbiusa':
            player2 = 'sym'
            return player2
        elif my_gladiator_2 == 'aga' or my_gladiator_2 == 'agapetus':
            player2 = 'aga'
            return player2
        elif my_gladiator_2 == 'gly' or my_gladiator_2 == 'glyptus':
            player2 = 'gly'
            return player2
        elif my_gladiator_2 == 'egl' or my_gladiator_2 == 'eglectus':
            player2 = 'egl'
            return player2
        elif my_gladiator_2 == 'mel' or my_gladiator_2 == 'mellusa':
            player2 = 'mel'
            return player2
        elif my_gladiator_2 == 'dez' or my_gladiator_2 == 'dezerter':
            player2 = 'dez'
            return player2
        elif my_gladiator_2 == 'slu' or my_gladiator_2 == 'sluga' or my_gladiator_2 == 'sługa':
            player2 = 'slu'
            return player2
        elif my_gladiator_2 == 'ska' or my_gladiator_2 == 'skazaniec':
            player2 = 'ska'
            return player2
        elif my_gladiator_2 == 'zam' or my_gladiator_2 == 'zamaskowana kurtyzana':
            player2 = 'zam'
            return player2
        elif my_gladiator_2 == 'ant' or my_gladiator_2 == 'antusa':
            player2 = 'ant'
            return player2
        elif my_gladiator_2 == 'terp' or my_gladiator_2 == 'terpusa':
            player2 = 'terp'
            return player2
        elif my_gladiator_2 == 'pri' or my_gladiator_2 == 'pristus':
            player2 = 'pri'
            return player2
        elif my_gladiator_2 == 'chr' or my_gladiator_2 == 'chrestus':
            player2 = 'chr'
            return player2
        elif my_gladiator_2 == 'lal' or my_gladiator_2 == 'laletus':
            player2 = 'lal'
            return player2



        else:
            print("Write the full name or first three letters of the warrior from your card\n")

def weaponek2():
    while True:
        my_weapon_2 = input(f"{'⚔️  '} Galadiator's weapon no. 2: ").lower().strip()
        print()
        if my_weapon_2 == 'm' or my_weapon_2 == 'miecz':
            weapon = 'sword'
            return weapon
        elif my_weapon_2 == 't' or my_weapon_2 == 'topor':
            if my_weapon_2 == 't':
                print(f'Attention! The program accepted "{my_weapon_2}" as Topór.\n')
            weapon = 'axe'
            return weapon
        elif my_weapon_2 == 't' or my_weapon_2 == 'trojzab' or my_weapon_2 == 'trójząb'  or my_weapon_2 == 'tro' or my_weapon_2 == 'none' or my_weapon_2 == 'n':
            weapon = ''
            return weapon
        else:
            print("Write the full name or first letter of the weapon from your weapon's card or 'None' or 'N', if you don't have it\n")



def armorek2():
    while True:
        my_armor_2 = input(f"{'🛡️  '} Galadiator's armor no. 2: ").lower().strip()
        print()
        if my_armor_2 == 'h' or my_armor_2 == 'helm' or my_armor_2 == 'hełm':
            armor = 'helmet'
            return armor
        elif my_armor_2 == 't' or my_armor_2 == 'tarcza':
            armor = 'shield'
            return armor
        elif my_armor_2 == 'none' or my_armor_2 == 'n':
            armor = ''
            return armor
        else:
            print("Write the full name or first letter of the armor from your armor's card or 'None' or 'N', if you don't have it.\n")

def specialek2():
    while True:
        my_special_2 = input(f"{'🕸️  '} Galadiator's special no. 2: ").lower().strip()
        print()
        if my_special_2 == 'sieć' or my_special_2 == 's' or my_special_2 == 'siec':
            special = 'net'
            return special
        elif my_special_2 == 'oszczep' or my_special_2 == 'o':
            special = 'javelin'
            return special
        elif my_special_2 == 'none' or my_special_2 == 'n':
            special = ''
            return special
        else:
            print("Write the full name or first letter of the special from your special's card, or 'None' or 'N', if you don't have it.\n")



