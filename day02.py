def diveP1():
    hori = 0
    depth = 0
    with open("input02.txt") as f:
        for line in f:
            a = line.rstrip().split()
            if a[0] == 'forward':
                hori += int(a[1])
            elif a[0] == 'up':
                depth -= int(a[1])
            else:
                depth += int(a[1])
    print(hori * depth)

def diveP2():
    hori = 0
    aim = 0
    depth = 0
    with open("input02.txt") as f:
        for line in f:
            a = line.rstrip().split()
            if a[0] == 'forward':
                hori += int(a[1])
                depth += aim * int(a[1])
            elif a[0] == 'up':
                aim -= int(a[1])
            else:
                aim += int(a[1])
    print(hori * depth)

if __name__ == '__main__':
    diveP1()
    diveP2()