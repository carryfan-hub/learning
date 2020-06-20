#praise the lord,jesus,christ
#lord jesus christplease help me
from tkinter import *
window = Tk()
x=Entry(window,width=200)
x.pack()
def showhim():
    m=input()
    class student:
        j="nms-dps"
        def _init_(self,name,age,rollnumber):
            self.name=name
            self.age=age
            self.rollnumber=rollnumber
        @classmethod
        def schoolname(cls):
            x.insert(0,cls.j)
        
        def studentinfo(self):
            x.delete(0,END)
            x.insert(0,self.name+"," + self.age + "," + self.rollnumber)
    class base:
        def _init_(self,favorites,hates) :
            self.favorites = favorites
            self.hates=hates
        def thorin(self):
            x.insert(0,self.favorites,self.hates)   
    class sutility(student,base):
        l="kou"
        def _init_(self,name,age,rollnumber,favorites,hates,year):
            base._init_(self,favorites,hates)
            student._init_(self,name,age,rollnumber)
            self.year=year
        def getinfo(self):
            x.delete(0,END)
            x.insert(0,self.name+"" + self.age+""+self.rollnumber+""+self.year+""+self.hates+""+self.favorites)
        @classmethod
        def class_variable(cls):
            x.insert(0,cls.l)
    m = sutility()
        
    m.name = str(input())
    m.age = str(input())
    m.year=str(input())
    m.rollnumber=str(input())
    m.favorites = str(input())
    m.hates=str(input())
    m.getinfo()
    sutility.schoolname()
    m.studentinfo()
    sutility.class_variable()

        
        

    
            

y=Button(window,text="mudit",command=showhim)
y.pack()
window.mainloop()

