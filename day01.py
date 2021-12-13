def SonarSweepP1():
    from numpy import loadtxt
    input = loadtxt("input1.txt")
    counter = 0
    for i in range(1, len(input)):
        if input[i - 1] < input[i]:
            counter += 1
    print(counter)


def SonarSweepP2():
    from numpy import loadtxt
    input = loadtxt("input1.txt")
    counter = 0
    for i in range(3, len(input)):
        if input[i - 3] < input[i]:
            counter += 1
    print(counter)


if __name__ == '__main__':
    SonarSweepP1()
    SonarSweepP2()
