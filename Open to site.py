print("hello world")

import turtle            
wn = turtle.Screen()     
alex = turtle.Turtle()        
for _ in range(3600):
    alex.forward(1)
    alex.right(1)

wn.bgpic("test.gif")
wn.mainloop()
