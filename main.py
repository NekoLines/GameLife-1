import time, os,  random


def print_list(lst, stop=True):
    for i in lst:
        print(*i)
    time.sleep(0.1)
    if stop:
        os.system('clear')


def neighbours(m, i, j, animal):
    output = [m[x][y] for x in [i-1,i,i+1] for y in [j-1,j,j+1] if x in range(0,len(m)) and y in range(0,len(m[x])) and (x,y) != (i,j)]
    res = 0
    for i in output:
        if i == animal:
            res += 1
    return res


shrimp = '🦐 '
fish = '🐟 '
wall = '🧱 '
nothing = '💦 '
items = [shrimp, fish, wall, nothing]

length = random.randint(1, 45)
width = random.randint(1, 45)

field = [[random.choice(items) for _ in range(width)] for __ in range(length)]

os.system('clear')


while True:
    for i in range(length):
        for j in range(width):
            if field[i][j] == fish:
                if neighbours(field, i, j, fish) < 2 or neighbours(field, i, j, fish) >= 4:
                    field[i][j] = nothing
            elif field[i][j] == shrimp:
                if neighbours(field, i, j, shrimp) < 2 or neighbours(field, i, j, shrimp) >= 4:
                    field[i][j] = nothing
            elif field[i][j] == nothing:
                if neighbours(field, i, j, shrimp) == 3:
                    field[i][j] = shrimp
                elif neighbours(field, i, j, fish) == 3:
                    field[i][j] = fish
    print_list(field)
    os.system('clear')
