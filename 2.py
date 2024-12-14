def convertToSeconds(string):
    splt = string.split(":")
    return int(splt[0]) * 60 + int(splt[1])

with open('26(2).txt') as file:
    n = int(file.readline())
    songs = []
    
    for i in range(n):
        song = []
        
        file.readline()
        song.append(': '.join(file.readline().split(': ')[1:]).strip())
        song.append(convertToSeconds(': '.join(file.readline().split(': ')[1:])))
        file.readline()
        songs.append(song)

lengths = [x[1] for x in songs]
minLength = min(lengths)
maxLength = max(lengths)

for i in songs:
    if i[1] == minLength:
        print(i[0])
        break

for i in songs:
    if i[1] == maxLength:
        print(i[0])
        break