width = int(input())
length = int(input())
height = int(input())

space = width * length * height

while space > 0:
    boxes = input()
    if space > 0 and boxes == 'Done':
        print(f'{space} Cubic meters left.')
        break
    space -= int(boxes)
else:
    print(f'No more free space! You need {abs(space)} Cubic meters more.')


