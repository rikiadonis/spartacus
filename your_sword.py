from gladiator_statistics import gladiator2_weapon, gladiator1_weapon
from armament import get_sword
from player_hit import player1_hit, player2_hit

def your_sword(pa, pd , hit, javelin):
    use_helmet = 0
    if gladiator1_weapon() == 'sword' and use_sword == 1:
        while True:
            if use_sword == 1:
                sword = input('Player1, do you want use a sword? ').strip().lower()
                if sword == 'y':
                    use_sword -= 1
                    pa = get_sword(pa)
                    print(f'Player1 attack:  {pa}')
                    print(f'Player2 defence: {pd}')
                    hit = player1_hit(pa, pd)
                    print(f'sword y {hit}')
                    for _ in range(hit):
                        print('SHIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    return hit, use_sword, use_helmet

    if gladiator2_weapon() == 'sword':
        while True:
            if use_sword == 1:
                sword = input('Player2, do you want use a sword? ').strip().lower()
                if sword == 'y':
                    use_sword = 0
                    pa = get_sword(pa)
                    print(f'Player2 attack:  {pa}')
                    print(f'Player1 defence: {pd}')
                    hit = player2_hit(pa, pd)
                    hit += javelin
                    print(f'hit + havelin {hit}')
                    for _ in range(hit):
                        print('SHIT!')
                    if hit <= 0:
                        print('YOU MISSED!')
                    return hit, use_sword, use_helmet
    else:
        use_sword = 0
        return hit, use_sword, use_helmet



