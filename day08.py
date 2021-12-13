# Unique:
# 1: 2
# 4: 4
# 7: 3
# 8: 7

# 2: 5 e
# 3: 5 f
# 5: 5 b

# 0: 6 no d check both d,g, 069 all have g
# 6: 6 no c check both a,c, 069 all have a
# 9: 6 no e

#            aaaa
#           b    c
#           b    c
#            dddd
#           e    f
#           e    f
#            gggg

# map all characters from input, by the frequency
# check the frequency of the character to know their actual location
# a: 8, b: 6, c: 8, d: 7, e: 4, f: 9, g: 7
# repeated: a,c=8, d,g=7

# we know 1,4,7,8 simply by the length of the output
# if len is 5,(2,3,5), check if any character have freq of e:4, b:6 corresponding to 2,5
# else confirm f:9(3) last
# if len is 6 (0,6,9), check if there is one d,g:7, or one a,c:8, no e:4 corresponding to 0,6,9


def sumofall(patternlist, outlist):
    sum = 0
    for i in range(len(patternlist)):
        dict = {}
        for pattern in patternlist[i]:
            for c in pattern:
                dict[c] = dict.get(c, 0)+1
        num = 0
        for out in outlist[i]:
            # unique 1478, len 5 235, len 6 069
            # value 1, len 2
            if len(out) == 2:
                num *= 10
                num += 1
            # value 4, len 4
            if len(out) == 4:
                num *= 10
                num += 4
            # value 7, len 3
            if len(out) == 3:
                num *= 10
                num += 7
            # value 8, len 7
            if len(out) == 7:
                num *= 10
                num += 8
            # value 2 3 5, len 5
            # e:4, b:6 corresponding to 2,5
            # confirm 3 last
            if len(out) == 5:
                num *= 10
                n = 0
                for c in out:
                    if dict[c] == 4:
                        n = 2
                        break
                    elif dict[c] == 6:
                        n = 5
                        break
                if n == 0:
                    n = 3
                num += n
            # value 0 6 9, len 6
            # check if there is one d,g:7, or one a,c:8, or no e:4 corresponding to 0,6,9
            if len(out) == 6:
                num *= 10
                e = 0
                dg = 0
                ac = 0
                for c in out:
                    if dict[c] == 7:
                        dg += 1
                    elif dict[c] == 8:
                        ac += 1
                    elif dict[c] == 4:
                        e += 1
                if dg == 1:
                    num += 0
                elif ac == 1:
                    num += 6
                elif e == 0:
                    num += 9
        print(num)
        sum += num
    return sum



if __name__ == '__main__':
    with open("input08.txt") as f:
        patternlist = []
        outlist = []
        for line in f:
            sign = line.strip().split('|')
            patternlist.append(sign[0].strip().split(' '))
            outlist.append(sign[1].strip().split(' '))

        count = 0
        for line in outlist:
            for x in line:
                if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7:
                    count += 1
        print(count)
        print(sumofall(patternlist, outlist))