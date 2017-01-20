import os,sys
import time
import datetime
import string
import example2
import config

#TO DO:
# 1. Convert to web app
# 2. Send email
# 3. Config file
# 4. weekly stats
# 5. Display time in a more readable format
# 6. Task Tracking/list
# 7. See previous files easier


filename=""
inst=""

def displayMenu():
	print ""
	print "Select an option:"
	print "-----------------"
	print "1. Start Time"
	print "2. View activities"
	print "3. Show total activities"
	print "4. Show week stats"
	print "5. Show previous files"
	print "6. Quit"
	print


# we should be storing time in an easy to store format 
# and display it in a more human readable format
def showTime(timeInSeconds):

	hr = timeInSeconds / 3600
	hr = int(hr)
	r = timeInSeconds % 3600

	mi = r / 60
	mi = int(mi)
	r = r % 60

	sec = int(r)

	output = ""
	if hr > 0: 
		output = str(hr) + " hours"

	if mi > 0:
		if len(output) > 0:
			output = output + " and " + str(mi) + " minutes"
		else:
			output = str(mi) + " minutes"

	if sec > 0:
		if len(output) > 0:
			output = output + " and " + str(sec) + " seconds"
		else:
			output = str(sec) + " seconds"
	return output

def convertSecToMin(timeInSeconds):
	return round(timeInSeconds / 60, 2)

def convertMinToHr(timeInMinute):
	return round(timeInMinute / 60, 2)

def convertSecToHr(timeInSeconds,remainder):
	remainder
	return convertMinToHr(convertSecToMin(timeInSeconds))

def parseString(str, delimiter):
	return str.split(delimiter)

def loadFile(activityDict,filename):

	#Note: race condition exists:
	#https://stackoverflow.com/questions/273192/how-to-check-if-a-directory-exists-and-create-it-if-necessary

	if not filename:
		d = datetime.date
		tDay = d.fromtimestamp(time.time())
		mDir = str(tDay.month) + "-" + str(tDay.year)

		dirPath = './timeTrackerLogs/' + str(mDir)
		if not os.path.exists(dirPath):
			os.makedirs(dirPath)
		relativePath = dirPath+'/'

	#FIX FILE NAME before commit
	filename = relativePath + str(datetime.date.today()) + "-log.txt"
	readFile(filename,activityDict)
	return filename

def readFile(filename,activityDict):
	try:
		inFile = open(filename, 'r')
		#print "Successfully opened: " + filename

		# get a list of lines
		contents = inFile.readlines()
		for line in contents:
			out = parseString(line,":")
			activityDict[out[0].strip().lower()] = float(out[1].strip("\n "))

		inFile.close()
	except IOError:
		# try to create the file
		try:
			outFile = open(filename, 'w')
			print "Successfully created: " + filename
			outFile.close()
		except IOError:
			print "Error: File does not exist"

def displayActivities(activityDict, showTotalTime):
	unit = "minutes"
	activityTime = 0
	totalTime = 0

	if len(activityDict) > 0:
		print
		print "Activities:"
		print "--------------------"
		for key in activityDict:
			activityTotalTime = 0
			activityTime = activityDict[key]
			activityTotalTime = activityTotalTime + activityTime
			print key, ":", showTime(activityTotalTime)

			totalTime = totalTime + activityTotalTime
		print

		print "_______________________________________________"
		print 
		print "TOTAL TIME: " + showTime(totalTime)
		print "_______________________________________________"
		#if showTotalTime:
		#       print getHumanReadableTime(totalTime)
	else:
		if not showTotalTime:
			print "No activity information to display."
			print

	#wait
	time.sleep(.5)

def showPreviousLogs():
	#display directory
	dirF = os.listdir("./timeTrackerLogs/")

	txt = []
	directory = []
	for files in dirF:
		if files.endswith('.txt'):
			txt.append(files)
		elif "-" in files:
			directory.append(files)
	
	for f in txt:
		print f

	for f in directory:
		print f

	#Prompt user to select a text or a directory	
	#wait for user response


def trackTime(activityDict):
	userInput = ""

	while userInput != str(3) or userInput != str(4):
		displayMenu()
		userInput = raw_input("Select an option: ")
		
		if userInput == str(1):
			activity = raw_input("Enter an activity: ")

			if activity.upper() != "QUIT" and len(activity) != 0:
				print "STARTING TIME... press ENTER to stop."
				print time.strftime("%X",time.localtime())

				timeStart = time.time()
				timeMid = ""
				
				#while True:
				#	try:
				#		timeMid = time.time()
				#		print showTime(timeMid - timeStart)+"\r",	#\r - carriage return char & "," tells print not to advance
				#	except KeyboardInterrupt:
				#		# Handles ctrl-C exception
				#		break

				print ""
				userInput = raw_input("Press ENTER to stop...")
				timeStop = time.time()
				totalTime = timeStop - timeStart

				print showTime(totalTime)
				
				#store time in dictionary
				if activity in activityDict:
					activityDict[activity] =  activityDict[activity] + totalTime
				else:
					activityDict[activity] =  totalTime
				
				#wait
				time.sleep(.5)

		elif userInput == str(2):
			displayActivities(activityDict, False)
		elif userInput == str(3):
			print "Not currently implemented."
		elif userInput == str(4):
			print "Not currently implemented."
		elif userInput == str(5):
			showPreviousLogs()
		elif userInput == str(6):
			break
		else:
			print "Enter a valid option..."

		saveFile(activityDict)

def saveFile(activityDict,filename):
	#if time is different, create a new file

	#break up current activity between previous days

	#otherwise, save to old file
	if len(activityDict) > 0:

		try:
			outFile = open(filename, "w")

			for key in activityDict:
				rowString = str(key) + " : " + str(activityDict[key]) + "\n"
				outFile.write(rowString)

			outFile.close()
		except IOError:
			print "Error: Unable to save file: " + filename

def showWeekStats():
	weeklyStatDict = {}
	filename=""

	#loadFiles
	loadFile(weeklyStatDict,filename)

#def categorizeActivities(activityDict):

	#if break, lunch, facebook, brk, warm up

	#if hacker, read, dev

if __name__ == "__main__":
	startTime = time.time()
	inst=startTime

	# declare a list
	activityDict = {} 

	filename = loadFile(activityDict,filename)
	trackTime(activityDict)
	saveFile(activityDict,filename)

	endTime = time.time()
	sessionTime = endTime - startTime

	print "Total session time: ".upper() + showTime(sessionTime)
	#sendDailyEmail()