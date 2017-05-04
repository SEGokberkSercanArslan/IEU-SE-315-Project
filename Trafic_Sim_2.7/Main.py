from Tkinter import *
import Functions
import Classes

def deneme():
    print "deneme"



#main root screen
root = Tk()
root.geometry("1024x768")
root.title("Trafic Simulator")
root.config(bg="grey")

#drawing screen on the root
canvas = Canvas(root,width=1024,height=400)
canvas.config(bg="white")
#canvas.bind("<Button-1>",Functions.onclick_handler)
#canvas.bind("<ButtonRelease-1>",Functions.onrelease_handler)
canvas.pack()
canvas.place(y=200)



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


print "Merhaba dünya"


'''
button = Button(root,text="Line Road",command=Functions.create_line(root_canvas=canvas))
button.place(x=70,y=0)
'''

#button2 = Button(root,text="Curve road",command=Functions.create_curve(root_canvas=canvas))
#button2.place(x=0,y=0)


root.config(menu=menubar)
root.mainloop()