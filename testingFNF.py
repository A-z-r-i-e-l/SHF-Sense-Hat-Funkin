import anvil.server
from anvil.tables import app_tables
from sense_emu import SenseHat
import time
from time import sleep
import random
from datetime import datetime

running = True

sense =  SenseHat()
sense.clear()



class arrow:
    def __init__(self):
        self.y_position = 7
        self.x_position = random.randint(0, 3)
        print("An arrow has been made")

    def display(self, color):
        sense.set_pixel(self.x_position, self.y_position, color)
    
    def move(self):
        global running
        if self.y_position>0 and self.y_position <=7:
            self.y_position = self.y_position - 1
        else:
            None

    def run(self):
        r = (255, 200, 21)
        self.display(r)
        time.sleep(1)
        k = (0, 0, 0)
        self.display(k)
        self.move()

#----------------------------------------------------------------------------------
class Catcher1:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        g = (0, 255, 0)
        self.display(g)
        print("Catcher1 has been made")

    def display(self, color):
        sense.set_pixel(self.x_position, self.y_position, color)

    def move(self, direction):
        self.x_position = self.x_position + direction

    def run(self):
        k = (0, 0, 0)
        self.display(k)
        g = (0, 255, 0)
        self.display(g)

#----------------------------------------------------------------------------------
class Catcher2:
    def __init__(self):
        self.x_position = 1
        self.y_position = 0
        g = (255, 0, 0)
        self.display(g)
        print("Catcher2 has been made")

    def display(self, color):
        sense.set_pixel(self.x_position, self.y_position, color)

    def move(self, direction):
        self.x_position = self.x_position + direction

    def run(self):
        k = (0, 0, 0)
        self.display(k)
        g = (255, 0, 0)
        self.display(g)
        #print(event)        

#----------------------------------------------------------------------------------
class Catcher3:
    def __init__(self):
        self.x_position = 2
        self.y_position = 0
        g = (0, 255, 0)
        self.display(g)
        print("Catcher3 has been made")

    def display(self, color):
        sense.set_pixel(self.x_position, self.y_position, color)

    def move(self, direction):
        self.x_position = self.x_position + direction

    def run(self):
        k = (0, 0, 0)
        self.display(k)
        g = (0, 0, 255)
        self.display(g)

#----------------------------------------------------------------------------------
class Catcher4:
    def __init__(self):
        self.x_position = 3
        self.y_position = 0
        g = (255, 0, 0)
        self.display(g)
        print("Catcher4 has been made")

    def display(self, color):
        sense.set_pixel(self.x_position, self.y_position, color)

    def move(self, direction):
        self.x_position = self.x_position + direction

    def run(self):
        k = (0, 0, 0)
        self.display(k)
        g = (255, 0, 255)
        self.display(g)
        #print(event)        


my_arrow = arrow()
my_catcher1 = Catcher1()
my_catcher2 = Catcher2()
my_catcher3 = Catcher3()
my_catcher4 = Catcher4()
score = 0

while running == True:
    my_arrow.run()
    my_catcher1.run()
    my_catcher2.run()
    my_catcher3.run()
    my_catcher4.run()
    for event in sense.stick.get_events():
        if (event.action == "pressed" and event.direction == "left") and (my_arrow.y_position == my_catcher1.y_position):
            score += 1
            print(score)
            time.sleep(1)
            my_arrow = arrow()
        
        if (event.action == "pressed" and event.direction == "up") and (my_arrow.y_position == my_catcher2.y_position):
            score += 1
            print(score)
            time.sleep(1)
            my_arrow = arrow()
        if (event.action == "pressed" and event.direction == "down") and (my_arrow.y_position == my_catcher3.y_position):
            score += 1
            print(score)
            time.sleep(1)
            my_arrow = arrow()
        
        if (event.action == "pressed" and event.direction == "right") and (my_arrow.y_position == my_catcher4.y_position):
            score += 1
            print(score)
            time.sleep(1)
            my_arrow = arrow()