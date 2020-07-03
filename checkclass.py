#praise the lord
#praise the lord,jesus,christ
#lord jesus christplease help me
x=int(input())

d=["1s","2s","2p","3s","3p","4s","3d","4p","5s","4d","5p","6s","4f","5d","6p","7s","5f","6d","7p"]
v=[]
for rt in d:
    if "s" in rt:
        if x>=2:
            kl = rt + "2"
            v.append(kl)
            x-=2
        elif x<2:
            kl  = rt + str(x)
            v.append(kl)
            print(v)
            break
    if "p" in rt:
        if x>=6:
            kl = rt+"6"
            v.append(kl)
            x-=6
        elif x<6:
            kl = rt + str(x)
            v.append(kl)
            print(v)
            break
    if "d" in rt:
        if x>=10:
            kl = rt + "10"
            v.append(kl)
            x-=10
        elif x<10:
            kl = rt+str(x)
            v.append(kl)
            print(v)
            break
    if "f" in rt:
        if x>=14:
            kl = rt + "14"
            v.append(kl)
            x-=14
        elif x<14:
            kl = rt + str(x)
            v.append(kl)
            print(v)
            break
            
    if x == 0:
        print(v)
        break
    else:
        continue
        