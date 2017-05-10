
from Tkinter import *
from Classes import *
start = None
road_id = 0
road = {}


def instructions():
    root_inst = Tk()
    root_inst.geometry("800x640")
    root_inst.title("instrucitons")
    label =Label(root_inst,text = "instructions will be come here!")
    label.pack()
    root_inst.mainloop()


def key_locactions(event):
    repr(event.char)

def call_back_test(event):
    print "Placed :",event.x,event.y


def onclick_handler(event):
    global start
    start = (event.x, event.y)

def onrelease_handler_line(event):
    global start , road_id
    if start is not None:
        x = start[0]
        y = start[1]
        event.widget.create_line(x, y, event.x, event.y)
        road[road_id] = Road_object(start[0],start[1],event.x,event.y)   #Create an object called road
        road_id+=1
        print repr(road) #adress test
        start = None

def onrelease_handler_arc(event):
    global  start , road_id
    if start is not None:
        x = start[0]
        y = start[1]
        event.widget.create_arc(x, y, event.x, event.y)
        road[road_id] = Road_object(start[0], start[1], event.x, event.y)  # Create an object called road dynmicly
        road_id+=1  #increase road id pointer

def create_line(root_canvas):
    root_canvas.bind("<Button-1>",onclick_handler)
    root_canvas.bind("<ButtonRelease-1>",onrelease_handler_line)



def create_arc(root_canvas):
    root_canvas.bind("<Button-1>",onclick_handler)
    root_canvas.bind("<ButtonRelease-1>",onrelease_handler_arc)



def simultate_roads():
    global road
    pass    #fill after development