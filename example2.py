#example, getting a date from an instant
import time
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

if __name__ == "__main__": 
	date = time.strftime("%m%d%Y")
	print date

	#cal = calendar.month(2017,1)
	#print cal

	print convertInstToDate(time.time())
	if not hasDayChanged(time.time()):
		print "Same"