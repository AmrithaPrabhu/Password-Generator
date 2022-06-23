from tkinter import *
import string
import random


#function for creating password
def createPassword():
     lengthPassword = int(lengthbox.get())
     #print(lengthPassword)
     password=""
     passWord.delete(0,END)
     for i in range(lengthPassword):
        if(ch.get()==3):
          password += random.choice(string.ascii_letters + string.digits+string.punctuation)
        elif(ch.get()==2):
            password += random.choice(string.ascii_letters + string.digits)
        elif(ch.get()==1):
            password += random.choice(string.ascii_letters)
     passWord.insert(0,password)
     #print(password)


#function for copying password
def copyPassword():
    passWord.clipboard_clear()
    passWord.clipboard_append(passWord.get())


front=Tk()
front.title("Password Generator")
front.configure(background="black")
front.geometry("430x500")

#choice variable for weak,medium,strong password
ch=IntVar()

title=Label(front,text="Password Generator",font=("Arial",30,'bold'),bg="black",fg="white",justify='center')
title.grid()

#weak radio button
weak=Radiobutton(front,text="Weak",variable=ch,value=1,bg="white",fg="black",font=("Arial",15,'bold'))
weak.grid(pady=10)

#medium radio button
medium=Radiobutton(front,text="Medium",variable=ch,value=2,bg="white",fg="black",font=("Arial",15,'bold'))
medium.grid(pady=10)

#strong radio button
strong=Radiobutton(front,text="Strong",variable=ch,value=3,bg="white",fg="black",font=("Arial",15,'bold'))
strong.grid(pady=10)

#determining length of the password
length=Label(front,text="Length of Password",font=("Arial",15,'bold'),bg="black",fg="white")
length.grid(pady=10)
lengthbox=Spinbox(front,from_=6,to=20,width=5,font=("Arial",15,'bold'))
lengthbox.grid()

#button for generating password
generate=Button(front,text="Generate",font=("Arial",15,'bold'),bg="white",fg="black",command=createPassword)
generate.grid(pady=20)

#Entry field for showcasing the password
passWord=Entry(front,width=25,font=("Arial",15,'bold'),bg="white",fg="black")
passWord.grid(pady=10)

#button for copying password
copy=Button(front,text="Copy",font=("Arial",15,'bold'),bg="white",fg="black",command=copyPassword)
copy.grid(pady=10)


text=Text(front)
text.tag_configure("center",justify="center")


front.mainloop()