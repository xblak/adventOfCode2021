import numpy as np


def getSumRishLevel(heightMap):
    sum = 0
    for x in range(len(heightMap)):
        for y in range(len(heightMap[x])):
            val = int(heightMap[x][y])
            # check if val is lower than all adjacent
            if (isHigherPoint(val, x + 1, y, heightMap) and
                    isHigherPoint(val, x - 1, y, heightMap) and
                    isHigherPoint(val, x, y + 1, heightMap) and
                    isHigherPoint(val, x, y - 1, heightMap)):
                sum += val + 1
    return sum


def isNotInBound(x, y, heightMap):
    return x < 0 or x >= len(heightMap) or y < 0 or y >= len(heightMap[x])


def isHigherPoint(val, x, y, heightMap):
    return isNotInBound(x, y, heightMap) or val < int(heightMap[x][y])


def getBasinSize(x, y, heightMap, visited) -> int:
    # stop if not in bound or visited
    if isNotInBound(x, y, heightMap) or visited[x][y]:
        return 0
    else:
        visited[x][y] = True
        # if < 9 means a connected valid basin
        # return 1 + all four directions, dfs
        if int(heightMap[x][y]) < 9:
            return 1 + (getBasinSize(x + 1, y, heightMap, visited) +
                        getBasinSize(x - 1, y, heightMap, visited) +
                        getBasinSize(x, y + 1, heightMap, visited) +
                        getBasinSize(x, y - 1, heightMap, visited))
    return 0


def getProdBasin(heightMap):
    # list to store all basin size
    allBasin = []
    row = len(heightMap)
    col = len(heightMap[0])
    # np zeros is easier
    # visited = [[False] * col for i in range(row)]
    visited = np.zeros((row, col))
    # go over the matrix
    for x in range(row):
        for y in range(col):
            allBasin.append(getBasinSize(x, y, heightMap, visited))
    # we only need 3 largest, priority queue or k largest should be better
    allBasin.sort(reverse=True)
    return np.prod(allBasin[:3])


if __name__ == '__main__':
    with open("input9.txt") as f:
        heightmap = []
        for line in f:
            heightmap.append(line.strip())
        print(getSumRishLevel(heightmap))
        print(getProdBasin(heightmap))
