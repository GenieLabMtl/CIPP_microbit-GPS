# CIPP_microbit-GPS


## Preparation steps
You will need the following to do the activity:

- Mu Editor: to edit and upload the code to the device. [Download here](https://codewith.mu/en/download)
- micro-bit
- gps module
- wire stripper
- soldering iron
- heatshrink tube
- hot air gun



## Part 1 : Get GPS to store location on device

*Start Mu Editor and get code on the micro:bit*

this code will be in python as we need to use advanced features not found in the editor we usually use, which is [makecode](https://makecode.microbit.org/).  This is a great ressource to learn the basics of programming as you start with a simplified visual coding language, and you can switch to JavaScript or Python at anytime to see how the code looks in these popular languages.

Python is a very common programming language that is pretty easy to learn.  However, the goal of this activity is to get the GPS going, so we will use a "copy-paste" approach to code the micro:bit.  You could simply load the files on the device without looking at any of it, but by copy-pasting you can at least get a sense of if this might interest you for other projects.  
To learn more about the python programming language, [w3schools](https://www.w3schools.com/python/default.asp) is a great place to start.

Press A to start capturing your current location.
Press A again to stop capturing.

The GPS locations will be stored on the micro:bit on files called gps01.csv, gps02.csv, etc.

1. As the code is quite complexe, it is provided in it's entirety [here](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/7761d36211a08e31bb17217241e255173bdf71ff/code/GPStoCSV.py). Download it to your computer by right-clicking anywhere on the page and Save as...

2. Open Mu Editor. Make sure you are in the "BBC micro:bit" mode.

![](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/Gifs/MuE_Mode_v2.gif)

3. Load the GPStoCSV.py file you just downloaded is step 1.

4. This code is pretty straight forward.  First, it establishes a connection with the GPS module.  Then, you use the A button to switch between "standby mode", where nothing is really happening, and "record mode", where your current location is being written every few seconds to a file on the micro:bit.  By pressing the B button, you can have a reminder of which mode you are in.  That's all you need to store GPS locations!

<br>
Now let's see how we can retrieve those locations, and find them again.


<br>

## Part 2
### Find your way to a GPS location

We will now see how we can get the micro:bit to point an arrow towards the GPS location we want to reach, effectively working as a compass pointing to that location instead of the magnetic North.

<br>

By integrating text-to-speech elements, we can also turn this program in a (very) basic AI assistant!  When the destination is reached, we will hear a vocal message saying so.

<br>

Alright, let's do this!

<br>

1. Download the code [here](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/7761d36211a08e31bb17217241e255173bdf71ff/code/CompassWithGPSData.py) and save it as we have done previously.

2. let's set the variables and constants needed for this program to run.
> - don't forget to change the GPS location next to DESTINATION to the one of your choice.
> - you can change the text-to-speech messages next to SM_Start and SM_End.
```py
#Variables and constants

# our current position, updated continuously by the GPS module
currentLocation = [45.530200884174725, -73.55110194184894]

# this is where we want to go
DESTINATION = (45.53465356340576, -73.56085768454646)

# How close we need to be to the destination to trigger our "We're here" message
DIST_THRESH = 0.0001

# to assemble the incoming data from the GPS module
msg = ""

# to store the message
listeNMEA = []

# True to enable GPS position detection
captureMode = True

# Speech messages
SM_Start = "Let's go!"
SM_END = "This is the spot"
```

3. initiate the internal compass

```py
# Functions

def initCompass():
    compass.calibrate()
```

4. some maths to have the compass point to the GPS location

```py
def angleFromCoordinate(lat1, long1, lat2, long2):
    # calculate the angle between our current position and the target location
    # this will return the bearing relative to the North
    dLon = long2 - long1

    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(
        dLon
    )

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng  # count degrees clockwise - remove to make counter-clockwise

    # bring between -180 and 180, 0 being North
    if brng > 180:
        brng = -(360 - heading)

    return brng
```

5. return the current direction the micro:bit is pointing relative to our target destination

```py
def currentHeading():
    # get the heading towards which the micro:bit is pointing
    heading = compass.heading()
    if heading > 180:
        heading = -(360 - heading)
    return heading
```
6. display the arrow on the screen
```py
def displayDirection():
    # once we have our current position, display an arrow pointing to the target GPS location
    direction = angleFromCoordinate(
        currentLocation[0], currentLocation[1], DESTINATION[0], DESTINATION[1]
    )

    azimut = currentHeading() - direction
    # make sure it works with range -180 to 180
    if azimut < -180:
        azimut += 360

    # E and W must be inverted
    if -22.5 <= azimut < 22.5:
        display.show(Image.ARROW_N)
    elif 22.5 <= azimut < 67.5:
        display.show(Image.ARROW_NW)
    elif 67.5 <= azimut < 112.5:
        display.show(Image.ARROW_W)
    elif 112.5 <= azimut < 157.5:
        display.show(Image.ARROW_SW)
    elif 157.5 <= azimut <= 180 or -180 <= azimut < -157.5:
        display.show(Image.ARROW_S)
    elif -157.5 <= azimut < -112.5:
        display.show(Image.ARROW_SE)
    elif -112.5 <= azimut < -67.5:
        display.show(Image.ARROW_E)
    elif -67.5 <= azimut < -22.5:
        display.show(Image.ARROW_NE)
    else:
        # is all is working properly, this should never display
        display.show(Image.CONFUSED)
```

7. initiate the GPS module, same as we've done in the previous program
```py
def initGPS():
    # establish communication with the GPS module and send init messages to receive only GPRMC data
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin1, rx=pin2)
    sleep(500)
    INIT_SEQUENCE_RMC = [
        b"\xB5\x62\x06\x08\x06\x00\x20\x4E\x01\x00\x01\x00\x84\x00\xB5\x62\x06\x08\x00\x00\x0E\x30",  # Frequence
        b"\x24\x45\x49\x47\x50\x51\x2c\x44\x54\x4d\x2a\x33\x42\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x0a\x00\x04\x23",  # Disable GPDTM
        b"\x24\x45\x49\x47\x50\x51\x2c\x47\x42\x53\x2a\x33\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x09\x00\x03\x21",  # Disable GPGBS
        b"\x24\x45\x49\x47\x50\x51\x2c\x47\x47\x41\x2a\x32\x37\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x00\x00\xfa\x0f",  # Disable GPGGA
        b"\x24\x45\x49\x47\x50\x51\x2c\x47\x52\x53\x2a\x32\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x06\x00\x00\x1b",  # Disable GPGRS
        b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x41\x2a\x33\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x02\x00\xfc\x13",  # Disable GPGSA
        b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x54\x2a\x32\x36\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x07\x00\x01\x1d",  # Disable GPGST
        b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x56\x2a\x32\x34\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x03\x00\xfd\x15",  # Disable GPGSV
        b"\x24\x45\x49\x47\x50\x51\x2c\x47\x4c\x4c\x2a\x32\x31\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x01\x00\xfb\x11",  # Disable GPGLL
        b"\x24\x45\x49\x47\x50\x51\x2c\x56\x54\x47\x2a\x32\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x05\x00\xff\x19",  # Disable GPVTG
        b"\x24\x45\x49\x47\x50\x51\x2c\x5a\x44\x41\x2a\x33\x39\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x08\x00\x02\x1f",  # Disable GPZDA
        b"\x24\x45\x49\x47\x50\x51\x2c\x52\x4d\x43\x2a\x33\x41\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x04\x01\xff\x18",  # Enable  GPRMC
    ]
    for i in INIT_SEQUENCE_RMC:
        uart.write(i)
        sleep(100)
```

8. function to fetch current GPS location
```py
def getCurrentLocation():
    # parse the incoming message from the GPS module
    if listeNMEA[0][17] == "A":
        currentLocation[0] = float(listeNMEA[0][19:28])
        if listeNMEA[0][30] == "S":
            currentLocation[0] = -currentLocation[0]
        currentLocation[1] = float(listeNMEA[0][32:42])
        if listeNMEA[0][44] == "W":
            currentLocation[1] = -currentLocation[1]
    else:
        display.show(Image.NO)
    listeNMEA.clear()
```

9. check if we have arrived, and make a sound when the destination is reached.
```py
def soundWhenClose(message):
    # check if close to destination, taking into account E/W N/S coordinate values
    # returns True if within threshold distance of the destination
    if (abs(currentLocation[0]) - abs(DESTINATION[0])) < DIST_THRESH and
        (abs(currentLocation[1]) - abs(DESTINATION[1])) < DIST_THRESH and
        (((currentLocation[0]== DESTINATION[0]) & (currentLocation[0]==0)) | (currentLocation[0] * DESTINATION[0] > 0)) and
        (((currentLocation[1]== DESTINATION[1]) & (currentLocation[1]==0)) | (currentLocation[1] * DESTINATION[1] > 0)) :

        # if we are close enough to the spot, a message will be heard, emitted from the micro:bit's speaker
        speech.say(message, pitch=120, speed=120, mouth=150, throat=170)
        display.show(Image.TARGET)

        sleep(5000)

        return True
    else:
        return False
```

10. run the program
```py
# Start program here
initCompass()
initGPS()

speech.say(SM_Start, pitch=120, speed=120, mouth=150, throat=170)

while True:

    # first get location from GPS
    if captureMode :
        if uart.any():
            incoming = uart.readline().format("%s")
            sp=incoming.split("$")
            msg += sp[0]
            if len(sp)>1:
                for m in sp[1:]:
                    listeNMEA.append(msg)
                    msg="$"+m
            getCurrentLocation()

    # then see if we are where we want to go to
    if soundWhenClose(SM_END):
        continue

    # and finally display the direction of the objective if we are not there yet
    displayDirection()
```

