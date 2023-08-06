"""
THIS MODULE CODED BY i3BODY ( TIME MODULE CLONE VERSION )
"""
import time
import datetime

lstx1 = []
lstx2 = []

def wait(parameter):
	for num in parameter:
		save_nu = lstx1.append(num)
		save_op = lstx2.append(num)

	# Get Operation ( s - m - h - d - w )
	last = lstx2.reverse()
	oper = lstx2[0]

	# Get Time
	num = ''.join(map(str, lstx1))[:-1]

	blacklist = ['~','!','@','#','$','%','^','&','*','(',')','-','+','/','\ ','|','{','}','[',']','+']

	if oper in blacklist:
		print('OperationError : You Can Use ( s - m - h - d - w ) .')
		time.sleep(5)
		exit()
	else:
		pass


	# Check Timeout If The User Used Days

	if oper == 'w':
		if int(num) > 2:
			print('TimeoutError : You Can Use Wait Maximum 2 Weeks Only .')
			time.sleep(5)
			exit()
		else:
			time.sleep(int(num)*86400*7)

	elif oper == 'd':
		get_timeout_date = datetime.datetime.today() + datetime.timedelta(days=14)
		get_userinp_date = datetime.datetime.today() + datetime.timedelta(days=int(num))
		#get_timeout_day  = get_timeout_date.strftime('%d')

		if get_timeout_date < get_userinp_date:
			print('TimeoutError : You Can Use Wait Maximum 14 Days Only .')
			time.sleep(5)
			exit()
		else:
			time.sleep(int(num)*86400)

	elif oper == 'h':
		if int(num) > 72:
			print('TimeoutError : You Can Use Wait Maximum 72 Hours Only .')
			time.sleep(5)
			exit()
		else:
			time.sleep(int(num)*3600)

	elif oper == 'm':
		if int(num) > 20160:
			print('TimeoutError : You Can Use Wait Maximum 20160 Minutes Only .')
			time.sleep(5)
			exit()
		else:
			time.sleep(int(num)*60)

	elif oper == 's':
		if int(num) > 1209600:
			print('TimeoutError : You Can Use Wait Maximum 1209600 Seconds Only .')
			time.sleep(5)
			exit()
		else:
			time.sleep(int(num))


	else:
		print('OperationError : You Can Use ( s - m - h - d - w ) .')
		time.sleep(5)
		exit()
		


	return parameter