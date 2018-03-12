class Parser:

    def __init__(self):

        with open('Add.asm','r') as f:
	    lines = f.readlines()	  
            commands = []

	    for line in lines:
	        if line[0:2] == '//':
		    pass
		elif line == '\r\n':
	            pass
	        else:
	            commands.append(line)	

	    print commands

	def hasMoreCommands(lines):
	    if len(lines) >= 0:
		return True
	    else:
		return False

			

test = Parser()

	
