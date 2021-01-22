# Single-byte XOR cipher
from collections import Counter
from score import *

g = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

g2=[]
for i in range(0,len(g)-1,2):
	g2.append(g[i]+g[i+1])

g=""
for i in g2:
	g += chr(int(i,16))

sc = {} 
for j in range(256):
	r = "".join(chr(ord(i)^j) for i in g)
	sc[r]=scores(r)

res = sorted(sc.items(), key=lambda x: x[1])
print(res[-10:])

	