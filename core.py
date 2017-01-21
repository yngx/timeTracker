#example, getting a date from an instant
import time
import os
from datetime import date
import calendar

#https://stackoverflow.com/questions/419163/what-does-if-name-main-do
def convertInstToDate(inst):
	st = time.localtime(inst)
	y,m,d = st[0],st[1],st[2]
	if m < 10:
		m = str(0) + str(m)
	return str(m) + str(d) + str(y)

def hasDayChanged(oldInst):
	oldSt = time.localtime(oldInst)
	newSt = time.localtime(time.time())

	if oldSt[2] != newSt[2]:
		return True
	elif oldSt[1] != newSt[1]:
		return True
	elif oldSt[0] != newSt[0]:
		return True

	return False

def getDayOfWeek():
	return date.today().weekday()


#assumes offSet is an integer
#I need to fix the leading zero
def getFileName(offSet,makeDirectory):
	tDay = time.strftime("%d")
	if offSet:
		if offSet < int(tDay):
			tDay = int(tDay) - offSet

	tMon = time.strftime("%m").lstrip("0")
	tYear= time.strftime("%Y")
	
	fName = str(tYear)+ "-" + "0" + str(tMon) + "-" + str(tDay)	#will get messed up later

	folderName = str(tMon) + "-" + str(tYear)
	dirPath = './timeTrackerLogs/' + folderName

	#Allow making of directory
	if makeDirectory:
		if not os.path.exists(dirPath):
			os.makedirs(dirPath)
	relativePath = dirPath+'/'

	#FIX FILE NAME before commit
	return relativePath + fName + "-log.txt"


if __name__ == "__main__": 
	dt = time.strftime("%Y-%m-%d")
	print dt

	print date.today().weekday()
	#cal = calendar.month(2017,1)
	#print cal

	print convertInstToDate(time.time())
	if not hasDayChanged(time.time()):
		print "Same"

	print getFileName(1,False)

	print getDayOfWeek()



