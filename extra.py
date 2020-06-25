#praise the lord,jesus,christ
#lord jesus christ please help me
x=[]
for i in range(0,6):
    y = str(input())
    x.append(y)
    
print(x)
v=[]
for t in x:
    for p in range(0,1):
        v.append(t[p])
        
print(v)

op=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
h=[]
for g in v:
    for k in range(0,26):
        if g == op[k]:
            h.append(k)
            break
        else:
            continue
m = []
while True:
    k = min(h)
    m.append(k)
    h.remove(k)
    if len(h)==0:
        break
    
print(m)
okn = []
for b in m:
    okn.append(op[b])
print(okn)
#final output
output = []
for i in okn:
    for mv in x:
        if i == mv[0]:
            output.append(mv)
        else:
            continue

print(output)