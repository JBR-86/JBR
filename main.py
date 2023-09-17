from tkinter import *
from PIL import ImageTk 
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        # background Image
        self.bg=ImageTk.PhotoImage(file="1.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=8,relwidth=1,relheight=1)

        # Login Frame
        Frame_login = Frame(self.root,bg="white")
        Frame_login.place(x=330,y=150,width=500,height=400,)

        # Titte Frame
        title = Label(Frame_login, text="Login Here", font=("Droid Sans Mono",35,"bold"), fg="#6162ff",bg="white").place(x=90,y=30)
        subtitle = Label(Frame_login, text="Members Login Area", font=("Droid Sans Mono",15,"bold"), fg="#1d1d1d",bg="white").place(x=90,y=100)

        # username
        lbl_user = Label(Frame_login, text="Username", font=("Droid Sans Mono",15,"bold"), fg="grey",bg="white").place(x=90,y=140)
        self.username = Entry(Frame_login, font=("Droid Sans Mono",15),bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320,height=35)

        # password
        lbl_password = Label(Frame_login, text="Password", font=("Droid Sans Mono",15,"bold"), fg="grey",bg="white").place(x=90,y=210)
        self.password = Entry(Frame_login, font=("Droid Sans Mono",15),bg="#E7E6E6")
        self.password.place(x=90,y=240, width=320,height=35)

        # Button
        forget = Button(Frame_login, text="Forgot password?",bd=0, font=("Droid Sans Mono",12), fg="#6162ff",bg="white").place(x=90,y=280)
        submit = Button(Frame_login,command=self.check_function, text="Login",bd=0, font=("Droid Sans Mono",15), bg="#6162ff",fg="white").place(x=90,y=320,width=180,height=40)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error:" "All fields are required",parent=self.root)
        elif self.username.get() != "JBR" or self.password.get() != "123123":
            messagebox.showerror("Error:" "Invalid Username or Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.username.get()}")

root = Tk()
obj = Login(root)
root.mainloop()