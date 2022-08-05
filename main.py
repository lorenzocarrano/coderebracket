import os
fileExtensions = ['.c']

def OtherCharactersAfterBracket(line):
    print('line to analyze: ', line)
    lineLen = len(line)
    bracketPos = line.rfind('{')
    for i in range(bracketPos+1, lineLen):
        print('character: ', line[i])
        if line[i] == ' ' or line[i] == '\t' or line[i] == '\n' or line[i] == '\r':
            continue
        else:
            print('returning True')
            return True
    print('returning False')
    return False
    
   
def CountLeadingTabs(line):
    i = 0
    count = 0
    while i < len(line):
        if line[i] == '\t':
            count = count +1
        else:
            return count
        i = i+1

def FilesListPreview(list):
    print('Parsed Files:')
    for element in list:
        print(element)

def main():
    filesList = []
    for extension in fileExtensions:
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(extension):
                    filesList.append(os.path.join(root, file))
    FilesListPreview(filesList)
    for filePath in filesList:
        file = open(filePath, 'r')
        # Reading the contents of the file and closing
        lines = file.readlines()
        file.close()
        i = 0
        while i < len(lines):
            if '{' in lines[i]:
                if OtherCharactersAfterBracket(lines[i]) == False:
                    bracketPosition = lines[i].rfind('{')
                    lines[i] = lines[i][:bracketPosition] + '' + lines[i][bracketPosition+1:]
                    nIter = CountLeadingTabs(lines[i])
                    lineToInsert = ''
                    for j in range(0, nIter):
                        lineToInsert = lineToInsert + '\t'
                    lineToInsert = lineToInsert + '{\n'
                    lines.insert(i+1, lineToInsert);
                    i = i+1
            i = i+1

        file = open(filePath, 'w')
        for line in lines:
            file.write(line)
        file.close()

if __name__ == "__main__":
    main()
