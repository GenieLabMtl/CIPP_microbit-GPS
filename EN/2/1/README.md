<h1 align="center"> Part 2 : Find your way to a GPS location </h1>

We will now see how we can get the micro:bit to point an arrow towards the GPS location we want to reach, effectively working as a compass pointing to that location instead of the magnetic North.

<br>

By integrating text-to-speech elements, we can also turn this program in a (very) basic AI assistant!  When the destination is reached, we will hear a vocal message saying so.

<br>

Alright, let's do this!

<br>

1. Download the code [here](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/7761d36211a08e31bb17217241e255173bdf71ff/code/CompassWithGPSData.py) and save it as we have done previously.

2. Open it in the MU editor.

3. Let's set the variables and constants needed for this program to run.
> - don't forget to change the GPS location next to DESTINATION in the code to the one of your choice.
> - you can change the text-to-speech messages next to SM_START and SM_END.

Here is the relevant part of the code:

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
SM_START = "Let's go!"
SM_END = "This is the spot"
```

4. Install the code on the micro:bit, and go outside!

If you want to go further, go to the next part! [here](https://github.com/GenieLabMtl/CIPP_microbit-GPS/tree/main/EN/2/2)