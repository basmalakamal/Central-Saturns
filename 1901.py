import math
from vpython import *
from datetime import date
import datetime, time



G = 6.674 * math.pow(10,-11)
sunM = 1.989 * math.pow(10,30)
date1 = input("Enter that latest date as %d/%m/%Y")
date2 = input("Enter that first date as %d/%m/%Y")
date_format = "%d/%m/%Y"
a = datetime.datetime.strptime(date1, date_format)
b = datetime.datetime.strptime(date2, date_format)
delta = a - b
ndays = delta.days
seconds = int(ndays)*24*60*60
class planet(object):
    def __init__(self,name,mass,RS,theta0,radius):
        self.name = name
        self.mass = mass
        self.RS = RS
        self.theta0 = theta0
        self.radius = radius
    def gravitationalForce(self):
        return G * (self.mass*sunM)/math.pow(self.RS,2)
    def angularVelocity(self):
        return math.sqrt(self.gravitationalForce()/(self.mass*self.RS))
    def angularPosition(self,t):
        return self.theta0 + self.angularVelocity() * t
    def varAngularPosition(self,t,dt):
        return self.angularPosition(t+dt)-self.angularPosition(t)

mercury = planet("Mercury",3.302 * math.pow(10,23),57910000000,0,0.3)
venus = planet("Venus",4.8685 * math.pow(10,24),108200000000,0,0.4)
earth = planet("Earth",5.973 * math.pow(10,24),149600000000,0,0.5)
mars = planet("Mars",6.4185 * math.pow(10,23),227900000000,0,0.45)
jupiter = planet("Jupiter",1.8986 * math.pow(10,27),778500000000,0,.8)
saturn = planet("Saturn",5.6846 * math.pow(10,26),1433000000000,0,0.7)
uranus = planet("Uranus",8.6832 * math.pow(10,25),2877000000000,0,0.6)
neptune = planet("Neptune",1.0243 * math.pow(10,26),4503000000000,0,0.6)


# Planets
mercpla = sphere(pos=vector(1.5,0,0),color=color.white,radius=0.3,make_trail=True)
venpla = sphere(pos=vector(3,0,0),color=color.orange,radius=0.4,make_trail=True)
eapla = sphere(pos=vector(5,0,0),color=color.magenta,radius=0.5,make_trail=True)
marpla = sphere(pos=vector(7,0,0),color=color.red,radius=0.45,make_trail=True)
juppla = sphere(pos=vector(9,0,0),color=color.cyan,radius=0.8,make_trail=True)
satpla = sphere(pos=vector(11,0,0),color=color.yellow,radius=0.7,make_trail=True)
urpla = sphere(pos=vector(13,0,0),color=color.green,radius=0.6,make_trail=True)
neppla = sphere(pos=vector(15,0,0),color=color.purple,radius=0.6,make_trail=True)
masscenter = sphere(pos=vector(0,0,0),color=color.blue,radius=0.1,make_trail=True)
planetsf = [mercpla,venpla,eapla,marpla,juppla,satpla,urpla,neppla]
planets = [mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
# Our program
t = 0
dt = 100000

while t < seconds:
    rate(70)
    for plan in range(len(planets)):
        planetsf[plan].pos = rotate(planetsf[plan].pos,angle=planets[plan].varAngularPosition(t,dt),axis=(vector(0,0,1)))
        t = t + dt
        centerx = (mercury.mass*mercpla.pos.x + venus.mass*venpla.pos.x + earth.mass*eapla.pos.x + mars.mass*marpla.pos.x + jupiter.mass*juppla.pos.x + saturn.mass*satpla.pos.x + uranus.mass*urpla.pos.x + neptune.mass*neppla.pos.x) /(mercury.mass + venus.mass + earth.mass + mars.mass + jupiter.mass + saturn.mass + uranus.mass + neptune.mass + sunM)
        centery = (mercury.mass*mercpla.pos.y + venus.mass*venpla.pos.y + earth.mass*eapla.pos.y + mars.mass*marpla.pos.y + jupiter.mass*juppla.pos.y + saturn.mass*satpla.pos.y + uranus.mass*urpla.pos.y + neptune.mass*neppla.pos.y) /(mercury.mass + venus.mass + earth.mass + mars.mass + jupiter.mass + saturn.mass + uranus.mass + neptune.mass + sunM)
        masscenter.pos = vector(centerx,centery,0)
