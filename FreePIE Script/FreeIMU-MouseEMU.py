import ctypes
from ctypes import windll
DEBUG = True

def update():
   global yaw
   global roll
   global pitch
   global emulation
   yaw = freeImu.yaw
   roll = freeImu.roll
   pitch = freeImu.pitch

if starting:
   yaw = 0
   roll = 0
   pitch = 0
   rsltx = 0
   rslty = 0
   emulation = 0
   enabled = False
   freeImu.update += update

#show yaw pitch roll on freepie
diagnostics.watch(yaw)
diagnostics.watch(roll)
diagnostics.watch(pitch)
diagnostics.watch(emulation)

deltaYaw = filters.delta(yaw)
deltaPitch = filters.delta(pitch)
deltaRoll = filters.delta(roll)

#update mouse movement if enabled
if (enabled):
   emulation = 1
   rsltx += -deltaYaw*multiplier
   rslty += -deltaPitch*multiplier
   mouse.deltaX = -deltaYaw*multiplier
   mouse.deltaY = -deltaPitch*multiplier

#set key z,x,c
toggle1 = keyboard.getPressed(Key.Z)
toggle2 = keyboard.getPressed(Key.X)
toggle3 = keyboard.getPressed(Key.C)

#enable mouse movement based on sensors key=z
if toggle1:
   multiplier = 10 #change value to adjust sensitivity default=10
   enabled = not enabled
   emulation = 0
   
#reset position to relative center key=x
if toggle2:
   mouse.deltaX = 0-rsltx
   mouse.deltaY = 0-rslty
   rsltx = 0
   rslty = 0
      
#reset cursor position to absolute center of screen key=c
if toggle3:
   resox = windll.user32.GetSystemMetrics(0)
   resoy = windll.user32.GetSystemMetrics(1)
   ctypes.windll.user32.SetCursorPos(resox/2, resoy/2)
