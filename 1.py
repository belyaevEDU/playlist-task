def convertToSeconds(string):
    splt = string.split(':')
    return int(splt[0]) * 60 + int(splt[1])

cnt = 0
with open('26(1).txt') as file:
    n = int(file.readline())
    for i in range(n):
        for _ in range(2): file.readline()
        if convertToSeconds(file.readline().split(': ')[1:][0].strip()) > 180:
            cnt += 1
        file.readline()

print(cnt)