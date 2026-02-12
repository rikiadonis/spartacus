from gladiator_statistics import gladiator1_special, gladiator2_special

def gannikus_hit(pa, pd):
    special_1 = gladiator1_special()
    special_2 = gladiator2_special()
    hit = 0
    if len(pa) == 1 and len(pd) == 1:
        if pa[0] >= pd[0]:
            hit += 1
    if len(pa) == 1 and len(pd) == 5:
        if pa[0] >= pd[0]:
            hit += 1
    elif len(pa) == 1 and len(pd) == 4:
        if pa[0] >= pd[0]:
            hit += 1
        if special_1 == 'kriksos' or special_2 == 'kriksos':
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
        if pa[0] >= pd[0]:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 1 and len(pd) == 2:
        if pa[0] >= pd[0]:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 2 and len(pd) == 1:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
    elif len(pa) == 2 and len(pd) == 5:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
    elif len(pa) == 2 and len(pd) == 4:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
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
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 2 and len(pd) == 2:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if special_2 == 'kriksos' or special_1 != 'oinomaos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 3 and len(pd) == 1:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
    elif len(pa) == 3 and len(pd) == 2:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 3 and len(pd) == 5:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] >= pd[2]:
            hit += 1
    elif len(pa) == 3 and len(pd) == 4:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] >= pd[2]:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
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
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] >= pd[2]:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 4 and len(pd) == 1:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] > 2:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
    elif len(pa) == 4 and len(pd) == 2:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] > 2:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
    elif len(pa) == 4 and len(pd) == 3:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] >= pd[2]:
            hit += 1
        if pa[3] > 2:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
            unique = []
            for i in pd:
                if i not in unique:
                    unique.append(i)
            if len(unique) == 1:
                hit -= 1
            if len(unique) == 2:
                hit -= 1
    elif len(pa) == 4 and len(pd) == 5:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] >= pd[2]:
            hit += 1
        if pa[3] >= pd[3]:
            hit += 1
    elif len(pa) == 4 and len(pd) == 4:
        if pa[0] >= pd[0]:
            hit += 1
        if pa[1] >= pd[1]:
            hit += 1
        if pa[2] >= pd[2]:
            hit += 1
        if pa[3] >= pd[3]:
            hit += 1
        if special_2 == 'kriksos' or special_1 == 'kriksos':
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
