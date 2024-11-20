#5/28/24
'''
from  tkinter import *

#create a window
window= Tk()
#add a text box
text= Label(window,text="GUIs in Python are pretty easy!")
text.pack()
#loop until user closes window
window.mainloop()
print("ASDF") #will print after you close the Tk window

------------------------------------------------------------

from tkinter import *

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(master, text="BYE!", fg="red",command=self.quit)
        self.button1.pack(side=LEFT)
        self.button2 = Button(master, text="Say someting!", command=self.say)
        self.button2.pack(side= LEFT)
    def say(self):
        print("Froot Loops")
        self.button2.config(text = "I SAID SOMETING", fg="blue")

##MAIN PROGRAM###
window = Tk()
app = App(window)
window.mainloop()

----------------------------------------------------------


# Importing tkinter module
from tkinter import *
# from tkinter.ttk import *
 
# creating Tk window
master = Tk()
 
# creating a Frame which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)
 
# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text = "Click me !", background = "red", fg = "white")
b1.pack(side = TOP, expand = True, fill = BOTH)
 
# Button 2
b2 = Button(pane, text = "Click me too", background = "blue", fg = "white")
b2.pack(side = TOP, expand = True, fill = BOTH)
 
# Button 3
b3 = Button(pane, text = "I'm also button", background = "green", fg = "white")
b3.pack(side = TOP, expand = True, fill = BOTH)


# Execute Tkinter
master.mainloop()

----------------------------------------------------------


from tkinter import *

class click(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.Button1 = Button(master, text = "DONT CLICK!", bg = "red", fg= "black", command = self.img)
        self.Button1.pack(side = LEFT, expand = True, fill= BOTH)

        self.Button2 = Button(master, text = "Click this one", bg = "green", fg = "black", command = self.second)
        self.Button2.pack(side = LEFT, expand = True, fill= BOTH)          

    def img(self):
        self.image = PhotoImage(file = "room.gif")
        self.Button1.config(image = self.image)
        
        
    def second(self):
        print("Looser")
        self.Button2.config(text = "You are a Sheep", bg = "black", fg = "white")
    
#Execute
     
window= Tk()
app = click(window)
window.mainloop()

-----------------------------------------------------------  


#GUI can create grid style using cordinates ex: (row= 1, column= 0)

from tkinter import *
class App(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.label1 = Label(window, text='Email:', bg='#E200E6')
        self.label2 = Label(window, text='Password:', bg='#E200E6')
        self.label1.grid(row=0, column=0) #increase sixe by using number of pixles ex:(oval(100,40,40,100)
        self.label2.grid(row=1, column=0)
        self.emailBox = Entry(window)
        self.pwBox = Entry(window)
        self.emailBox.grid(row=0, column=1)
        self.pwBox.grid(row=1, column=1)
        self.loginBtn = Button(window, text='Login', command=None)
        self.loginBtn.grid(row=2, columnspan=2)

window = Tk()
window.title("Adding an Image")
g = App(window)
window.config(bg='#E200E6')

window.mainloop()

------------------------------------------------------------
'''


