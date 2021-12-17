def fold_once(all_dots, fold):
    val = int(fold[2:])
    if fold[0] == 'x':
        # size of the set has to be unchanged during iteration,
        # so we iterate a deep copy instead
        for dot in all_dots.copy():
            if dot[0] > val:
                # new location = val - (dot[0] - val)
                # remove old tuple(immutable), add the folded one back
                x = 2 * val - dot[0]
                y = dot[1]
                all_dots.remove(dot)
                all_dots.add((x, y))
    else:
        for dot in all_dots.copy():
            if dot[1] > val:
                x = dot[0]
                y = 2 * val - dot[1]
                all_dots.remove(dot)
                all_dots.add((x, y))
    print(len(all_dots))


def draw_the_dots(all_dots):
    # print the result
    maxY = 0
    maxX = 0
    for dot in all_dots:
        maxY = max(maxY, dot[1])
        maxX = max(maxX, dot[0])
    # +1 for inclusion
    for y in range(maxY+1):
        for x in range(maxX+1):
            if (x, y) in all_dots:
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    with open("input13.txt") as f:
        all_dots = set()
        for line in f:
            line = line.strip()
            if line.startswith('fold'):
                fold_once(all_dots, line.split(' ')[2])
            elif line:  # check if line is not empty
                dot = tuple(map(int, line.split(',')))
                all_dots.add(dot)
        draw_the_dots(all_dots)
