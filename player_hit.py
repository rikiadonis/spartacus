from gladiator_statistics import gladiator1_special, gladiator2_special

def main():
    pa = 1
    pd = 2
    dup = player1_hit(pa, pd)

def player1_hit_ini(pa, pd):
    special_1 = gladiator1_special()
    special_2 = gladiator2_special()
    hit = 0
    if len(pa) == 1 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
    if len(pa) == 1 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
    elif len(pa) == 1 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1


    elif len(pa) == 1 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        pd[1]
        pd[2]
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 2 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1

    elif len(pa) == 2 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1

    elif len(pa) == 2 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1


    elif len(pa) == 2 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        pd[1]
        pd[2]
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 2 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1

    elif len(pa) == 3 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1

    elif len(pa) == 3 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        pd[3]
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1


    elif len(pa) == 3 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1

    elif len(pa) == 4 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1

    elif len(pa) == 4 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1
    return hit

def player2_hit_ini(pa, pd):
    special_1 = gladiator2_special()
    special_2 = gladiator1_special()
    hit = 0
    if len(pa) == 1 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
    if len(pa) == 1 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
    elif len(pa) == 1 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        pd[1]
        pd[2]
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
    elif len(pa) == 2 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1

    elif len(pa) == 2 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1

    elif len(pa) == 2 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 2 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 2 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1

    elif len(pa) == 3 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1

    elif len(pa) == 3 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        pd[3]
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1

    elif len(pa) == 4 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1

    elif len(pa) == 4 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1
    return hit

def player1_hit(pa, pd):
    special_1 = gladiator1_special()
    special_2 = gladiator2_special()
    hit = 0
    if len(pa) == 1 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
    if len(pa) == 1 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
    elif len(pa) == 1 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 2 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
    elif len(pa) == 2 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1

    elif len(pa) == 2 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 2 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 2 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1

    elif len(pa) == 3 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1
            if special_2 == 'kriksos' and special_1 != 'oinomaos':
                unique = []
                for i in pd:
                    if i not in unique:
                        unique.append(i)
                if len(unique) == 1:
                    hit -= 1

    elif len(pa) == 3 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1

    elif len(pa) == 3 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 4 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1

    elif len(pa) == 4 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1
            if special_2 == 'kriksos' and special_1 != 'oinomaos':
                unique = []
                for i in pd:
                    if i not in unique:
                        unique.append(i)
                if len(unique) == 1:
                    hit -= 1


    elif len(pa) == 4 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit += 1
            if len(unique) == 3:
                hit += 1

    elif len(pa) == 4 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 5 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if pa[4] > 2:
            hit += 1
    elif len(pa) == 5 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if pa[4] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 5 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if pa[4] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 5 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if pa[4] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 5 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if pa[4] > pa[4]:
            hit += 1

    return hit



def player2_hit(pa, pd):
    special_1 = gladiator2_special()
    special_2 = gladiator1_special()
    hit = 0
    if len(pa) == 1 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
    elif len(pa) == 1 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
    elif len(pa) == 1 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 2 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1

    elif len(pa) == 2 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1

    elif len(pa) == 2 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 2 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 2 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1

    elif len(pa) == 3 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1

    elif len(pa) == 3 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 3 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 1
            if len(unique) == 2:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 4 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1

    elif len(pa) == 4 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1

    elif len(pa) == 4 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit += 1
            if len(unique) == 3:
                hit += 1

    elif len(pa) == 4 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if special_1 == 'spartacus' and special_2 != 'oinomaos':
            unique = []
            for i in pa:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit += 2
            if len(unique) == 2:
                if pa[0] == pa[1] and pa[2] == pa[3]:
                    hit += 2
                else:
                    hit +=1
            if len(unique) == 3:
                hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1

    elif len(pa) == 5 and len(pd) == 1:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if pa[4] > 2:
            hit += 1
    elif len(pa) == 5 and len(pd) == 2:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if pa[4] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1

    elif len(pa) == 5 and len(pd) == 3:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if pa[4] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 5 and len(pd) == 4:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if pa[4] > 2:
            hit += 1
        if special_2 == 'kriksos' and special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 2
            if len(unique) == 2:
                if pd[0] == pd[1] and pd[2] == pd[3]:
                    hit -= 2
                else:
                    hit -=1
            if len(unique) == 3:
                hit -= 1
    elif len(pa) == 5 and len(pd) == 5:
        if pa[0] > pd[0]:
            hit += 1
        if pa[1] > pd[1]:
            hit += 1
        if pa[2] > pd[2]:
            hit += 1
        if pa[3] > pd[3]:
            hit += 1
        if pa[4] > pa[4]:
            hit += 1
    return hit


if __name__=='__main__':
    main()
