def ParsingData(file_name):
    lines = open(file_name,'r').read().split('\n')
    dictionary = {}
    for line in range(0, len(lines)):
        lines[line] = lines[line].split(':')[1]
        numbers = list(map(int, lines[line].split(',')))
        dictionary[line] = numbers

ParsingData("newfile.txt")