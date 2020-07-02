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
mk=[]
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
    
    if len(c)==1:
        for a in c:
            v=str(i)+"s"+str(a)
            mk.append(v)
        
    if len(c)==4 or len(c)<4 and i == 2:
        
        qwe = 0
        for dc in range(0,len(c)):
            
            if dc == 0 :
                fg = "2"+"s"+str(c[dc])
                mk.append(fg)
            if dc!= 0 :
                qwe+=int(c[dc])
            if dc == len(c)-1 :
                vc = "2"+"p"+str(qwe)
                
                mk.append(vc)
        c.clear()
    if len(c)<=9 and i == 3:
        for xc in range(0,len(c)):
            if xc==0:
                fd = "3"+"s"+str(c[xc])
                mk.append(fd)
            if xc !=0:
                po =[]
                for was in range(1,len(c)):
                    po.append(was)
                if len(po)<4:
                    ert=0
                    for gfd in range(0,len(po)):
                        ert+=int(po[gfd])
                    bcx = "3"+"p"+str(ert)
                    mk.append(bcx)
                    c.clear()
                if len(po)>4:
                    ert=0
                    for gfd in range(0,4):
                        ert+=int(po[gfd])
                    ku = 0
                    while ku<4:
                        po.pop(ku)
                        ku+=1
                    
                
                
                        
    
        
    
        
    if s == []:
        print(mk)
        print(i)
        
        break
        
    else:
        i+=1
        
    
            
                
                
        
    
    
                
        
    
        
        
    
    
    
            
    
        
        
        
        
            
    

    
    
    


        
    

        
        
        

                
                
                
                
    
       
       