def get_point(bracket):
    # get the score for invalid inputs
    if bracket == ')':
        return 3
    elif bracket == ']':
        return 57
    elif bracket == '}':
        return 1197
    elif bracket == '>':
        return 25137


def find_invalid_or_complete(line):
    # return the first invalid closing bracket
    # else return the list of opening brackets left
    # input should not have any 'completed' ones,
    # if there are, add another if to fix it.
    stack = []
    dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for c in line:
        if c in [')', ']', '}', '>']:
            if c != stack.pop():
                return c
        else:
            stack.append(dict[c])
    return stack


def get_complete_score(stack):
    # pop the whole stack to get the score
    score = 0
    while len(stack) != 0:
        bracket = stack.pop()
        score *= 5
        if bracket == ')':
            score += 1
        elif bracket == ']':
            score += 2
        elif bracket == '}':
            score += 3
        elif bracket == '>':
            score += 4
    return score


if __name__ == '__main__':
    with open("input10.txt") as f:
        point = 0
        all_complete = []
        for line in f:
            # strip to get rid of /n
            bracket = find_invalid_or_complete(line.strip())
            if isinstance(bracket, str):
                point += get_point(bracket)
            else:
                all_complete.append(get_complete_score(bracket))
        print(point)
        # sort and get the middle index to get the median score
        # since it's guaranteed to have odd number of scores, len/2 round to ground for middle
        all_complete.sort()
        print(all_complete[int(len(all_complete) / 2)])
