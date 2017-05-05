from Tkinter import *
import Functions
import Classes

def deneme():
    print "deneme"


root=Tk()
root.geometry("1600x1000")
root.title("Trafic Simulator")
root.config(bg="grey")

#create a frame working on canvas
frame=Frame(root,width=800,height=400)
frame.place(y=250)


canvas=Canvas(frame,bg='#FFFFFF',width=800,height=800,scrollregion=(0,0,2880,1440))
#Horizental Scroll Bar
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
#Vertical Scroll Bar
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
#Canvas Creation
canvas.config(width=1580,height=500,bg="white")
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)


#Create Menu
menubar = Menu(root)
#File operation menu
file_menu = Menu(menubar,tearoff=0)
file_menu.add_command(label = "Open",command = deneme)
file_menu.add_command(label = "Save Project",command =deneme)
file_menu.add_command(label = "Quit",command = root.quit)
file_menu.add_separator()
menubar.add_cascade(label = "File",menu = file_menu)
#Simulation menu
simultate_menu = Menu(menubar,tearoff=0)
simultate_menu.add_command(label = "Simultate",command = deneme)
menubar.add_cascade(label = "Simutlate",menu = simultate_menu)
#Help menu and menu's members
help_menu = Menu(menubar,tearoff=0)
help_menu.add_command(label = "instructions",command = Functions.instructions )
menubar.add_cascade(label = "Help",menu = help_menu)
#Tool menu
tool_menu= Menu(menubar,tearoff=0)
tool_menu.add_command(label="Line",command=Functions.create_line(canvas))
tool_menu.add_command(label="Arc",command=Functions.create_arc(canvas))
menubar.add_cascade(label="Tools",menu=tool_menu)
#End of menu functions



#Right Click Pop up tool menu
popup = Menu(root,tearoff=0)
popup.add_command(label="Line Tool")
popup.add_command(label="Arc  Tool")
popup.add_command(label="Road Attr")
popup.add_separator()




root.config(menu=menubar)
root.mainloop()