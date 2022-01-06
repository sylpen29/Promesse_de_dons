from tkinter import *
from functools import partial

def form_login(login, password):
	print(" Pseudo :", login.get())
	print("Mot de passe :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x200')  
tkWindow.title('Formulaire Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Utilisateur").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Mot de passe").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(form_login, username, password)

#login button
loginButton = Button(tkWindow, text="Envoyer", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()