<h1 align="center">Trouvez votre chemin vers une position GPS </h1>

Nous allons maintenant voir comment nous pouvons faire en sorte que le micro:bit pointe une flèche vers l'emplacement GPS que nous voulons atteindre, fonctionnant comme une boussole pointant vers cet emplacement plutôt que le Nord magnétique.

<br>

En intégrant des éléments de synthèse vocale, nous pouvons également transformer ce programme en un assistant IA (très) basique ! Lorsque la destination est atteinte, nous entendrons un message vocal nous en informant.

<br>

Et c'est parti !

<br>

1. Téléchargez le code [ici](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/7761d36211a08e31bb17217241e255173bdf71ff/code/CompassWithGPSData.py) et enregistrez-le comme nous l'avons fait précédemment.

2. Ouvrez-le dans l'éditeur MU

3. Définissons les variables et les constantes nécessaires à l'exécution de ce programme.
<br>
> - N'oubliez pas de changer la position GPS à côté de DESTINATION dans le code par celle de votre choix.
> - Vous pouvez modifier les messages de synthèse vocale à côté de SM_START et SM_END.

*En programmation, les constantes - des valeurs qui ne changent pas durant le programme - sont habituellement nommées avec un nom écrit en MAJUSCULES.*

Voici la section du code en question :

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

4. Installer le code sur le micro:bit, et aller dehors!

***Tout ce qui suit est simplement là pour indiquer ce que fait le code. Rien n'a besoin d'être modifier pour que ça fonctionne.***

5. Initialise le compas interne

```py
# Functions

def initCompass():
    compass.calibrate()
```

6. Des formules mathématiques pour que le compas pointe vers la position GPS

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

7. Retourne la direction dans laquelle le micro:bit fait face, relativement à notre destination cible

```py
def currentHeading():
    # get the heading towards which the micro:bit is pointing
    heading = compass.heading()
    if heading > 180:
        heading = -(360 - heading)
    return heading
```

8. Affiche la flèche à l'écran

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

9. Lance le programme du module GPS, comme dans l'activité précédente

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

10. Récupére la position GPS actuelle

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

11. Vérifie si nous sommes arrivés, et fait un son lorsque la destination est atteinte.

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

12. Lance le programme
```py
# Start program here
initCompass()
initGPS()

speech.say(SM_START, pitch=120, speed=120, mouth=150, throat=170)

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

