import sys
colored_eggs = int(input())
color = 0
count_red = 0
count_orange = 0
count_blue = 0
count_green = 0
max_size = -sys.maxsize

for colored_eggs in range(1, colored_eggs +1):
    color = input()
    if color == 'red':
        count_red += 1
        if count_red > max_size:
            max_size = count_red

    if color == 'orange':
        count_orange += 1
        if count_orange > max_size:
            max_size = count_orange

    if color == 'blue':
        count_blue += 1
        if count_blue > max_size:
            max_size = count_blue

    if color == 'green':
        count_green += 1
        if count_green > max_size:
            max_size = count_green
if max_size == count_red:
    color = 'red'
elif max_size == 'orange':
    color = 'orange'
elif max_size == count_blue:
    color = 'blue'
elif max_size == count_green:
    color = 'green'

print(f'Red eggs: {count_red}')
print(f'Orange eggs: {count_orange}')
print(f'Blue eggs: {count_blue}')
print(f'Green eggs: {count_green}')
print(f'Max eggs: {max_size} -> {color}')






