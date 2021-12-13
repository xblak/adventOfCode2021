import numpy as np
def naivesolution():
    from numpy import loadtxt
    fishes = loadtxt("input06.txt", dtype=int, delimiter=',')
    days = 80
    for _ in range(days):
        fishes -= 1
        newfish = 0
        for i in range(len(fishes)):
            if fishes[i] == -1:
                fishes[i] = 6
                newfish += 1
        fishes = np.append(fishes, [8] * newfish)
        print(fishes)
    print(len(fishes))

def anotherday(map):
    # fishes have 0 day produce new fishes
    newfish = map[0]
    # move all fishes to one less day
    for i in range(len(map)-1):
        map[i] = map[i+1]
    map[8] = newfish
    map[6] += newfish
    print(map)

def countfish(map):
    # count total fishes in the map
    sum = 0
    for fish in map:
        sum += fish
    return sum

if __name__ == '__main__':
    # naivesolution()
    with open("input06.txt") as f:
        fishes = f.readline().strip().split(',')
        map = [0] * 9
        for fish in fishes:
            map[int(fish)] += 1
        for _ in range(256):
            anotherday(map)
        print(countfish(map))