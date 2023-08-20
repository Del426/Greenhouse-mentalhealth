from tkinter import *
print("hello world")


#window setup
import turtle            
wn = turtle.Screen()  
wn.setup(400,400)   
wn.bgpic("test.gif")
wn.mainloop()


#interative button
def click():
    if lab["text"] == "Hello":
        lab["text"]="Bye" 
    else:
        lab["text"]=="Hello"

root = Tk()
root.title("Hello")

lab =Label(root, text="Hello")
lab.pack()

button = Button(root, text="Click me", command=click)
button.pack()

root.mainloop()