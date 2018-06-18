from __future__ import print_function
from pwn import *
import re

# Connect and log in
p = connect("offsec-chalbroker.osiris.cyber.nyu.edu", 1254)
p.recvuntil(":")
p.sendline("jm5833")
p.recvuntil('Decode this!\n')

data = p.recvall()

# No longer need connections
p.close()

# Decrypt Data
while not "flag{" in data:

    # Purge bad characters
    data = re.sub(r'[\'\"/\\]', '', data)

    # Determine base and convert
    base64Regex = re.compile(r'[A-Z]')
    base64Match = base64Regex.search(data)

    if not base64Match == None:
        print("base64")
        data = data.decode("base64")
    else:
        print("Hex")
        data = data.decode("hex")

print(data)

