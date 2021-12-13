# https://adventofcode.com/2021/day/12
# dict with all caves and it's connection (graph)
# dfs(backtrack) all possible path, use a set to keep track of visited
# return 0 if we found a dead end, return 1 if reach the end
# no CAVE is connect to CAVE in input, so infinite loop is impossible

def dfs_start(caves, question):
    sum = 0
    for cave in caves['start']:
        if question == 1:
            sum += dfs_helper(caves, cave, set)
        else:
            # Ideally, q2 should also use a set for O(1) lookup time
            # not sure what's the problem
            # I thought it's because backtracking will not have the element to remove when using twice,
            # since it's removed in the recursion.
            # But that doesn't help, still result in an infinite loop. Why??

            # Edit: found the bug right after I wrote everything above
            # it removes the cave in visited without adding one
            # in [a], add a, remove a, we still have [a], but it will be {} in set
            # so it results in visiting a small cave three times
            # fixed by not removing the cave in visited when we use the 'twice pass'
            sum += dfs_helper2(caves, cave, set, True)
    return sum


def dfs_helper(caves, cur_cave, visited):
    # base cases
    if cur_cave == 'end':
        return 1
    if cur_cave == 'start':
        return 0
    # dead end if it's a visited small cave
    if cur_cave.islower() and cur_cave in visited:
        return 0
    # only need to store small caves
    if cur_cave.islower():
        visited.add(cur_cave)
    sum = 0
    for cave in caves[cur_cave]:
        sum += dfs_helper(caves, cave, visited)
    # backtracking
    if cur_cave.islower():
        visited.remove(cur_cave)
    return sum


def dfs_helper2(caves, cur_cave, visited, twice):
    # q2 allows to visit a single small cave twice
    # use a flag, pass as the first time
    if cur_cave == 'end':
        return 1
    if cur_cave == 'start':
        return 0
    if cur_cave.islower() and cur_cave in visited:
        if twice:
            # don't backtrack(remove cur_cave) when using 'twice pass'
            twice = False
            sum = 0
            for cave in caves[cur_cave]:
                sum += dfs_helper2(caves, cave, visited, twice)
            return sum
        else:
            return 0
    if cur_cave.islower():
        visited.add(cur_cave)
    sum = 0
    for cave in caves[cur_cave]:
        sum += dfs_helper2(caves, cave, visited, twice)
    if cur_cave.islower():
        visited.remove(cur_cave)
    return sum


if __name__ == '__main__':
    with open("input12.txt") as f:
        caves = {}
        for line in f:
            cave1, cave2 = line.strip().split('-')
            # make a graph for all caves
            if cave1 not in caves:
                caves[cave1] = []
            if cave2 not in caves:
                caves[cave2] = []
            caves[cave1].append(cave2)
            caves[cave2].append(cave1)
    print(caves)
    print(dfs_start(caves, 1))
    print(dfs_start(caves, 2))
