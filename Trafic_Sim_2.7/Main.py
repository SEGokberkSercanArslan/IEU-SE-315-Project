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
#tool_menu.add_command(label="Arc",command=Functions.create_arc(canvas))
menubar.add_cascade(label="Tools",menu=tool_menu)
#End of menu functions



#Right Click Pop up tool menu
popup = Menu(root,tearoff=0)
popup.add_command(label="Line Tool",command=Functions.create_line)
popup.add_command(label="Arc  Tool",command=Functions.create_arc)
popup.add_separator()
popup.add_command(label="Road Attr")
popup.add_separator()

def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()
root.bind("<Button-3>",do_popup)


button1= Button(root,text="Red Light Timer",bg="grey",fg="white")
button1.grid(row=0,column=0,ipadx=80)
entry1 = Entry(root,bg="white",fg="black")
entry1.grid(row=0,column=1)

button2= Button(root,text="Green Light Timer",bg="grey",fg="white")
button2.grid(row=1,column=0,ipadx=80)
entry2 = Entry(root,bg="white",fg="black")
entry2.grid(row=1,column=1)

button3= Button(root,text="Max Capacity",bg="grey",fg="white")
button3.grid(row=2,column=0,ipadx=80)
entry3 = Entry(root,bg="white",fg="black")
entry3.grid(row=2,column=1)

button4= Button(root,text="Max Pass Per Min",bg="grey",fg="white")
button4.grid(row=3,column=0,ipadx=80)
entry4 = Entry(root,bg="white",fg="black")
entry4.grid(row=3,column=1,padx=40)


label_road_number = Label(root,bg="grey",fg="black",text="Road Number :")
label_road_number.grid(row=0,column=2)

label_road_rl_info = Label(root,bg="grey",fg="black",text="Road Red Light :")
label_road_rl_info.grid(row=1,column=2)

label_road_gl_info = Label(root,bg="grey",fg="black",text="Road Green Light :")
label_road_gl_info.grid(row=2,column=2)

label_max_road_cap = Label(root,bg="grey",fg="black",text="Max Vehicle Capacity :")
label_max_road_cap.grid(row=3,column=2)

label_max_veh_pass = Label(root,bg="grey",fg="Black",text="Max Vehicle Pass :")
label_max_veh_pass.grid(row=4,column=2)





root.config(menu=menubar)
root.mainloop()