class Parser:

    def __init__(self):

        with open('Add.asm','r') as f:
	    self.linesList = f.readlines()	  
            self.commandsList = []
            self.currentCommand = ''

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
	    return 'A_COMMAND'

        # match if dest=comp or comp;jump or dest=comp;jump.
	# only comp not match.
	
        if '=' in self.currentCommand:
	    return 'C_COMMAND'

        if ';' in self.currentCommand:
	    return 'C_COMMAND'

        return 'L_COMMAND'

    def sysmbol(self):
	pass			

test = Parser()
print test.commandsList

while True:
    if test.hasMoreCommands():
        test.advance()
        print test.commandType()

    else:
        break


#for command in test.commandsList:
#    print command
