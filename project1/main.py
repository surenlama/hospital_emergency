#Hospital  emergency room booking system
from tkinter import *
import os
from tkinter import messagebox
import mysql.connector
from register import *
import datetime
 
room=["1","2","3","4","5","6","7","8","9","10"]
amount=0
roomtype=""
room1=0
name=""
price=0
starttime=0
endtime=0

def passworddoesnotmatch():
    global screen3
    screen3=Toplevel(root)
    screen3.title("UserNotExit")
    screen3.geometry("150x100")
    Label(screen3,text="PasswordNotMatch").pack()
    Button(screen3,text="OK",command=delete2).pack()

def Usernotexit():
    global screen3
    screen3=Toplevel(root)
    screen3.title("UserNotExit")
    screen3.geometry("150x100")
    Label(screen3,text="UserAlreadyExits").pack()
    Button(screen3,text="OK",command=delete2).pack()

def delete2():
    screen3.destroy()

def empty():
    global screen3
    screen3=Toplevel(root)
    screen3.title("Empty")
    screen3.geometry("150x100")
    Label(screen3,text="PleaseFillUp").pack()
    Button(screen3,text="OK",command=delete2).pack()    

def sucessregister():
    global screen3
    screen3=Toplevel(root)
    screen3.title("Sucess")
    screen3.geometry("150x100")
    Label(screen3,text="Sucessfully registered").pack()
    Button(screen3,text="OK",command=delete2).pack()

def new():
    global screen10
    screen10=Toplevel(root)
    screen8.destroy()
    screen10.geometry("550x400")
    screen10.configure(background="white")
    l1=Label(screen10,text="Welcome to the Emergency room",font="comicsansms 20 bold",fg="white",bg="green")
    b1=Button(screen10,text="Add profile",font="comicsansms 10 bold",fg="white",bg="red",command=patientadd)
    b2=Button(screen10,text="Add Book",font="comicsansms 10 bold",fg="white",bg="red",command=Book)
    b3=Button(screen10,text="Bill",font="comicsansms 10 bold",fg="white",bg="red",command=Bill)
    b4=Button(screen10,text="Exit",font="comicsansms 10 bold",fg="white",bg="red",command=close)
    l1.pack()
    Label(screen10,text="").pack()
    b1.pack()
    Label(screen10,text="").pack()
    b2.pack()
    Label(screen10,text="").pack()
    b3.pack()
    Label(screen10,text="").pack()
    b4.pack()

def close():
    screen10.destroy()
    endtime=datetime.date.today()
    messagebox.showwarning("bye","Ending time:"+str(endtime))


def registerverify():
    global usernameinfo,passwordinfo
    usernameinfo=username.get()
    passwordinfo=password.get()
    repasswordinfo=repassword.get()
    listoffiles= os.listdir()
    if usernameinfo=="" or passwordinfo=="" or repasswordinfo=="":
        empty()
    else:        
        if usernameinfo not in listoffiles:           
            if passwordinfo==repasswordinfo:
                file=open(usernameinfo,"w")
                file.write(usernameinfo+"\n")
                file.write(passwordinfo+"\n")
                file.write(repasswordinfo)
                file.close()
                usernameentry.delete(0,END)
                userpasswordentry.delete(0,END)
                userrepasswordentry.delete(0,END)
                sucessregister()           
            else:
                passworddoesnotmatch()        
        else:
            Usernotexit()

def register():
    global screen1
    screen1=Toplevel(root)
    screen1.title("Register")
    screen1.geometry("350x350")
    screen1.configure(background="white")
    global username,password,repassword
    username=StringVar()
    password=StringVar()
    repassword=StringVar()
    global usernameentry,userpasswordentry,userrepasswordentry

    Label(screen1,text="Please enter details below to register",fg="white",bg="green",font=("comicsansms",8,"bold")).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username",fg="white",bg="green").pack()
    usernameentry=Entry(screen1,textvariable=username,fg="black")
    usernameentry.pack()
    Label(screen1,text="Password",fg="white",bg="green").pack()
    userpasswordentry=Entry(screen1,textvariable=password,fg="black",show="*")
    userpasswordentry.pack()
    Label(screen1,text="Repassword",fg="white",bg="green").pack()
    userrepasswordentry=Entry(screen1,textvariable=repassword,fg="black",show="*")
    userrepasswordentry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Add more",width=10,height=1,command=regist,bg="green").pack()  
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width=10,height=1,command=registerverify,bg="red").pack()

def regist():
    window=Regis()
    window.value()
    window.submit("Submit")
    window.mainloop()

def paswordverify():
    global username2,password2,a,b,screen2,screen1
    username2=username1.get()
    password2=password1.get()
 
    listoffiles= os.listdir()
    if username2=="" or password2=="":
        empty()
    else:    
        if username2 in listoffiles:
          file1= open(username2,'r') 
          verify=file1.read().splitlines()
          if password2 in verify:
              start()
              a=username2
              b=password2
          else:
             passwordincorrect()
        else:
            usernotfound()  

def Book():
    global amount,roomtype,room1,name,price,var 
    screenbook=Toplevel(root)

    screenbook.geometry("734x520")
    screenbook.configure(background="pink")
    screenbook.title("Form")
   
    name=StringVar()
    price=StringVar()
    Label(screenbook,text="Select room",bg="red",fg="white",font="comicsansms 19 bold").pack()
    Label(screenbook,text="").pack()
    Label(screenbook,text="Submit a number to book the room",fg="white",bg="green").pack()
    messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10" )
    Label(screenbook,text="").pack() 
    usernameentry1=Entry(screenbook,textvariable=name)
    usernameentry1.pack()
    Label(screenbook,text="").pack()
    Label(screenbook,text="pay 7000 for 1 room",fg="white",bg="green").pack()
    Label(screenbook,text="").pack()
    usernameentry=Entry(screenbook,textvariable=price)
    usernameentry.pack()
    Label(screenbook,text="").pack()
    Button(screenbook,text="Submit",width=10,height=1,command=submit,bg="red",fg="white").pack()
    Label(screenbook,text="").pack()
   
    var=IntVar()
    Label(screenbook,text="choose your room type",fg="white",bg="red",font="lucida 15 bold").pack()
    Label(screenbook,text="").pack()
    Radiobutton(screenbook,text="International Emergency Care Unit",variable=var,value=1,bg="green",fg="black",padx=14).pack()
    Radiobutton(screenbook,text="Critical Care Areas",variable=var,value=2,bg="green",fg="black",padx=14).pack()
    Radiobutton(screenbook,text="ophthalmology",variable=var,value=3,bg="green",fg="black",padx=14).pack()
    Radiobutton(screenbook,text="dentistry",variable=var,value=4,bg="green",fg="black",padx=14).pack()
    Label(screenbook,text="").pack()
    Button(screenbook,text="Submit",fg="white",bg="red",command=submit1).pack()
    Label(screenbook,text="").pack()
 

def submit():
        global name,price,amount,room1

        if len(room)==0:
                messagebox.showwarning("Room packed","Sorry every room is booked")

        if name.get()=="" or price.get()=="":
            messagebox.showwarning("pop up","Please fillup")


        elif name.get()=="1" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000
                room1+=1
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")
         
        elif name.get()=="2" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000
                room1+=1
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="3" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000
                room1+=1   
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="4" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000
                room1+=1   
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="5" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000
                room1+=1   
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="6" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000 
                room1+=1   
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="7" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000 
                room1+=1   
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="8" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000 
                room1+=1   
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="9" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000 
                room1+=1    
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif name.get()=="10" and price.get()=="7000":
            if name.get() not in room:
                messagebox.showwarning("pop up",f"{name.get()} Already booked")
            else:    
                messagebox.showwarning("pop up",f"{name.get()} room booked")
                room.remove(name.get())
                amount+=7000 
                room1+=1   
                messagebox.showwarning("Select a room number","1,2,3,4,5,6,7,8,9,10")

        elif price.get()<"7000":
                messagebox.showwarning("sorry","your money is less than 7000")

        elif price.get()>"7000":
                messagebox.showwarning("sorry","your money is more than 7000")   


def submit1():
       global var,roomtype
       if var.get()==1:
           roomtype="International Emergency Care Unit"
           messagebox.showwarning("pressed","select") 
       elif var.get()==2:
           roomtype="Critical Care Areas"  
           messagebox.showwarning("pressed","select")   
       elif var.get()==3:  
           roomtype="ophthalmology" 
           messagebox.showwarning("pressed","select")     
       elif var.get()==3:  
           roomtype="dentistry"  
           messagebox.showwarning("pressed","select")          
       else:
           pass


def patientadd():
    screenadd=Toplevel(root)
    screenadd.geometry("760x480")
    screenadd.configure(background="pink")
    screenadd.title("Form")
    global firstname,lastname,email,phone,age,country,gender
    firstname=StringVar()
    lastname=StringVar()
    email=StringVar()
    phone=StringVar()
    age=IntVar()
    gender=StringVar()
    country=StringVar()

    Label(screenadd,text="Please enter below to add profile",fg="white",bg="green",font=("comicsansms",8,"bold")).pack()
    Label(screenadd,text="").pack()
    Label(screenadd,text="Patient firstname",fg="white",bg="green").pack()
    usernameentry=Entry(screenadd,textvariable=firstname,fg="black",bg="silver")
    usernameentry.pack()

    Label(screenadd,text="Patient lastname",fg="white",bg="green").pack()
    userlastentry=Entry(screenadd,textvariable=lastname,fg="black",bg="silver")
    userlastentry.pack()

    Label(screenadd,text="Patient Email",fg="white",bg="green").pack()
    useremail=Entry(screenadd,textvariable=email,fg="black",bg="silver")
    useremail.pack()

    Label(screenadd,text="Patient phonenumber",fg="white",bg="green").pack()
    userphone=Entry(screenadd,textvariable=phone,fg="black",bg="silver")
    userphone.pack()

    Label(screenadd,text="patient age",fg="white",bg="green").pack()
    userage=Entry(screenadd,textvariable=age,fg="black",bg="silver")
    userage.pack()

    Label(screenadd,text="patient gender",fg="white",bg="green").pack()
    userage=Entry(screenadd,textvariable=gender,fg="black",bg="silver")
    userage.pack()

    Label(screenadd,text="patient country",fg="white",bg="green").pack()
    usercountry=Entry(screenadd,textvariable=country,fg="black",bg="silver")
    usercountry.pack()
    Label(screenadd,text="").pack()
    Button(screenadd,text="submit",fg="white",bg="red",command=heat).pack()

def heat():
    global firstname,lastname,email,phone,age,country,screen,gender
    if firstname.get()=="" or lastname.get()=="" or email.get()=="" or phone.get()=="" or age.get() ==0 or country.get()=="" or gender.get()=="":
        messagebox.showinfo("Please","Fillup the form") 
    else:      
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="hospital")
        mycursor=mydb.cursor()            
        s="INSERT INTO profile(Firstname,Lastname,Email,phone,age,gender,country) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        b1=(firstname.get(),lastname.get(),email.get(),phone.get(),age.get(),gender.get(),country.get())
        mycursor.execute(s,b1)
        mydb.commit()
        messagebox.showinfo("Wow","Sucessfully Register")      

def Bill():
    global screenbill,name1,root
    screenbill=Toplevel(root)
    screenbill.geometry("764x500")
    screenbill.configure(background="pink")
    screenbill.title("Bill")
    name1=StringVar()
    Label(screenbill,text="Bill of patient",fg="white",bg="green").pack()      
    Label(screenbill,text="").pack()
    Label(screenbill,text="Enter the name of patient",fg="white",bg="green").pack()    
    Label(screenbill,text="").pack()
    usernameentry1=Entry(screenbill,textvariable=name1)
    usernameentry1.pack()
    Label(screenbill,text="").pack()
    Button(screenbill,text="Submit",width=10,height=1,command=submitbill,bg="red",fg="white").pack()

def submitbill():
    global screenbill,name1
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="hospital")
    mycursor=mydb.cursor() 
    mycursor.execute("select * from profile where Firstname=%s",[name1.get()])
    result=mycursor.fetchall()
    for row in result:             
            Label(screenbill,text="").pack()
            Label(screenbill,text='Patient Firstname:'+row[0],fg="black",bg="pink",font=("comicsansms",15,"bold")).pack()
            Label(screenbill,text='Patient Lastname:'+row[1],fg="black",bg='pink',font=("comicsansms",15,"bold")).pack()
            Label(screenbill,text='Patient Email:'+row[2],fg="black",bg='pink',font=("comicsansms",15,"bold")).pack()
            Label(screenbill,text='Patient Phonenumber:'+row[3],fg="black",bg='pink',font=("comicsansms",15,"bold")).pack()
            Label(screenbill,text='Patient Age:'+str(row[4]),fg="black",bg='pink',font=("comicsansms",15,"bold")).pack()
            Label(screenbill,text='Patient Gender:'+row[5],fg="black",bg='pink',font=("comicsansms",15,"bold")).pack()
            Label(screenbill,text='Patient Country:'+row[6],fg="black",bg='pink',font=("comicsansms",15,"bold")).pack() 
            Label(screenbill,text='Patient Total amount:'+str(amount),fg="black",bg='pink',font=("comicsansms",15,"bold")).pack()  
            Label(screenbill,text='Patient room:'+str(room1),fg="black",bg='pink',font=("comicsansms",15,"bold")).pack() 
            Label(screenbill,text='Patient Type of room:'+roomtype,fg="black",bg='pink',font=("comicsansms",15,"bold")).pack() 
    mydb.commit()    
    mydb.close()             

def start():
    global screen8
    screen8=Toplevel(root)
    starttime=datetime.date.today()
    screen2.destroy()
    screen8.title("Hospital")
    screen8.geometry("750x450")
    screen8.configure(background="green")
    Label(screen8,text="").pack()
    Label(screen8,text="starting time:"+str(starttime),font="comicsansms 15 bold",fg="black").pack()
    write=Label(screen8,text="Hospital Emergency Room Booking System",font="comicsansms 20 bold",fg="red")
    photo=PhotoImage(file="hospital.png",height=350)
    suren=Label(screen8,image=photo)
    b1=Button(screen8,text="Start",command=new,bg="red",font="comicsansms 19 bold")
    b1.pack(side=BOTTOM)
    suren.pack()
    write.pack()
    screen8.mainloop()

def usernotfound():
    global screen3
    screen3=Toplevel(root)
    screen3.title("usernotfound")
    screen3.geometry("150x100")
    Label(screen3,text="UserNotFound").pack()
    Button(screen3,text="OK",command=delete2).pack() 

def passwordincorrect():
    global screen3
    screen3=Toplevel(root)
    screen3.title("Passwordincorrect")
    screen3.geometry("150x100")
    Label(screen3,text="Password Incorrect").pack()
    Button(screen3,text="OK",command=delete2).pack()

def login():
    global screen2
    screen2=Toplevel(root)
    screen2.title("Register")
    screen2.geometry("300x250")
    screen2.configure(background="white")
    global username1,password1
    username1=StringVar()
    password1=StringVar()

    global usernameentry1,userpasswordentry1
    Label(screen2,text="Please enter details below to login",fg="white",bg="green",font=("comicsansms",8,"bold")).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Username",bg="green",fg="white").pack()
    usernameentry1=Entry(screen2,textvariable=username1)
    usernameentry1.pack()
    Label(screen2,text="Password",bg="green",fg="white").pack()
    userpasswordentry1=Entry(screen2,textvariable=password1,show="*")
    userpasswordentry1.pack()
  
    Label(screen2,text="").pack()
    Button(screen2,text="Submit",width=10,height=1,command=paswordverify,bg="red").pack()

def main_screen():
    global root
    root=Tk()    
    root.configure(background='white')
    root.geometry("644x434")
    root.title("Entertainment Console")
    Label(root,text="",bg="grey",width="300",height="1",font=("Calibri,13")).pack()
    Label(root,text="").pack()
    Button(root,text="Login",height="1",width="10",command=login,bg="green",fg="white",font=("comicsansms",20,"bold")).pack()
    Label(root,text="").pack()
    Button(root,text="Register",height="1",width="10",command=register,bg="green",fg="white",font=("comicsansms",20,"bold")).pack()
    root.mainloop()   

if __name__ == "__main__":

    main_screen()     