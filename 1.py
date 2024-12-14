def convertToSeconds(string):
    splt = string.split(':')
    return int(splt[0]) * 60 + int(splt[1])


with open('26(1).txt') as file:
    n = int(file.readline())
    lengths = []
    
    for i in range(n):
        for _ in range(2): file.readline()
        lengths.append(file.readline().split(': ')[1:][0].strip())
        file.readline()

cnt = 0
for i in lengths:
    if convertToSeconds(i) > 180:
        cnt += 1

print(cnt)