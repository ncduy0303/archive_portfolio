f = open('raw-achievements.txt')
year = '123'
arr = []
for line in f:
    line = line.strip()
    if line == '':
        continue
    if len(line) == 4 and line[0] == '2':
        print('{')
        print('"year": ' + year + ',')
        print('"achievements": [' + ','.join(arr) + ']')
        print('},')
        year = line
        arr = []
        continue
    arr.append('"' + line + '"')
