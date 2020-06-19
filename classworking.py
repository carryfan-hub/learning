#praise the lord,jesus,christ
#lord jesus christplease help me
x=[]
for t in range(0,3):
    y=str(input())
    x.append(y)

class student:
    def _init_(self,name,age,rollnumber):
        self.name=name
        self.age=age
        self.rollnumber=rollnumber
    def info(self):
        global x
        s=[]
        for p in range(0,3):
            try:
                m=int(x[p])
                s.append(m)
            except:
                self.name=x[p]
        for t in range(0,2):
            self.age=s[0]
            self.rollnumber=s[1]
        ui="hello {},your info \nyour age : {} \nyour rollnumber:{}"
        print(ui.format(self.name,self.age,self.rollnumber))


go = student()
go.info()
                
            




