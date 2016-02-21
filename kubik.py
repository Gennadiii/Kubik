from random import randint
hod = None
number_of_players = int( input('Input number of players: ') )
players = ['x' for x in range(number_of_players)]
for j in range(number_of_players):
    players[j] = {
        'name': input('Name of player ' + str(j+1) + ' :'),
        'skip_next_move': False
    }

move = 0
while True:
    if players[move%number_of_players]['skip_next_move']:
        players[move%number_of_players]['skip_next_move'] = False
        move += 1
        continue
    hod = randint(1,6)
    print( players[move%number_of_players]['name'] + ' - ' + str(hod) )
    move_result = input()
    if move_result == '-': players[move%number_of_players]['skip_next_move'] = True
    if move_result == '+': move -= 1
    move += 1
