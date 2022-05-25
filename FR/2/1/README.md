<h1 align="center"> Partie 2 : Trouvez votre chemin vers une position GPS </h1>

Nous allons maintenant voir comment nous pouvons faire en sorte que le micro:bit pointe une flèche vers l'emplacement GPS que nous voulons atteindre, fonctionnant comme une boussole pointant vers cet emplacement plutôt que le Nord magnétique.

<br>

En intégrant des éléments de synthèse vocale, nous pouvons également transformer ce programme en un assistant IA (très) basique ! Lorsque la destination est atteinte, nous entendrons un message vocal nous en informant.

<br>

Et c'est parti !

<br>

1. Téléchargez le code [ici](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/7761d36211a08e31bb17217241e255173bdf71ff/code/CompassWithGPSData.py) et enregistrez-le comme nous l'avons fait précédemment.

2. Ouvrez-le dans l'éditeur MU

3. Définissons les variables et les constantes nécessaires à l'exécution de ce programme.
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

Si vous voulez allez plus loin, rendez-vous dans la partie suivante! [ici](https://github.com/GenieLabMtl/CIPP_microbit-GPS/tree/main/FR/2/2)