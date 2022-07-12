<h1 align="center"> Part 1.2 : The components </h1>

Once the code is done, we need to assemble the components. They are: 

1. battery holder with batteries
2. GPS module
3. micro:bit
4. breakout board for micro:bit

We can see on this image taken from the datasheet which cables are which on the GPS module.

*Be careful!* The colours of the cables are not always the same, so only the order matters.
<p align="center"><img align="center" width="500" src="https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/GPS_Connectors.png" alt="GPS cables order image"></p>



Here are the connections that need to be made:

1. GND (G on the board) to GND on the m:bit
2. RX (R on the board) to 1 on m:bit
3. TX (T on the board) to 2 on m:bit
4. VCC (V on the board) to 3V on m:bit

If you now power the micro:bit, you should also see the red light come up on the GPS module!  The GPS module needs to lock on satelites to work properly, so it will not work indoors.  Place all the components in the canoe and go outside. Once you are outside and it has acquired the signal of at least 2 satelites, a green light on the GPS will turn on, meaning it can now work properly! Press on the A button and wait a few seconds to record a location, then press it again to stop recording.  That's it!  Go back indoors to retrieve the data and proceed with the next step of the activity [here](https://github.com/GenieLabMtl/CIPP_microbit-GPS/tree/main/EN/2).

#### When you're done, proceed to the next step of the activity [here](https://github.com/GenieLabMtl/CIPP_microbit-GPS/tree/main/FR/1/3).
