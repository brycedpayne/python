player_stats = 25

print('\nYou have {} skill points.  Use them wisely!'.format(player_stats))
print('You must distribute your skills between attack and healing')

player_attack = input('\nHow strong of an attack would you like? ')
player_stats -= int(player_attack)
print('You have {} skill points remaining'.format(player_stats))
player_heal = input('\nHow strong of healing would you like? ')

player = {'name': 'Bryce', 'attack': int(player_attack), 'heal': int(player_heal), 'health': 100}
monster = {'name': 'Monster', 'attack': 12, 'health': 100}

print(player)