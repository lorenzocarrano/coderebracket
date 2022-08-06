import os
import sys
fileExtensions = ['.c', '.h']

def OtherCharactersAfterBracket(line):
    lineLen = len(line)
    bracketPos = line.rfind('{')
    for i in range(bracketPos+1, lineLen):
        if line[i] == ' ' or line[i] == '\t' or line[i] == '\n' or line[i] == '\r' or line[i] == '\0':
            continue
        else:
            return True
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

def ModifiedFilesDisplay(list):
    print('Modified Files:')
    for element in list:
        print(element)

def PrintHelp():
    print('pyrebracket [path] - path is the path from which start parsing and modifing files')

def BracketIsTheOnlyCharacterInLine(line):
    l = line.replace(' ', '')
    l = l.replace('\t', '')
    l = l.replace('\n', '')
    l = l.replace('\r', '')
    return len(l) == 1

def main():
    if len(sys.argv) == 1:
        pathToStart = '.'
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-h':
            PrintHelp()
            return
        pathToStart = sys.argv[1]
    else:
        print('uncorrect parameters number')
        return

    filesList = []
    modifiedFilesList = []
    for extension in fileExtensions:
        for root, dirs, files in os.walk(pathToStart):
            for file in files:
                if file.endswith(extension):
                    filesList.append(os.path.join(root, file))
    FilesListPreview(filesList)
    for filePath in filesList:
        flag = 0
        file = open(filePath, 'r')
        # Reading the contents of the file and closing
        lines = file.readlines()
        file.close()
        i = 0
        while i < len(lines):
            if '{' in lines[i]:
                if OtherCharactersAfterBracket(lines[i]) == False and BracketIsTheOnlyCharacterInLine(lines[i]) == False:
                    if flag == 0:
                        modifiedFilesList.append(filePath)
                        flag = 1
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

    ModifiedFilesDisplay(modifiedFilesList)

if __name__ == "__main__":
    main()
