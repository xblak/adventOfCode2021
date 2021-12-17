# naive solution start
# def one_step(template, dict):
#     i = 0
#     while i < len(template) - 1:
#         # see if it's a valid pair in dict
#         if (template[i], template[i + 1]) in dict:
#             template.insert(i + 1, dict[(template[i], template[i + 1])])
#             i += 1
#         i += 1
#
#
# def find_score(template):
#     # count max
#     freq = {}
#     x = 100000
#     y = 0
#     for i in template:
#         freq[i] = freq.get(i, 0) + 1
#     for key in freq:
#         x = min(x, freq[key])
#         y = max(y, freq[key])
#     return y - x
# naive solution end

def one_step(pairs: dict, rules: dict, freq: dict):
    pairs_copy = pairs.copy()
    for pair in pairs_copy:
        if rules[pair]:
            # times of character getting added
            t = pairs_copy[pair]
            # remove the old pair
            pairs[pair] = pairs[pair] - t
            # add two new pairs
            pairs[(pair[0], rules[pair])] = pairs.get((pair[0], rules[pair]), 0) + t
            pairs[(rules[pair], pair[1])] = pairs.get((rules[pair], pair[1]), 0) + t
            # add the new times of character to freq
            freq[rules[pair]] = freq.get(rules[pair], 0) + t


def find_score(freq):
    # count max
    x = 100000000000000
    y = 0
    for key in freq:
        x = min(x, freq[key])
        y = max(y, freq[key])
    return y - x

if __name__ == '__main__':
    with open("input14.txt") as f:
        template = f.readline().strip()
        pairs = {}
        freq = {}
        rules = {}
        # store the freq of pairs
        for i in range(len(template)-1):
            pairs[(template[i], template[i + 1])] = pairs.get((template[i], template[i + 1]), 0) + 1
        # store the freq of character
        for i in template:
            freq[i] = freq.get(i, 0) + 1
        # read the rules from input
        for line in f:
            list_line = list(line.strip())
            if list_line:
                rules[list_line[0], list_line[1]] = list_line[-1]
        # naive solution
        # for _ in range(10):
        #     print(template)
        #     one_step(template, rules)
        # print(find_score(template))
        for i in range(40):
            if i == 10:
                print('q1:', find_score(freq))
            one_step(pairs, rules, freq)
        print('q2:',find_score(freq))



