import numpy as np


def getSumRishLevel(heightmap):
    sum = 0
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            val = int(heightmap[x][y])
            # check if val is lower than all adjacent
            if (isHigherPoint(val, x + 1, y, heightmap) and
                    isHigherPoint(val, x - 1, y, heightmap) and
                    isHigherPoint(val, x, y + 1, heightmap) and
                    isHigherPoint(val, x, y - 1, heightmap)):
                sum += val + 1
    return sum


def isNotInBound(x, y, heightmap):
    return x < 0 or x >= len(heightmap) or y < 0 or y >= len(heightmap[x])


def isHigherPoint(val, x, y, heightmap):
    return isNotInBound(x, y, heightmap) or val < int(heightmap[x][y])


def isPartOfBasin(x, y, heightmap, visited) -> int:
    # stop if not in bound or visited
    if isNotInBound(x, y, heightmap) or visited[x][y]:
        return 0
    else:
        visited[x][y] = True
        # if < 9 means a connected valid basin
        # return 1 + all four directions, dfs
        if int(heightmap[x][y]) < 9:
            return 1 + (isPartOfBasin(x + 1, y, heightmap, visited) +
                        isPartOfBasin(x - 1, y, heightmap, visited) +
                        isPartOfBasin(x, y + 1, heightmap, visited) +
                        isPartOfBasin(x, y - 1, heightmap, visited))
    return 0


def getProdBasin(heightmap):
    # list to store all basin size
    allbasin = []
    row = len(heightmap)
    col = len(heightmap[0])
    # np zeros is easier
    # visited = [[False] * col for i in range(row)]
    visited = np.zeros((row, col))
    # go over the matrix
    for x in range(row):
        for y in range(col):
            allbasin.append(isPartOfBasin(x, y, heightmap, visited))
    # we only need 3 largest, priority queue or k largest should be better
    allbasin.sort(reverse=True)
    return np.prod(allbasin[:3])


if __name__ == '__main__':
    with open("input9.txt") as f:
        heightmap = []
        for line in f:
            heightmap.append(line.strip())
        print(getSumRishLevel(heightmap))
        print(getProdBasin(heightmap))
