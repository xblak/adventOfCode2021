def findFinalScore(draw: list, matrices: list, bingoStop: int, bingoMatrix: int) -> int:
    # convert all called draw into lookup set, since it is a str set, need to cast int to str when checking
    index = draw.index(str(bingoStop))
    drawSet = set(draw[:index+1])
    # find sum of non selected numbers in the bingo matrix
    sum = 0
    for i in matrices[bingoMatrix * 5:bingoMatrix * 5 + 5]:
        for j in i:
            if str(j) not in drawSet:
                sum += j
    return sum * bingoStop


def findFirstAndLastBingo(draw: list, matrices: list) -> [int, int,int, int]:
    # return first/last bingo draw number (assume the draw has no duplicate) and matrix index
    # keep a record of index of bingo matrix
    bingoCount = set([])
    numOfMat = len(matrices) / 5
    # first 5 for counting row, last 5 for counting col
    bingo = [[0] * 10 for i in range(int(numOfMat))]
    firstBingoStop = 0
    firstBingoMatrix = 0
    for s in draw:
        # loop matrix index
        for i in range(len(matrices)):
            # no need to check bingo matrix
            curMat = int(i / 5)
            if curMat not in bingoCount:
                for j in range(len(matrices[0])):
                    # matches draw, increase bingo count on row and col
                    if matrices[i][j] == int(s):
                        bingo[curMat][i - curMat * 5] += 1
                        bingo[curMat][5 + j] += 1
                        # if bingo, add matrix index to set, save first and last bingo
                        if bingo[curMat][i - curMat * 5] == 5 or bingo[curMat][5 + j] == 5:
                            bingoCount.add(curMat)
                            if len(bingoCount) == 1:
                                firstBingoStop = int(s)
                                firstBingoMatrix = curMat
                            if len(bingoCount) == numOfMat:
                                lastBingoStop = int(s)
                                lastBingoMatrix = curMat
                                return firstBingoStop, firstBingoMatrix, lastBingoStop, lastBingoMatrix

if __name__ == '__main__':
    with open("input04.txt") as f:
        # not really the best parsing, probably should convert 'draw' from str to int list
        draw = f.readline().strip().split(',')
        from numpy import loadtxt
        input = f.readlines()
        matrices = loadtxt(input, dtype=int)
        firstBingoStop, firstBingoMatrix, lastBingoStop, lastBingoMatrix = findFirstAndLastBingo(draw, matrices)
        print(findFinalScore(draw, matrices, firstBingoStop, firstBingoMatrix))
        print(findFinalScore(draw, matrices, lastBingoStop, lastBingoMatrix))

