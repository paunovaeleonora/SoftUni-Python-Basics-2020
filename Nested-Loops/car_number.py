start = int(input())
end = int(input())


for a in range(start, end + 1):
    for b in range(start, end + 1):
        for c in range(start, end + 1):
            for d in range(start, end + 1):
                if a % 2 == 0:
                    if d % 2 == 0:
                        continue
                else:
                    if d % 2 == 1:
                        continue
                if a < d:
                    continue
                if (b + c) % 2 == 1:
                    continue
                number = str(a) + str(b) + str(c) + str(d)
                print(f'{number} ', end='')
