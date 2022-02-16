# CIPP_microbit-GPS

## Part 1 : Get GPS to store location on device

We want to store a GPS location that we like. Perfect! Turns out we can do that with the components we have to our disposal!

The code we will use today works pretty easily:

> Press A to start capturing your current location.
> Press A again to stop capturing.

That's all we need! The GPS locations will be stored on the micro:bit on files called gps01.csv, gps02.csv, etc. and will look something like this:
![GPS locations stored on csv file](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/GPSCapture_small.png)
The coordinates are stored in the Degrees Minutes format. To use them in the next step or in Google Earth, for example, we will need to convert them to Decimal degree, which can be done conveniently on [this website](https://coordinates-converter.com/en/).

**Let's do this!**

### The code

1. As the code is quite complexe, it is provided in it's entirety [here](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/7761d36211a08e31bb17217241e255173bdf71ff/code/GPStoCSV.py). Download it to your computer by right-clicking anywhere on the page and Save as...
<br>

![](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/saveFileonGit.gif)

2. Open Mu Editor. Make sure you are in the "BBC micro:bit" mode.
<br>

![](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/MuE_Mode_v2.gif)

3. Load the GPStoCSV.py file you just downloaded is step 1.

4. This code is pretty straight forward.  First, it establishes a connection with the GPS module.  Then, you use the A button to switch between "standby mode", where nothing is really happening, and "record mode", where your current location is being written every few seconds to a file on the micro:bit.  By pressing the B button, you can have a reminder of which mode you are in.  That's all you need to store GPS locations!

<br>

### The components

Once the code is done, we need to assemble the components. The various components - battery holder, GPS module, micro:bit - should fit pretty well in the canoe you've printed.  We can see on this image taken from the datasheet which cables are which.  *Be careful!* The colours of the cables are not always the same, so only the order matters.
![GPS cables order image](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/GPS_Connectors.png)


Here are the connections that need to be made:

1. GND (G on the board) to GND on the m:bit
2. RX (R on the board) to 1 on m:bit
3. TX (T on the board) to 2 on m:bit
4. VCC (V on the board) to 3V on m:bit

If you now power the micro:bit, you should also see the red light come up on the GPS module!  The GPS module needs to lock on satelites to work properly, so it will not work indoors.  Once you are outside and it has acquired the signal of at least 2 satelites, it will turn on a green light, meaning it can now work properly! Press on that A button and wait a few seconds to record a location, then press it again to stop recording.  That's it!  Go back indoors to retrieve the data and proceed with the next step of the activity [here](https://github.com/GenieLabMtl/CIPP_microbit-GPS/tree/main/2).



<br>
