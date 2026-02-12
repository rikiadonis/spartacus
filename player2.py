import random
def main():
    pass

def player2_attack(attack_1):
    a1 = [random.randint(1,6)]
    a2 = sorted([random.randint(1,6), random.randint(1,6)], reverse=True)
    a3 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6)], reverse=True)
    a4 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)], reverse=True)
    a5 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6),random.randint(1,6), random.randint(1,6)], reverse=True)
    if attack_1 == 1:
        pa = a1
        return pa
    elif attack_1 == 2:
        pa = a2
        return pa
    elif attack_1 == 3:
        pa = a3
        return pa
    elif attack_1 == 4:
        pa = a4
        return pa
    elif attack_1 == 5:
        pa = a5
        return pa

def player2_defence(defence_2):
    d1 = [random.randint(1,6)]
    d2 = sorted([random.randint(1,6), random.randint(1,6)], reverse=True)
    d3 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6)], reverse=True)
    d4 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)], reverse=True)
    d5 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)], reverse=True)
    if defence_2 == 1:
        pd = d1
        return pd
    elif defence_2 == 2:
        pd = d2
        return pd
    elif defence_2 == 3:
        pd = d3
        return pd
    elif defence_2 == 4:
        pd = d4
        return pd
    elif defence_2 == 5:
        pd = d5
        return pd

def player2_ini_attack(attack_1):
    a1 = [random.randint(1,6)]
    a2 = sorted([random.randint(1,6), random.randint(1,6)], reverse=True)
    a3 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6)], reverse=True)
    a4 = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)], reverse=True)
    if attack_1 == 1:
        pa = a1
        return pa
    elif attack_1 == 2:
        pa = a2
        return pa
    elif attack_1 == 3:
        pa = a3
        return pa
    elif attack_1 == 4:
        pa = a4
        return pa

if __name__=='__main__':
    main()
