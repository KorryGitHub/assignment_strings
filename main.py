# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_0 = "Ruud Gullit "
player_1 = "Marco van Basten "

goal_0 = 32
goal_1 = 54 

scorers = player_0 + str(goal_0) + ", " + player_1 + str(goal_1)

report ="{}scored in the {}nd minute \n{}scored in the {}th minute".format(player_0, goal_0, player_1, goal_1)
print(report)

player = "Frank Rijkaard"
first_name = player[:player.find(" ")] 

last_name_len = len(player[player.find(" ")+1:])

name_short = player[0] + '. ' + player[player.find(" ")+1:] 

chant = (first_name + '!') * len(first_name)

good_chant= chant [-1] != ' ' 