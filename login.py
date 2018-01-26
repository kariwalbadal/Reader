from tkinter import *
import tkinter.messagebox as tm
import imaplib
from main import main
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0)
        self.label_2.grid(row=1)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)


        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()


    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)

        #if username == "john" and password == "password":
         #   tm.showinfo("Login info", "Welcome John")
        #else:
         #   tm.showerror("Login error", "Incorrect username or password")
        imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        
        try:
            imap.login(username, password)
            tm.showinfo("Login Successful", "You have logged in successfully")
            root.destroy()
            main(username, password)
        except Exception as e:
            tm.showerror("Login Error", "Username or password incorrect")
            


root = Tk()
lf = LoginFrame(root)
root.mainloop()
