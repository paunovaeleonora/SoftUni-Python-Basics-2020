import math


word = input()
p = int(input())  # bank holidays
h = int(input())  # weekends travel



game_sofia = (48 - h) * (3 / 4) + (2 / 3) * p
game_province = h
result = game_sofia + game_province
if word == 'leap':
    result = result * 1.15

else:
    result = result


result = math.floor(result)

print(result)



