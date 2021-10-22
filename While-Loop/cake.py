w = int(input())
h = int(input())

area = w * h


while area > 0:
    piece = input()
    if area > 0 and piece == "STOP":
        print(f'{area} pieces are left.')
        break
    area -= int(piece)
else:
    print(f'No more cake left! You need {abs(area)} pieces more.')
