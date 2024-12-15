from tkinter import*
window = Tk()
window.geometry("400x400")
window.title("Login")
window.config(background="orange")
# creating labels

username = Label(window,text="Username",bg="blue")
username.place(x=100,y=100)
user_name_input=Entry(window,width=40)
user_name_input.place(x=190,y=100)

password = Label(window,text="Pssword",bg="blue")
password.place(x=100,y=200)

user_password = Entry(window,width=40)
user_password.place(x=190,y=200)

# bd is border
button = Button(window,text="Submit",bd=5,bg="purple")
button.place(x=100,y=300)


window.title("Button.py")
button = Button(window,text="Click here",background="red",bd=5,activebackground="white",activeforeground="green",command=window.destroy)
button.pack(side="bottom")




menubar = Menu(window)

# Adding File menu
file = Menu(menubar)
menubar.add_cascade(label = 'File' , menu = file)
file.add_cascade(label = "New File" , command=None)
file.add_cascade(label = "Open" , command=None)
file.add_cascade(label = "Save" , command=None)
file.add_separator()
file.add_cascade(label = "Exit" , command=window.destroy)

# Adding Edit bar
edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Edit" , menu=edit)
edit.add_cascade(label = "Cut" , command=None)
edit.add_cascade(label = "Copy" , command=None)
edit.add_cascade(label = "Paste" , command=None)
edit.add_cascade(label = "Select All" , command=None)
edit.add_cascade(label = "Find" , command=None)
edit.add_cascade(label = "Replace" , command=None)

# Adding Help bar
help = Menu(menubar,tearoff=1)
menubar.add_cascade(label = "Help" , menu=help)
help.add_cascade(label = "Take Help",command=None)
help.add_cascade(label = "Exit" , command=window.destroy)






window.config(menu=menubar)



window.mainloop()
