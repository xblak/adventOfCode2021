import numpy as np

def getrealfuel(steps):
    # 1+2+...+n = n(n+1)/2 calculate the real crab fuel
    return steps*(steps+1)/2

if __name__ == '__main__':
    from numpy import loadtxt
    arr = loadtxt('input7.txt', dtype=int, delimiter=',')
    # get a really big number for comparison
    least = float('inf')
    leastreal = float('inf')
    for i in range(np.min(arr), np.max(arr)):
        least = min(least, np.sum(np.abs(arr - i)))
        leastreal = min(leastreal, np.sum(getrealfuel(np.abs(arr - i))))
    print(least, leastreal)
