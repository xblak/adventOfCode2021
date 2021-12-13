def parseline(s:str) -> [int,int,int,int]:
    import re
    # split by ',' or ' -> ', return x1, y1, x2, y2
    arr = re.split(',| -> ', s)
    return int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3])


def drawLineP1(map:dict, x1:int, y1:int, x2:int, y2:int):
    # only drawing straight lines when x1 == x2 or y1 == y2
    if x1 == x2:
        if y1 > y2:
            # not sure if this is a good way to swap value lol
            y1, y2 = y2, y1
        for i in range(y1, y2+1):
            key = str(x1) + ',' + str(i)
            map.update({key: map.get(key, 0)+1})
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2+1):
            key = str(i) + ',' + str(y1)
            map.update({key: map.get(key, 0) + 1})


def drawLineP2(map:dict, x1:int, y1:int, x2:int, y2:int):
    # only drawing diagonal lines
    if x1 == x2 or y1 == y2:
        return
    dy = 1
    # always go from left to right (x), y need to swap at the same time
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    if y1 > y2:
        dy = -1
    for i in range(x1, x2+1):
        key = str(i) + ',' + str(y1)
        y1 += dy
        map.update({key: map.get(key, 0) + 1})

if __name__ == '__main__':
    with open("input05.txt") as f:
        map = {}
        count = 0
        for line in f:
            x1, y1, x2, y2 = parseline(line.strip())
            drawLineP1(map, x1, y1, x2, y2)
        for i in map.values():
            if i >= 2:
                count += 1
        print(count,len(map))

    with open("input05.txt") as f:
        # probably don't need to iterate the file twice
        # one potential solution is use two dicts,
        # one dict for straight line only, the other one for both
        # another way is to save the diagonal line into a list, draw them in the end (better)
        count = 0
        for line in f:
            x1, y1, x2, y2 = parseline(line.strip())
            drawLineP2(map, x1, y1, x2, y2)
        for i in map.values():
            if i >= 2:
                count += 1
        print(count, len(map))
