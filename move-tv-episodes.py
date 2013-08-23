import shutil, os, re

userName  	= "joelperry"
tvShows	  	= ['The Simpsons', 'Family Guy', 'American Dad', 'The Cleveland Show', 'Community', 'Workaholics', 'Futurama', 'Breaking Bad', 'South Park', 'Louie', 'Adventure Time', 'Regular Show']
fromDirectory 	= "/Users/" + userName + "/Downloads/"
toDirectory   	= "/Users/" + userName + "/Movies/TV Shows/"
files 		= os.listdir(fromDirectory)
count 		= 0

for show in tvShows:
	for file in files:
		if re.search(show.replace(' ', '[.\s]'), file, re.IGNORECASE):
			print file
			episodeInfo = re.search("S?([0-9]?[0-9])E?([0-9][0-9])", file, re.IGNORECASE)

			if episodeInfo:
				season  = episodeInfo.group(1).lstrip('0')
				shutil.move(fromDirectory + file, toDirectory + show + "/Season " + season + "/" + file)	
			else:
				shutil.move(fromDirectory + file, toDirectory + show + "/" + file)

			count += 1

if count > 0:
	print str(count) + " episodes moved successfully" 
