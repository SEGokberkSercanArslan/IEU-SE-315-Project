
from Tkinter import *
from Classes import *
start = None

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
    global start
    if start is not None:
        x = start[0]
        y = start[1]
        event.widget.create_line(x, y, event.x, event.y)
        #Function Test
        m =Road_object(start[0],start[1],event.x,event.y)
        print "fPOSx:{}".format(m.get_fposx())
        print "fPOSy:{}".format(m.get_fposy())
        print "sPOSx:{}".format(m.get_sposx())
        print "sPOSy:{}".format(m.get_sposy())
        start = None

def onrelease_handler_arc(event):
    global  start
    if start is not None:
        x = start[0]
        y = start[1]
        event.widget.create_arc(x, y, event.x, event.y)
def create_line(root_canvas):
    root_canvas.bind("<Button-1>",onclick_handler)
    root_canvas.bind("<ButtonRelease-1>",onrelease_handler_line)



def create_arc(root_canvas):
    root_canvas.bind("<Button-1>",onclick_handler)
    root_canvas.bind("<ButtonRelease-1>",onrelease_handler_arc)
