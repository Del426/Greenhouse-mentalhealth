# Import module 
from tkinter import *
import tkinter as tk

# Create object 
root = Tk()
  
# Adjust size 
root.geometry("400x400")
  
# Add image file
bg = PhotoImage( file = "test.gif")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
  
# Add text
label2 = Label( root, text = "Welcome")
  
label2.pack(pady = 50)
  
# Create Frame
frame1 = Frame( root,)
frame1.pack(pady = 20)
  
def Close():
    exit()

def Change():
    #i have no idea how to link animation to this
    print("IDK")


# Add buttons
button1 = Button( frame1, text = "Exit", command=Close)
button1.pack(pady = 20)
  
button2 = Button( frame1, text = "Start", command=Change)
button2.pack(pady = 20)
  

# Execute tkinter
root.mainloop()