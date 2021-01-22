from score import scores

f = open("4.txt","r")
e = f.readlines()

sc={}
for y in e:
	
	g2=[]
	for i in range(0,len(y)-1,2):
		g2.append(y[i]+y[i+1])

	k=""
	for i in g2:
		k += chr(int(i,16))

	for j in range(256):
		r = "".join(chr(ord(i)^j) for i in k)
		sc[r]=scores(r) 	

res = sorted(sc.items(), key=lambda x: x[1])
print(res[-10:])
