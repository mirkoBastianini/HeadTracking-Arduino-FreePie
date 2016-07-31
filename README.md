#HeadTracking with Arduino and FreePie
This is a cheap headtracking with Arduino and MPU-6050, for a more immersive experience with games that support TrackIR or FreeTrack.

First of all, we must buy an Arduino Nano (every model of Arduino it's ok, but Nano is the smallest of the family) and a MPU-6050 sensor.

#Connection

The picture below shows the connection between Arduino and the sensor. 

![alt tag](https://github.com/mirkoBastianini/HeadTracking-Arduino-FreePie/blob/master/img/connection.jpg)

If you want, you can reduce the number of cables to one (only GND cable), if you use a strip as I did.

![alt tag](https://github.com/mirkoBastianini/HeadTracking-Arduino-FreePie/blob/master/img/myconnection.jpg)

#Arduino code

After install Arduino IDE, if you connect your Arduino with sensor and you load the script YawPithRoll.ino (download it from the folder <i>Arduino script</i> of this repo), you should see values getting out from serial port.

#FreePie code

FreePIE is a application for bridging and emulating input devices. Install it from this link:

!http://andersmalmgren.github.io/FreePIE/

Now download the script inside <i>FreePie Script</i> folder of this repo and load it into the program. You must choose if you want emulate <b>TrackIR</b> or <b>Freetrack</b>, by playing with the respective variabile in the script. By default, TrackIR is setting to True, and FreeTrack is setting to False.

In my case, Assetto Corsa supports TrackIR. You can also change the multiplier for a better sensitivity in game.

After doing this, press F5 and you should see value on the Watch console of FreePie.

Here is a list of games supported by TrackIR:
!https://www.naturalpoint.com/trackir/games/

and a list of games supported by FreeTrack:
!https://en.wikipedia.org/wiki/List_of_games_compatible_with_FreeTrack

#Calbration

Calibration of this device is very important: I suggest you to open the FreePie script, put the device in "point zero" (the position when you are in front of monitor), and start the console. 
You will see <i>Yaw, Pitch and Roll</i> values and <i>TrackIR.yaw, TrackIR.pitch and TrackIR.Roll</i> values. Your goal is to add a constant in the script that will become zero the values of <i>TrackIR.yaw, TrackIR.pitch and TrackIR.Roll</i>.

Enjoy!

