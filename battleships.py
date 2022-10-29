# batttles ships game

import random

def where(a):
    coords = input(a +'\n')
    coord1 = int(coords[:coords.find(',')])
    coord2 = int(coords[coords.find(',')+1:])
    coords = [coord1,coord2]
    return coords

def dead(ship):
    a = grid1.index(ship)
    grid1[a] =  'BOOM'   

def dead1(ship):
    a = grid2.index(ship)
    del grid2[a]   

def miss(cd):
    a = grid1.index(cd)
    grid1[a] = 'MISS'

grid1 = []
for i in range(4):
    for o in range(4):
        grid1.append([i,o])

grid2 = []
for i in range(4):
    for o in range(4):
        grid2.append([i,o])

warship = random.choice(grid1)

submirine = random.choice(grid1)
while submirine == warship:
    submirine = random.choice(grid1)

gunner = random.choice(grid1)
while gunner == submirine or gunner == warship:
    gunner = random.choice(grid1)

carrier = random.choice(grid1)
while carrier == gunner or carrier == submirine or carrier == warship:
    carrier = random.choice(grid1)

speed  = random.choice(grid1)
while speed == warship or speed == submirine or speed == gunner or speed == carrier:
    speed = random.choice(grid1)

speed1 = random.choice(grid1)
while speed1 == warship or speed1 == submirine or speed1 == gunner or speed1 == carrier or speed1 == speed:
    speed1 = random.choice(grid1)

# print(warship,carrier,gunner,speed,speed1,submirine)
print('\nWelcome to battleships, there are 6 ships on the grid system which is 4x4\n')
print('Inputs are coordinates from 0-3 and 0-3, EX: 0,0 is valid to 3,3 is valid\n')
print('Type E to exit at any time\n')
begin = input('Begin? Y/N ')
hits = 0
aihits = 0
if begin == 'N':
    print('Oh okay...')
    quit()
print(grid1[0:4])
print(grid1[4:8])
print(grid1[8:12])
print(grid1[12:16])
print()
print('Where would you like to place your: ')
player_gunner = where('Gunner')
player_warship = where('Warship')
player_carrier = where('Carrier')
player_submirine = where('Submirine')
player_speed = where('Speed Boat')
player_speed1 = where('Speed Boat 2')
print()

while begin == 'Y':
    print('**********')
    print(grid1[0:4])
    print(grid1[4:8])
    print(grid1[8:12])
    print(grid1[12:16])
    
    player = input('\nWhere do you want to fire?: ')
    
    if player == 'E':
        begin = 'N'
    else:
        coord1 = int(player[:player.find(',')])
        coord2 = int(player[player.find(',')+1:])
        player = [coord1,coord2]
   
    # decides whether the player hit the ai or not 
    if player == warship or player == submirine or player == carrier or player == speed or player == speed1 or player == gunner:
        print('BOOM!! Nice hit!')
        hits += 1
        if player == warship:
            dead(warship) 
            print('Warship Destroyed!')
            if hits < 2:
                print(hits,'Ship Destroyed by you!\n')
            else:
                print(hits,'Ships Destroyed by you!\n')
        if player == submirine:
            dead(submirine)
            print('Submirine Destroyed!')
            if hits < 2:
                print(hits,'Ship Destroyed by you!\n')
            else:
                print(hits,'Ships Destroyed by you!\n')
        if player == gunner:
            dead(gunner)
            print('Gunner Destroyed!')
            if hits < 2:
                print(hits,'Ship Destroyed by you!\n')
            else:
                print(hits,'Ships Destroyed by you!\n')
        if player == carrier:
            dead(carrier)
            print('Carrier Destroyed!')
            if hits < 2:
                print(hits,'Ship Destroyed by you!\n')
            else:
                print(hits,'Ships Destroyed by you!\n')
        if player == speed:
            dead(speed)
            print('Speed Boat Destroyed!')
            if hits < 2:
                print(hits,'Ship Destroyed by you!\n')
            else:
                print(hits,'Ships Destroyed by you!\n')
        if player == speed1:
            dead(speed1)
            print('Speed Boat 2 Destroyed!')
            if hits < 2:
                print(hits,'Ship Destroyed by you!\n')
            else:
                print(hits,'Ships Destroyed by you!\n')
    else:
        print('Donkey! You missed!')
        if hits < 2:
            print(hits,'Ship Destroyed by you!\n')
        else:
            print(hits,'Ships Destroyed by you!\n')
        miss(player)

    if hits == 6:
        print('Well Done! You won!')
        print('GG EZ')
        quit()

    ai = random.choice(grid2)
    print('\nBot fires at', ai)

    # decides whether ai hit player or not
    if ai == player_warship or ai == player_submirine or ai == player_carrier or ai == player_speed or ai == player_speed1 or ai == player_gunner:
        print('Bot hit your ship')
        aihits += 1
        if ai == player_warship:
            dead1(player_warship)
            print('Warship Destroyed!')
            print(aihits, 'Destroyed by bot!\n')
        if ai == player_submirine:
            dead1(player_submirine)
            print('Submirine Destroyed!')
            print(aihits, 'Destroyed by bot!\n')
        if ai == player_gunner:
            dead1(player_gunner)
            print('Gunner Destroyed!')
            print(aihits, 'Destroyed by bot!\n')
        if ai == player_carrier:
            dead1(player_carrier)
            print('Carrier Destroyed!')
            print(aihits, 'Destroyed by bot!\n')
        if ai == player_speed:
            dead1(player_speed)
            print('Speed Destroyed!')
            print(aihits, 'Destroyed by bot!\n')
        if ai == player_speed1:
            dead1(player_speed1)
            print('Speed Destroyed!')
            print(aihits, 'Destroyed by bot!\n')
            
    else:
        print('Bot missed\n')
        print(aihits, 'Destroyed by bot\n')
        dead1(ai)

    if aihits == 6:
        print('You lost!')
        quit()