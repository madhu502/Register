
from atexit import register
from tkinter import *
import sqlite3
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Register:
    def __init__(self,root) :
        self.root=root
        self.root.title("Register")
        self.root.geometry("1700x900+0+0")



# bg image

        my_image=Image.open("a1.jpg")
        resized_image=my_image.resize((1550,800))

        self.bg=ImageTk.PhotoImage(resized_image)
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        

# left image
        my_image=Image.open("stu.png")
        resized_image=my_image.resize((500,700))
        
        self.bg1=ImageTk.PhotoImage(resized_image)
        bg1_lbl=Label(self.root,image=self.bg1)
        bg1_lbl.place(x=50,y=100,width=470,height=520)


######### main frame ########
       
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)


####### labels and Entry ######
        
        fname=Label(frame, text="First Name",font=("times of roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,font=("times new  roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)


#######______row1########
        lname=Label(frame, text="Last Name",font=("times of roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)


#########_------row2
 
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)


        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
         
        self.txt_email=ttk.Entry(frame,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

#_------row3-----

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        
        security_A=Label(frame,text="Select Security Answers",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

##-----row4---
          

       

if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
   








