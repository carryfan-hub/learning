#praise the lord,jesus,christ
#lord jesus christplease help me

import camelcase
c = camelcase.CamelCase()
x = str(input())
t=0
m=0
s=[]
for i in x:
    try:
        v=int(i)
        t+=1
    except:
        m+=1
        s.append(i)


print(t)
print(m)
st="".join(s)
print(st)
print(s)

h=[]
ku=[]
t=0
for us in st:
    if c.hump(us)==s[t]:
        h.append(us)
    else:
        ku.append(us)
    t+=1
    if t == len(s):
        break
print(len(h))
print(len(ku))
oiu=2
print(oiu)









  

                
            




