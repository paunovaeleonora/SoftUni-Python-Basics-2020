men = int(input())
women = int(input())
max_count_tables = int(input())
sitting = 0
is_full = False

for man in range(1, men + 1):
    if is_full:
        break
    for woman in range(1, women + 1):
        print(f'({man} <-> {woman}) ', end='')
        sitting += 1
        if sitting == max_count_tables:
            is_full = True
            break

