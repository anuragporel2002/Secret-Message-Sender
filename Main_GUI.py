#Secret Email Sender
#Import Libraries
import random
import smtplib
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

#Global Database for whole Applicatction
global db
db={"user_1":"pass_1",
    "user_2":"pass_2"
    }

#Basic Function
def Encrypt(text,l,u,p):
    encrypted_text=""
    #traversal
    for i in range(len(text)):
        temp=text[i]
        #Uppercase
        if temp.isupper():
            encrypted_text += chr((ord(temp) + u-65) % 26 + 65)
        #Lower and others
        elif temp.islower():
            encrypted_text += chr((ord(temp) + l-97) % 26 + 97)
        else:
            encrypted_text += chr((ord(temp) + p-32) % 26 + 32)
    return encrypted_text
def Decrypt(text,l,u,p):
    decrypted_text=""
    #traversal
    for i in range(len(text)):
        temp=text[i]
        #Uppercase
        if temp.isupper():
            decrypted_text += chr((ord(temp) - u-65) % 26 + 65)
        #Lower and others
        elif temp.islower():
            decrypted_text += chr((ord(temp) - l-97) % 26 + 97)
        else:
            decrypted_text += chr((ord(temp) - p-32) % 26 + 32)
    return decrypted_text
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender email id', 'password')
    server.sendmail('sender email id', to, content)
    server.close()

#Function For Initial Login
def login():
    forget_login_window()
    next_window()
def checkLogin():
    username = the_user.get()
    password=the_pass.get()
    if (username in db) and db[username]==password:
        login()
    else:
        showinfo("Error","Access Denied")
def forget_login_window():  # forget all the grid items.
    username_1.place_forget()
    password_1.place_forget()
    myLabel1.place_forget()
    myLabel2.place_forget()
    Butlog.place_forget()
def next_window():
    global rcv, msg, receiver
    rcv=StringVar()
    root.geometry("650x600")
    msg=Text(root,width=60, height=33,bd=5)
    msg.place(x=2,y=50)
    Lab1=Label(root, text="To:", background='lightblue',font=("consolas",13,'bold'))
    Lab1.place(x=2,y=2)
    receiver=Entry(root, textvariable=rcv,width=55,bd=5,font=("consolas",11,'bold'))
    receiver.place(x=40,y=2)
    buten=Button(root,padx=28,pady=5,bd=5,bg='white',text="Encrypt\n& Send",font=("Courier New",13,'bold'),command=Encode)
    buten.place(x=500,y=2)
    butde=Button(root,padx=28,pady=5,bd=5,bg='white',text="Decrypt",font=("Courier New",13,'bold'),command=Decode)
    butde.place(x=500,y=70)

#Button Function
def Decode():
    global msg
    key = askstring('Secret Key', 'Your Secret Key')
    l=key.split("-")
    text=msg.get("1.0",'end-1c')
    de=Decrypt(text,int(l[0]),int(l[1]),int(l[2]))
    msg.delete("1.0",END)
    msg.insert(END,de)
def Encode():
    global msg,rcv,receiver
    to=rcv.get()
    key = askstring('Secret Key', 'Encryption Key')
    l=key.split("-")
    text=msg.get("1.0",'end-1c')
    en=Encrypt(text,int(l[0]),int(l[1]),int(l[2]))
    msg.delete("1.0",END)
    msg.insert(END,en)
    try:
        sendEmail(to,en)
        receiver.delete(0,END)
        showinfo("Success","Message Sent Successfully!")
    except:
        showinfo("Failed","Unable to Send!")
    
    
    


#Tkinter Widget
root=Tk()
root.title("Secret Message Sender v1.0")
root.geometry("700x600")

# StringVars
the_user = StringVar()  # used to retrieve input from entry
the_pass = StringVar()

##########################################Initial Login Page#########################################
myLabel1 = Label(root, text="Username :", background='lightblue',font=("consolas",13,'bold'))
myLabel1.place(x=150,y=200)
myLabel2 = Label(root, text="Password :", background='lightblue',font=("consolas",13,'bold'))
myLabel2.place(x=150,y=230)
# Entry fields
username_1 = Entry(root, textvariable=the_user,width=40,bd=4,font=("consolas",11,'bold'))
username_1.place(x=250,y=200)
password_1 = Entry(root, show='*', textvariable=the_pass,width=40,bd=4,font=("consolas",11,'bold'))
password_1.place(x=250,y=230)
#Buttons
Butlog=Button(root,padx=10,pady=3,bd=4,bg='white',text="Login",font=("Courier New",11,'bold'),command=checkLogin)
Butlog.place(x=350,y=260)

root.mainloop()
