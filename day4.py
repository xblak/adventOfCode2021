def giantSquidP1(draw:list,matrices:list):
    # find which draw makes first bingo, and which matrix bingo
    bingostop, bingomatrix = findBingo(draw, matrices)
    print(findFinalScore(draw, matrices, bingostop, bingomatrix))

def giantSquidP2(draw:list,matrices:list):
    bingostop, bingomatrix = findLastBingo(draw, matrices)
    print(findFinalScore(draw, matrices, bingostop, bingomatrix))

def findFinalScore(draw:list, matrices:list, bingostop:int, bingomatrix:int) -> int:
    # convert all called draw into lookup set
    index = draw.index(str(bingostop))
    drawSet = set(draw[:index])
    # find sum of non selected numbers in the bingo matrix
    sum = 0
    for i in matrices[bingomatrix * 5:bingomatrix * 5 + 5]:
        for j in i:
            if str(j) not in drawSet:
                sum += j
    # the bingostop number needs to be removed
    return (sum-bingostop)*bingostop

def findBingo(draw: list, matrices: list) -> [int,int]:
    numOfMat = len(matrices) / 5
    bingo = [[0] * 10 for i in range(int(numOfMat))]
    for s in draw:
        for i in range(len(matrices)):
            for j in range(len(matrices[0])):
                if matrices[i][j] == int(s):
                    n = int(i / 5)
                    bingo[n][i - n * 5] += 1
                    bingo[n][5 + j] += 1
                    if bingo[n][i - n * 5] == 5 or bingo[n][5 + j] == 5:
                        bingostop = int(s)
                        bingomatrix = int(i / 5)
                        return bingostop, bingomatrix

def findLastBingo(draw: list, matrices: list) -> [int,int]:
    bingocount = set([])
    numOfMat = len(matrices) / 5
    bingo = [[0] * 10 for i in range(int(numOfMat))]
    for s in draw:
        for i in range(len(matrices)):
            for j in range(len(matrices[0])):
                if matrices[i][j] == int(s):
                    n = int(i / 5)
                    bingo[n][i - n * 5] += 1
                    bingo[n][5 + j] += 1
                    if bingo[n][i - n * 5] == 5 or bingo[n][5 + j] == 5:
                        bingocount.add(n)
                        if len(bingocount) == numOfMat:
                            bingostop = int(s)
                            bingomatrix = int(i / 5)
                            return bingostop, bingomatrix

if __name__ == '__main__':
    with open("input4.txt") as f:
        draw = f.readline().strip().split(',')
        from numpy import loadtxt
        input = f.readlines()
        matrices = loadtxt(input, dtype=int)
    giantSquidP1(draw,matrices)
    giantSquidP2(draw,matrices)