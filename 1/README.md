# CIPP_microbit-GPS


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
