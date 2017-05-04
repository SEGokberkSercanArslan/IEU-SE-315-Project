from Tkinter import *

class Road_object():
    def __init__(self,max_cap,gl_timer,rl_timer,max_veh_pass):
        self.red_light =rl_timer
        self.green_light =gl_timer
        self.road_capacity= max_cap
        self.maximum_vehicle_pass=max_veh_pass
    def printattributes(self):
        print self.red_light
        print self.green_light
        print self.road_capacity
    def initialize_event_pos(self,fepx,fepy,sepx,sepy):
        #fepx=First  event x pixel location
        #fepy=First  event y pixel location
        #sepx=Second event x pixel location
        #sepy=Second event y pixel location
        self.first_event_posx=fepx
        self.first_event_posy=fepy
        self.second_event_posx=sepx
        self.second_event_posy=sepy
    def road_attribute_screen(self):
        road_root = Tk()
        road_root.geometry("600x600"),
        road_root.title("Attribute initialize screen")

        #Entry boxes and save buttons will come here !!


        road_root.mainloop()
