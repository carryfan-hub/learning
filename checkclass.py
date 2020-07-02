#praise the lord
#praise the lord,jesus,christ
#lord jesus christplease help me
x=int(input())
s=[]

def electroconfig(x):
    global s
    i = 1
    
    
    while True:
        for t in range(0,i):
            if t == 0:
                m=2
                x-=m
                
                s.append(m)
                
            else:
                for w in range(-t,t+1):
                    if x == 1:
                        l = 1
                        x-=l
                        s.append(l)
                    if x!=0 and x!=1:
                        l=2
                        x-=l
                        s.append(l)
                    if x == 0:
                        break
        i+=1
        if x == 0:
            print(s)
            
            break
                    
if __name__ == "__main__":
    electroconfig(x)
mk=[2,10,18,36,54,86,118]
vxz=[]
mc=[]
i = 1
while i>0:
    r = i**2
    c=[]
    d = []
    for t in range(0,r):
        d.append(t)
    
    if len(s)<len(d):
        for eo in s:
            c.append(eo)
        print(c)
        s.clear()
    if len(s)>len(d):
        for e in range(0,len(d)):
            c.append(s[e])
        print(c)
        if len(d)==1:
            s.pop(0)
        else:
            kk = 0
            while kk<len(d):
                for th in range(0,1):
                    s.pop(th)
                kk+=1
    
                    
                
                
    for ewq in mk:
        cd = x-ewq
        if cd<0:
            break
        else:
            vxz.append(ewq)
        
    po=max(vxz)
    print(po)
    for esa in mk:
        g=x-esa
        if g <0:
            kgf=esa
            print(kgf)
            break
            
    if i == 2:
        hgf = int(kgf)-x
        gdsm=[5,4,3,2,1]
        kjhn=[6,7]
        if hgf in gdsm:
            kx = ["s","p"]
            y=-1
            for edf in kx:
                
                y+=1
                while y<len(c):
                    fdg = str(po)+"2"+str(edf)+str(c[y])
                    mc.append(fdg)
                    break
        if hgf in kjhn:
            fdg = str(po)+"2"+"s"+str(c[-1])
            mc.append(fdg)
            
    
                    
    
        
    if s == []:
        print(mc)
        
        print(i)
        
        break
        
    else:
        i+=1
        
    
            
                
                
        
    
    
                
        
    
        
        
    
    
    
            
    
        
        
        
        
            
    

    
    
    


        
    

        
        
        

                
                
                
                
    
       
       