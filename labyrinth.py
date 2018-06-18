from pwn import *
import itertools, sys

slist = ["L", "R"]
'''
for i in range(0, len(xploits)):
	p = process("./labyrinth")
	p.sendline(xploits[i])
	response = p.recvall()
	if("maze" in response):
		print response
		p.close()
		sys.exit(1)
	p.close()
'''	
def sendPayload(xploit):
	p = process("./labyrinth")
	p.sendline(xploit)
	response = p.recvall()
	if("flag" in response):
		print response
		p.close()
		sys.exit(1)

for i in range(20,25):
	xploit = list(itertools.product(slist, repeat = i))
	for j in range(0, len(xploit)):
		payload = "".join(xploit[j])
		print "Sending ", payload, " \n"
		sendPayload(payload)

