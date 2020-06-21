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
o=0
q=0
op=0
for us in st:
    if c.hump(us)==s[op]:
        o+=1
    else:
        q+=1
    op+=1
    if op == len(s):
        break

print(o)
print(q)








  

                
            




