import numpy as np


def one_step(matrix) -> int:
    # find all == 10, flashes them(set to 0)
    # increase all adjacent by 1, unless already flashed(0)
    step_flashes = 0
    while True:
        # np.where on 2d array will return [[all x], [all y]]
        index = np.where(matrix > 9)
        # if no more to flash then break
        if len(index[0]) == 0:
            break
        step_flashes += len(index[0])
        flashes(matrix, index)
    return step_flashes


def flashes(matrix, index):
    # flashes all > 9
    for x, y in zip(index[0], index[1]):
        matrix[x][y] = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                increase(matrix, i, j)


def increase(matrix, x, y):
    # increase all adjacent by 1, unless already flashed(0), center is always 0
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return
    if matrix[x][y] != 0:
        matrix[x][y] += 1


if __name__ == '__main__':
    filename = open('input11.txt')
    matrix = []
    line = filename.readline().strip()
    while line:
        # map(function, iterable), applies the func to all items
        line = list(map(int, str(line)))
        matrix.append(line)
        line = filename.readline().strip()
    # cast to numpy array
    matrix = np.array(matrix)
    all_flashes = 0
    total_octopus = len(matrix) * len(matrix[0])
    for steps in range(100000):
        # increase all by 1
        matrix += 1
        step_flashes = one_step(matrix)
        if steps < 100:
            # count all flashes up to 100 steps
            all_flashes += step_flashes
        elif steps == 100:
            # print the counter when 100 steps
            print(all_flashes)
        if step_flashes == total_octopus:
            # all flashing at the same time!
            print(steps+1)
            break

