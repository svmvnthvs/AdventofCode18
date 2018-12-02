def getsum():
    array = [line.rstrip() for line in open('day1.txt')]
    changes = list(map(int, array))
    a = sum(changes)
    print(a)
    return a

def getfirstfreq():
    array = [line.rstrip() for line in open('day1.txt')]
    freqs = []
    c = 0
    d = 0
    freqs.append(c)
    while (d == 0):
        for i in range(len(array)):
            c += int(array[i])
            for j in range(len(freqs)):
                if (c == freqs[j]):
                    d = 1
            if (d == 0):
                freqs.append(c)
            if (d == 1):
                print(c)
                return c

getsum()
getfirstfreq()