from Tkinter import *
from itertools import count

class Road_object():
    _ids=count(0)

    def __init__(self,fposx,fposy,sposx,sposy):
        self.first_posx=fposx
        self.first_posy=fposy
        self.second_posx=sposx
        self.second_posy=sposy
        self.id=self._ids.next()
    def initialize_redlight_timer(self,red_light):
        self.red_light_timer=red_light
    def initialize_greenlight_timer(self,green_light):
        self.green_light_timer=green_light
    def initialize_max_capacity(self,max_road_cap):
        self.max_road_capacity=max_road_cap
    def initialize_max_pass(self,max_pass):
        self.max_veheicle_pass=max_pass
    def get_fposx(self):
        return self.first_posx
    def get_fposy(self):
        return self.first_posy
    def get_sposx(self):
        return self.second_posx
    def get_sposy(self):
        return self.second_posy
    def get_red_light_timer(self):
        return self.red_light_timer
    def get_green_light_timer(self):
        return self.green_light_timer
    def get_max_road_cap(self):
        return self.max_road_capacity
    def get_max_vehicle_pass(self):
        return self.max_veheicle_pass
    def get_current_number_of_roads(self):
        return self.id


