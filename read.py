

def read_file(filename):
    lines = []
    with open (filename , 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None   #python 的預設值為虛無功能 
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line =='Tom':
            person = 'Tom'
            continue
        if person:     #如果person有值才執行下一行動作
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():

    lines = read_file('input.txt')
    lines =convert(lines)    #用取代的方式覆蓋
    write_file('output.txt', lines)

main()