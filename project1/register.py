from tkinter import *
from tkinter import messagebox
import os
class Regis(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("760x480")
        self.configure(background="pink")
        self.title("Form")
        
    def click(self):
        print("Button clicked")

    def value(self):
         global firstname,lastname,email,phone,age,country,gender
         firstname=StringVar()
         lastname=StringVar()
         email=StringVar()
         phone=StringVar()
         age=IntVar()
         gender=StringVar()
         country=StringVar()

         Label(self,text="Please enter below to add profile",fg="white",bg="green",font=("comicsansms",8,"bold")).pack()
         Label(self,text="").pack()
         Label(self,text="User firstname",fg="white",bg="green").pack()
         usernameentry=Entry(self,textvariable=firstname,fg="black",bg="silver")
         usernameentry.pack()

         Label(self,text="User lastname",fg="white",bg="green").pack()
         userlastentry=Entry(self,textvariable=lastname,fg="black",bg="silver")
         userlastentry.pack()

         Label(self,text="User Email",fg="white",bg="green").pack()
         useremail=Entry(self,textvariable=email,fg="black",bg="silver")
         useremail.pack()

         Label(self,text="User phonenumber",fg="white",bg="green").pack()
         userphone=Entry(self,textvariable=phone,fg="black",bg="silver")
         userphone.pack()

         Label(self,text="User age",fg="white",bg="green").pack()
         userage=Entry(self,textvariable=age,fg="black",bg="silver")
         userage.pack()

         Label(self,text="User gender",fg="white",bg="green").pack()
         userage=Entry(self,textvariable=gender,fg="black",bg="silver")
         userage.pack()

         Label(self,text="User country",fg="white",bg="green").pack()
         usercountry=Entry(self,textvariable=country,fg="black",bg="silver")
         usercountry.pack()
         Label(self,text="").pack()

    def submit(self,text):
        Button(self,text=text,fg="white",bg="red",command=self.heat).pack()

    def heat(self):

          global firstname,lastname,email,phone,age,country,screen,gender
          self.firstname=firstname.get()
          self.lastname=lastname.get()
          self.email=email.get()
          self.phone=phone.get()
          self.age=age.get()
          self.country=country.get()
          self.gender=gender.get()
          



          listoffiles= os.listdir()
          if firstname.get()=="" or lastname.get()=="" or email.get()=="" or phone.get()=="" or age.get()=="" or  country.get()=="" or gender.get()=="":
                messagebox.showwarning("please","fill up the form")
    
          else:        
             if self.firstname not in listoffiles:           
           
                        file=open(self.firstname,"w")
                        file.write(self.firstname+"\n")
                        file.write(self.lastname+"\n")
                        file.write(self.email+"\n")
                        file.write(self.phone+"\n")
                        file.write(str(self.age)+"\n")
                        file.write(self.country+"\n")
                        file.write(self.gender+"\n")
                        file.close()
               
      
             else:
                  messagebox.showwarning("sorry","Already register")
         
if __name__ == "__main__":

    window=Regis()
    window.value()
    window.submit("Submit")
    window.mainloop()