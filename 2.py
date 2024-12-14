def convertToSeconds(string):
    splt = string.split(":")
    return int(splt[0]) * 60 + int(splt[1])

with open('26(2).txt', encoding='utf-8') as file:
    n = int(file.readline())
    songs = {}
    
    for i in range(n):
        file.readline()
        name = ': '.join(file.readline().split(': ')[1:]).strip()
        length = convertToSeconds(': '.join(file.readline().split(': ')[1:]))
        file.readline()
        if length in songs:
            songs[length].add(name)
        else:
            songs[length] = set([name])

for i in sorted(songs.keys()):
    for k in sorted(songs[i]):
        print(k)