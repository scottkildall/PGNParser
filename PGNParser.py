# load all lines into an array
def loadLines(filename):
	f = open( filename, "r" )
	lines = []
	for line in f:
		# do additional line-processing here
		lines.append( line.rstrip('\n') )
		 

	f.close()
	return lines

def getChessLine(filename):
	lines = loadLines(filename)
	
	chessLine = ""
	for l in lines:
		if (l[0] != '[' and l[0] != "\r"):
			chessLine = chessLine + l

	return chessLine

# return array of chess lines, even indices = white, odd indices = black
def parseChessLines(chessLine):
	clArray = []
	return clArray

def outputCSV(clArray, filename):
	f = open( filename, "w" )

	# write header
	f.write( "White,Black\n")
	
	# write out array lines here

	f.close()

# main
cl = getChessLine("kasparov_deep_blue_1996.pgn")
clArray = parseChessLines(cl)
outputCSV(cl, "output.csv")
