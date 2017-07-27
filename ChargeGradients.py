# Circuit Charge Gradient Simulation
# Physics 131
# J.J. Strnad
# Spring 2013

from visual import *
from visual.graph import *

Scene = display( title = "Circuit Charge Gradient Simulation", x=0, y=0, width = 1200, height = 750,
                 center = (0,-50,0), range = (140,80,100), background = (.2, .2, .2))
Scene.autoscale = false


#Constants
q = 1.6e-19
k = 8.99e-9
Dscale = 1e-1
m = 9.09e-31
dt = 1e-11

DragForce1 = 3.5e-22  
DragForce2 = 1.4e-23 
DragForce3 = 5e-24 
DragForce4 = DragForce2 + .3e-23
DragForce5 = 1.35e-22
             
NegDragForce1 = 3e-22  
NegDragForce2 = 1.5e-23 
NegDragForce3 = 5e-24 
NegDragForce4 = DragForce2 + .3e-23
NegDragForce5 = -1.35e-22


#Dimensions
TopLeft = vector(-75, 1.5, 0.5)

""" Battery """
batteryPos = cylinder(pos = (-30,0,0), axis = (30,0,0), radius = 11, color = (.804,.149,.149))
batteryNeg = cylinder(pos = (0,0,0), axis = (30,0,0), radius = 11, color = (.5,.5,.5))

label(pos=(-15,0,0), text='+')
label(pos=(15,0,0), text='-')

""" Boxes """
# underneath boxes
boxU1 = box(pos = TopLeft + (0, -1.5, -1.5), axis = (90,0,0), height = 3, width = .5, color = (1,.725,.0588))
boxU4 = box(pos = (118.5,-60,-1), axis = (0,120,0), height = 3, width = .5, color = (1,.725,.0588))

boxU2 = box(pos = (-118.5, -59.25, -1), axis = (0,121.5,0), height = 3, width = .5, color = (1,.725,.0588))
boxU5 = box(pos = (75,0,-1), axis = (90,0,0), height = 3, width = .5, color = (1,.725,.0588))

boxU3 = box(pos = (0,-118.5,-1), axis = (240,0,0), height = 3, width = .5, color = (1,.725,.0588))

# side boxes
boxB3 = box(pos = (0,-120,0.5), axis = (240,0,0), height = .5, width = 3, color = (1,1, 0))
boxB1 = box(pos = TopLeft + (1.5, -3,0), axis = (87,0,0), height = .5, width = 2, color = (1,1,0))
boxB5 = box(pos = (73.5, -1.5, 0), axis = (87,0,0), height = .5, width = 2, color = (1,1,0))

boxL2 = box(pos = (-120,-59.25,0.5), axis = (0,121.5,0), height = .5, width = 3, color = (1,1,0))
boxL4 = box(pos = (117,-59.25,0.5), axis = (0,115.5,0), height = .5, width = 2, color = (1,1,0))

boxR4 = box(pos = (120, -59.25,0.5), axis = (0,121.5,0), height = .5, width = 3, color = (1,1,0))
boxR2 = box(pos = (-117, -59.25,0.5), axis = (0,115.5,0), height = .5, width = 2, color = (1,1,0))

boxT1 = box(pos = TopLeft, axis = (90,0,0), height = .5, width = 3, color = (1,1,0))
boxT5 = box(pos = (75,1.5,0.5), axis = (90,0,0), height = .5, width = 3, color = (1,1,0))
boxT3 = box(pos = (0,-117,0.5), axis = (234,0,0), height = .5, width = 2, color = (1,1, 0))



def checkWalls():
    #check L2
    if ((test.pos.x < 0) and (test.pos.y > (boxL2.pos.y - (boxL2.axis.y / 2))) and
        (test.pos.y < (boxL2.pos.y + (boxL2.axis.y / 2) -1)) and (test.pos.x < boxL2.pos.x)):
        test.momentum.x *= -1

    #check L4
    if ((test.pos.x > 115) and (test.pos.y > (boxL2.pos.y - (boxL2.axis.y / 2))) and
        (test.pos.y < (boxL2.pos.y + (boxL2.axis.y / 2))) and (test.pos.x < boxL2.pos.x)):
        test.momentum.x *= -1

    #check R2
    if ((test.pos.x < -115) and (test.pos.y > -117) and   
        (test.pos.y < (boxR2.pos.y + (boxR2.axis.y / 2)) -1) and (test.pos.x > boxR2.pos.x)):
        test.momentum.x *= -1

    #check R4
    if ((test.pos.x > 116) and (test.pos.y > -116) and
        (test.pos.y < -1.5) and (test.pos.x < boxR4.pos.x)):
        test.momentum.x *= -1
    
    #check T1
    if ((test.pos.y > -60) and (test.pos.x > (boxT1.pos.x - (boxT1.axis.x / 2))) and
        (test.pos.x < (boxT1.pos.x + (boxT1.axis.x / 2))) and (test.pos.y > boxT1.pos.y)):
        test.momentum.y *= -1

    #check T3
    if ((test.pos.y < -60) and (test.pos.x > (boxT3.pos.x - (boxT3.axis.x / 2))) and
        (test.pos.x < (boxT3.pos.x + (boxT3.axis.x / 2))) and (test.pos.y > boxT3.pos.y)):
        test.momentum.y *= -1

    #check T5
    if ((test.pos.y > -60) and (test.pos.x > (boxT5.pos.x - (boxT5.axis.x / 2))) and
        (test.pos.x < (boxT5.pos.x + (boxT5.axis.x / 2))) and (test.pos.y > boxT5.pos.y)):
        test.momentum.y *= -1

    #check B1
    if ((test.pos.y > -60) and (test.pos.x > (boxB1.pos.x - (boxB1.axis.x / 2))) and
        (test.pos.x < (boxB1.pos.x + (boxB1.axis.x / 2))) and (test.pos.y < boxB1.pos.y)):
        test.momentum.y *= -1

    #check B3
    if ((test.pos.y < -60) and (test.pos.x > (boxB3.pos.x - (boxB3.axis.x / 2) -1)) and
        (test.pos.x < (boxB3.pos.x + (boxB3.axis.x / 2))) and (test.pos.y < boxB3.pos.y)):
        test.momentum.y *= -1

    #check B5
    if ((test.pos.y > -60) and (test.pos.x > (boxB5.pos.x - (boxB5.axis.x / 2))) and
        (test.pos.x < (boxB5.pos.x + (boxB5.axis.x / 2))) and (test.pos.y < boxB5.pos.y)):
        test.momentum.y *= -1


""" Positive Exterior Charges """
PositiveCharges = []
PosChgO = 1
PosChgI = 1
SizeStepI = 3
SizeStepO = 3
ChgStep = 1.5

#62 charges on each side
# Max charge: 191751, min charge: 1

for i in range(-5, -115, -10):
    Charge = sphere(pos = ( i, -122, 0), radius = .3 + (SizeStepO * .03), charge = PosChgO, color = color.red)
    PositiveCharges.append(Charge)
    SizeStepO += 1
    PosChgO = PosChgO * ChgStep

for i in range(-5, -115, -10):
    Charge = sphere(pos = ( i, -115, 0), radius = .3 + (SizeStepI * .03), charge = PosChgI, color = color.red)
    PositiveCharges.append(Charge)
    SizeStepI += 1
    PosChgI = PosChgI * ChgStep

for i in range(-110, -4, 10):
    Charge = sphere(pos = (-122, i, 0), radius = .3 + (SizeStepO * .03), charge = PosChgO, color = color.red)
    PositiveCharges.append(Charge)
    SizeStepO += 1
    PosChgO = PosChgO * ChgStep

for i in range(-110, -4, 10):
    Charge = sphere(pos = ( -115, i, 0), radius = .3 + (SizeStepI * .03), charge = PosChgI, color = color.red)
    PositiveCharges.append(Charge)
    SizeStepI += 1
    PosChgI = PosChgI * ChgStep

for i in range(-112, -30, 10):
    Charge = sphere(pos = (i, 3.5, 0), radius = .3 + (SizeStepO * .03), charge = PosChgO, color = color.red)
    PositiveCharges.append(Charge)
    SizeStepO += 1
    PosChgO = PosChgO * ChgStep

for i in range(-112, -30, 10):
    Charge = sphere(pos = (i, -3.5, 0), radius = .3 + (SizeStepI * .03), charge = PosChgI, color = color.red)
    PositiveCharges.append(Charge)
    SizeStepI += 1
    PosChgI = PosChgI * ChgStep


""" Negative Exterior Charges """
NegativeCharges = []
NegChgO = -1
NegChgI = -1
SizeStepO = 1
SizeStepI = 1

for i in range(5, 115, 10):
    Charge = sphere(pos = ( i, -122, 0), radius = .3 + (SizeStepO * .03), charge = NegChgO, color = color.blue)
    NegativeCharges.append(Charge)
    SizeStepO += 1
    NegChgO = NegChgO * ChgStep

for i in range(5, 115, 10):
    Charge = sphere(pos = ( i, -115, 0), radius = .3 + (SizeStepI * .03), charge = NegChgI, color = color.blue)
    NegativeCharges.append(Charge)
    SizeStepI += 1
    NegChgI = NegChgI * ChgStep

for i in range(-110, -4, 10):
    Charge = sphere(pos = (122, i, 0), radius = .3 + (SizeStepO * .03), charge = NegChgO, color = color.blue)
    NegativeCharges.append(Charge)
    SizeStepO += 1
    NegChgO = NegChgO * ChgStep

for i in range(-110, -4, 10):
    Charge = sphere(pos = ( 115, i, 0), radius = .3 + (SizeStepI * .03), charge = NegChgI, color = color.blue)
    NegativeCharges.append(Charge)
    SizeStepI += 1
    NegChgI = NegChgI * ChgStep

for i in range(112, 30, -10):
    Charge = sphere(pos = (i, 3.5, 0), radius = .3 + (SizeStepO * .03), charge = NegChgO, color = color.blue)
    NegativeCharges.append(Charge)
    SizeStepO += 1
    NegChgO = NegChgO * ChgStep

for i in range(112, 30, -10):
    Charge = sphere(pos = (i, -3.5, 0), radius = .3 + (SizeStepI * .03), charge = NegChgI, color = color.blue)
    NegativeCharges.append(Charge)
    SizeStepI += 1
    NegChgI = NegChgI * ChgStep
    

#Test Charge
sign = input("What test charge would you like to send through the circuit? Type 'p' for positron or 'e' for electron: ")

Q = 0

if (sign == 'e'):
    Q = -q
    TestColor = color.blue
    TestPos = (34,0,0)
else:
    Q = q
    TestColor = color.red
    TestPos = (-34,0,0)

test = sphere(pos = TestPos, velocity = vector(0,0,0), radius = 1.2, mass = m, charge = Q, momentum = vector(0,0,0), color = TestColor)

def Force():

    Fnet = vector(0,0,0)
    for i in NegativeCharges:
        r = (test.pos - i.pos) * Dscale
        rmag = mag(r)
        forceMag = (k * test.charge * i.charge) / (rmag ** 2)
        force = (forceMag / rmag) * r
        Fnet = Fnet + force
    
    for i in PositiveCharges: 
        r = (test.pos - i.pos) * Dscale
        rmag = mag(r)
        forceMag = (k * test.charge * i.charge) / (rmag ** 2)
        force = (forceMag / rmag) * r
        Fnet = Fnet + force
    return Fnet
    
t = 0
ForceList = []

def drag():
    fdrag= vector(0,0,0)
    if (sign == 'p'):
        if ((t > (3*dt)) and (test.pos.x < -32) and (test.pos.x > -116) and (test.pos.y > -3)):
            fdrag = DragForce1 * norm(Force()) 
        elif ((test.pos.x < -116) and (test.pos.y < -10) and (test.pos.y > -110)):
            fdrag.y = -DragForce2   
        elif ((test.pos.x > -105) and (test.pos.x < 105) and (test.pos.y < -116)):
            fdrag.x = DragForce3     
        elif ((test.pos.x > 116) and (test.pos.y < 10) and (test.pos.y > -110)):
            fdrag.y = DragForce4 
        elif ((test.pos.x > 30) and (test.pos.x < 116) and (test.pos.y > -3)):
            fdrag.x = -DragForce5 
            
        else: fdrag = vector(0,0,0)
        return fdrag


    elif (sign == 'e'):
   
        if ((t > (3*dt)) and (test.pos.x > 32) and (test.pos.x < 116) and (test.pos.y > -3)):
            fdrag = NegDragForce1 * norm(Force())
        elif ((test.pos.x > 116) and (test.pos.y < -10) and (test.pos.y > -110)):
            fdrag.y = -NegDragForce2 
        elif ((test.pos.x < 105) and (test.pos.x > -105) and (test.pos.y < -116)):
            fdrag.x = -NegDragForce3 
        elif ((test.pos.x < -116) and (test.pos.y < 10) and (test.pos.y > -110)):
            fdrag.y = NegDragForce4 
        elif ((test.pos.x < -30) and (test.pos.x > -116) and (test.pos.y > -3)):
            fdrag.x = -NegDragForce5 
         
        else: fdrag = vector(0,0,0)
        return fdrag


def push():
    if (sign == 'p'): 
        if ((test.pos.x < -118.5) and (test.pos.y > -13)):
            test.momentum.y = -mag(test.momentum)
            test.momentum.x = 0         
        if ((test.pos.x < -115) and (test.pos.y < -118.5)):
            test.momentum.x = mag(test.momentum)
            test.momentum.y=0
        if ((test.pos.x > 119) and (test.pos.y < -105)):
            test.momentum.y = mag(test.momentum)
            test.momentum.x = 0
        if ((test.pos.y > 0) and (test.pos.x > 112)):
            test.momentum.x = -mag(test.momentum)
            test.momentum.y = 0
            
    elif (sign == 'e'):
        if ((test.pos.x > 118.5) and (test.pos.y > -13)):
            test.momentum.y = -mag(test.momentum)
            test.momentum.x = 0
        if ((test.pos.x > 115) and (test.pos.y < -118.5)):
            test.momentum.x = -mag(test.momentum)
            test.momentum.y=0
        if ((test.pos.x < -118.5) and (test.pos.y < -10)):
            test.momentum.y = mag(test.momentum)
            test.momentum.x = 0
        if ((test.pos.y > 0) and (test.pos.x < -112)):
            test.momentum.x = mag(test.momentum)
            test.momentum.y = 0
            

oscillation = gdisplay(xtitle='Time', ytitle='Velocity of Charge')
funct1 = gcurve(color=(.2, .63, .79))

# Main while loop
while t < 3.2e-8:
    rate(1e8)
    Fdrag = drag()
    test.momentum = test.momentum + (Force()  - Fdrag) * dt
    push()
    
    test.velocity = test.momentum / test.mass
    vel = test.velocity
    test.pos = test.pos + test.velocity
    checkWalls()
   
    if (sign == 'p'): funct1.color = (1,0,0)
    funct1.plot( pos=(t, mag(test.velocity)))
        
    t = t + dt
    if ((test.pos.x < 30) and (test.pos.x > -30) and (test.pos.y > -3)): break




