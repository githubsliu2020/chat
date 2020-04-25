

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] #s[0]清單內的前五個字
    name = s[0][5:] #s[0]清單從開始的第五個字走到結尾
    print(time)
    print(name)