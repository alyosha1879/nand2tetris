class Parser:

    def __init__(self):

        with open('Add.asm','r') as f:
            self.linesList = f.readlines()
            self.commandsList = []
            self.currentCommand = ''
            self.currentType = ''

            for line in self.linesList:
                if line[0:2] == '//':
                    pass
                elif line == '\r\n':
                    pass
                else:
                    self.commandsList.extend(line.split())

    def hasMoreCommands(self):

        if len(self.commandsList) > 0:
            return True
        else :
            return False

    def advance(self):

        self.currentCommand = self.commandsList.pop(0)
        return self.currentCommand

    def commandType(self):

        if self.currentCommand[0:1] == '@':
            self.currentType = 'A_COMMAND'

        elif self.currentCommand[0] == '(' and self.currentCommand[-1] == ')':
            self.currentType =  'L_COMMAND'

        else:
            self.currentType = 'C_COMMAND'

        return self.currentType

    def symbol(self):

        if self.currentType == 'A_COMMAND':
           return self.currentCommand[1:]

        if self.currentType == 'L_COMMAND':
           return self.currentCommand[1:-1]

    def dest(self):

        if '=' in self.currentCommand:
            return self.currentCommand.split('=')[0]
    def comp(self):

        if '=' in self.currentCommand:
            return self.currentCommand.split('=')[1]
        elif ';' in self.currentCommand:
            return self.currentCommand.split(';')[0]
        else:
            return self.currentCommand

    def jump(self):

        if ';' in self.currentCommand:
            return self.currentCommand.split(';')[1]

test = Parser()
print test.commandsList

while True:
    if test.hasMoreCommands():
        test.advance()
        if test.commandType() == 'C_COMMAND':
            print test.dest()
            print test.comp()
            print test.jump()

        if test.currentType != 'C_COMMAND':
            print test.symbol()
    else:
        break
            
