def buildDomain(d):
    domain = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    arr = []
    for i in d:
        dom = domain.copy()
        for index, j in enumerate(i):
            assciVal = ord(j) - 97
            if assciVal >= 0 and assciVal <= 26:
                dom[assciVal] = index
        arr += [dom]


def findInDomain(arr, param):
    domain = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    for index, j in enumerate(param):
        assciVal = ord(j) - 97
        if assciVal >= 0 and assciVal <= 26:
            domain[assciVal] = index
    maxMatch = -1
    for i in arr:
        numOfMatch = 0
        for index, j in enumerate(i):
            if j == domain[index] and j != -1:
                numOfMatch += 1
        if numOfMatch > maxMatch:
            maxMatch = numOfMatch

    if maxMatch > len(param) - 3:
        return True
