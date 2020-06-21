#praise the lord,jesus christ
#lord,jesus christ please help me
l = input()
m = []
m.append(l)
i = 0
while i<10:
    
    y = input()
    m.append(y)
    print(m)
    i+=1

print(m)
x = "00000000000000000000000000000000000000000000000"
c = list(x)
i=0
k=1
z=0

while k>-1:
    d=str(input())
    if d == "v":
        break
    if d != "v":
        c[i]=str(k)
        g = "".join(c)
        print(g)
        k+=1
        if k == 9:
            i+=1
            k=0
    if i == len(c)-1:
        break
    
    while z>-1:
        print(m[z],"=",g)
        z+=1
        break



