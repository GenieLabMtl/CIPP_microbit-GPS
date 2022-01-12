# CIPP_microbit-GPS


## Prep

mu-editor:  [download](https://codewith.mu/en/download)
micro-bit
gps module
wire stripper
soldering iron
heatshrink tube
hot air gun





## Part 1
### Get GPS to store location

start mu editor and get code on the micro:bit

this code will be in python as we need to use advanced features not found in the editor we usually use, which is [makecode](https://makecode.microbit.org/).

Python is a very common programming language that is pretty easy to learn.  However, the goal of this activity is to get the GPS going, so we will use a "copy-paste" approach to code the micro:bit.  You could simply load the files on the device without looking at any of it, but by copy-pasting you can at least get a sense of if this might interest you for other projects.  
To learn more about the python programming language, [w3schools](https://www.w3schools.com/python/default.asp) is a great place to start.

1. Create new file and save it as "GPStoCSV.py"
2. 
> we start by importing the library to run the micro:bit:

`from microbit import *`

3. 
> this function will activate the communication between the GPS and the micro:bit

`def initGPS():
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin1, rx=pin2)
    sleep(500)
    INIT_SEQUENCE_RMC = [
    b"\xB5\x62\x06\x08\x06\x00\x20\x4E\x01\x00\x01\x00\x84\x00\xB5\x62\x06\x08\x00\x00\x0E\x30",                 # Frequence
    b"\x24\x45\x49\x47\x50\x51\x2c\x44\x54\x4d\x2a\x33\x42\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x0a\x00\x04\x23", # Disable GPDTM
    b"\x24\x45\x49\x47\x50\x51\x2c\x47\x42\x53\x2a\x33\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x09\x00\x03\x21", # Disable GPGBS
    b"\x24\x45\x49\x47\x50\x51\x2c\x47\x47\x41\x2a\x32\x37\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x00\x00\xfa\x0f", # Disable GPGGA
    b"\x24\x45\x49\x47\x50\x51\x2c\x47\x52\x53\x2a\x32\x30\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x06\x00\x00\x1b", # Disable GPGRS
    b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x41\x2a\x33\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x02\x00\xfc\x13", # Disable GPGSA
    b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x54\x2a\x32\x36\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x07\x00\x01\x1d", # Disable GPGST
    b"\x24\x45\x49\x47\x50\x51\x2c\x47\x53\x56\x2a\x32\x34\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x03\x00\xfd\x15", # Disable GPGSV
    b"\x24\x45\x49\x47\x50\x51\x2c\x47\x4c\x4c\x2a\x32\x31\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x01\x00\xfb\x11", # Disable GPGLL
    b"\x24\x45\x49\x47\x50\x51\x2c\x56\x54\x47\x2a\x32\x33\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x05\x00\xff\x19", # Disable GPVTG
    b"\x24\x45\x49\x47\x50\x51\x2c\x5a\x44\x41\x2a\x33\x39\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x08\x00\x02\x1f", # Disable GPZDA
    b"\x24\x45\x49\x47\x50\x51\x2c\x52\x4d\x43\x2a\x33\x41\x0d\x0a\xb5\x62\x06\x01\x03\x00\xf0\x04\x01\xff\x18"  # Enable  GPRMC
    ]
    for i in INIT_SEQUENCE_RMC:
        uart.write(i)
        sleep(100)
    uart.init(115200) # on redonne la main pour la communication USB
`

4. 
> this function will save the GPS location to a file on the micro:bit

`def saveFile():
    global noFile
    noFile += 1
    with open("gps{:02d}.csv".format(noFile),'wt') as myCSV :
        for m in listeNMEA:
            if m != "" and m[0] == '$':
                if m[-1] == "\n":
                    myCSV.write(m)
                else:
                    myCSV.write(m+"\n")
        myCSV.close()
    listeNMEA.clear()`

5. 
> we initiate the GPS module and assign variables to run the program

`# Debut du programme

initGPS()

# Variables globales
msg=""
listeNMEA=[]
captureMode=False
display.show(Image.HAPPY)
noFile=0`

6. 
> this will loop forever as long as the micro:bit is powered

`while True:
    if button_a.was_pressed():
        # Bouton a : change le mode capture
        captureMode = not captureMode
        if captureMode:
            uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin1, rx=pin2)
            display.show(Image.TARGET)
            msg=""
        else:
            saveFile()
            uart.init(115200)
            display.show(Image.HAPPY)

    if button_b.was_pressed():
        # Affiche l'etat
        display.show(len(listeNMEA))
        sleep(1000)
        display.show(Image.TRIANGLE)
        sleep(500)
        display.show(noFile)
        sleep(1000)
        if captureMode:
            display.show(Image.TARGET)
        else:
            display.show(Image.HAPPY)

    if captureMode :
        if uart.any():
            incoming = uart.readline().format("%s")
            sp=incoming.split("$")
            msg += sp[0]
            if len(sp)>1:
                for m in sp[1:]:
                    listeNMEA.append(msg)
                    msg="$"+m
        if len(listeNMEA)>20:
            saveFile()
`


## Part 2