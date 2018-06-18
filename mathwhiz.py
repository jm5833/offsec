import socket

def hextoint(num):
	retval = 0
	try:
		retval = int(num)
	except:
		units = dict([("0", 0), ("1", 1), ("2",2), ("3", 3), 
					  ("4", 4), ("5", 5), ("6", 6), ("7", 7),
					  ("8", 8), ("9", 9),
					  ("a", 10), ("b",11), ("c", 12), 
					  ("d",13), ("e", 14), ("f", 15)])
		data = list(num)
		datalen = len(data)
		for x in range(0,datalen - 2):
			retval = retval + (units[data[datalen - x - 1]] * (16 ** x))
	return retval

def texttoint(num):
	retval = 0
	try:
		retval = int(num)
	except:
		units = dict([("ZERO", 0), ("ONE",1), ("TWO",2),
					  ("THREE",3), ("FOUR",4), ("FIVE",5),
					  ("SIX",6), ("SEVEN",7), ("EIGHT",8),
					  ("NINE",9)])
		data = num.split("-")
		datalen = len(data)
		for x in range(0,datalen):
			retval = retval + (units[data[datalen - x - 1]] * (10 ** x))
	return retval

def bintoint(num):
	retval = 0
	try:
		retval = int(num)
	except:
		units = dict([("0",0), ("1",1)])
		data = list(num)
		datalen = len(data)
		for x in range(0,datalen - 2):
			retval = retval + (units[data[datalen - x - 1]] * (2 ** x))
	return retval

def toint(num):
	data = list(num)
	check =  ''.join(data[:2])
	if check == "0x":
		return hextoint(num)
	elif check == "0b":
		return bintoint(num)
	else:
		return texttoint(num)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("offsec-chalbroker.osiris.cyber.nyu.edu", 1236))
print s.recv(1024),
netid = raw_input()
print netid,
s.send(netid +'\n')
print s.recv(1024),
response = str(s.recv(1024))
print response
data = response.split()
result = 0
a = int(data[37])
b = int(data[39])
if data[38] == "+":
	result = a + b
elif data[38] == "-":
	result = a - b
elif data[38] == "*":
	result = a * b
print result
s.send(str(result) + '\n')
while True:
	response = str(s.recv(1024))
	print response,
	data = response.split()
	a = toint(data[2])
	b = toint(data[4])
	if data[3] == "+":
		result = a + b
	elif data[3] == "-":
		result = a - b
	elif data[3] == "*":
		result = a * b
	print str(result) + '\n'
	s.send(str(result) + '\n')

