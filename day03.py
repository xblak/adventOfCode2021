def binaryDiagP1():
    with open("input03.txt") as f:
        sum = []
        half = 0
        for line in f:
            half += 0.5
            line = line.strip()
            if len(sum) == 0:
                sum = [0] * len(line)
            for i in range (0, len(line)):
                sum[i] += int(line[i])
        gamma = ''
        epsi = ''
        for i in sum:
            if i > half:
                gamma += '1'
                epsi += '0'
            else:
                gamma += '0'
                epsi += '1'
        powerCons = int(gamma, 2) * int(epsi, 2)
        print(powerCons)

def binaryDiagP2():
    with open("input03.txt") as f:
        numstring = []
        for line in f:
            numstring.append(line.strip())
        liftSupRating = int(findRating(numstring, 0), 2) * int(findRating(numstring, 1), 2)
        print(liftSupRating)

def findMostCommon(numstring: list, index: int) -> int:
    count = 0
    for i in numstring:
        count += 0.5 - int(i[index])
    if count <= 0:
        return 1
    else:
        return 0

def findRating(numstring: list, type: int) -> str:
    import copy
    list = copy.deepcopy(numstring)
    for i in range (0, len(list[0])):
        common = findMostCommon(list, i)
        if type == 0:
            list = [j for j in list if int(j[i]) == common]
        else:
            list = [j for j in list if int(j[i]) != common]
        if len(list) == 1:
            return list[0]
    print(list)
    return list[0]


if __name__ == '__main__':
    binaryDiagP1()
    binaryDiagP2()