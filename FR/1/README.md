# CIPP_microbit-GPS

## Partie 1 : Utiliser le GPS pour sauvegarder un emplacement

Nous voulons stocker une position GPS que nous aimons. Parfait! Il s'avère que nous pouvons le faire avec les composantes dont nous disposons !

Le code que nous allons utiliser aujourd'hui fonctionne assez facilement :

> Appuyez sur A pour commencer à capturer votre emplacement actuel.
> Attendre quelques secondes pour s'assurer que nous avons plusieurs lectures valides.
> Appuyez à nouveau sur A pour arrêter la capture.

C'est tout ce que nous avons besoin de faire ! Les emplacements GPS seront sauvegardés sur le micro:bit dans des fichiers appelés gps01.csv, gps02.csv, etc. et qui ressemblent à ceci :
![Localisations GPS stockées dans un fichier csv](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/GPSCapture_small.png)
Les coordonnées sont stockées au format Degrés-Minutes. Pour les utiliser à l'étape suivante ou dans Google Earth, par exemple, nous devrons les convertir en degré décimal, ce qui peut être fait facilement sur [ce site Web](https://coordinates-converter.com/en/).

**Allons-y!**

### Le code

1. Comme le code est assez complexe, il est fourni dans son intégralité. Téléchargez-le sur votre ordinateur en cliquant avec le bouton droit n'importe où sur la page et en sélectionnant Enregistrer sous...

[Télécharger le code ici.](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/7761d36211a08e31bb17217241e255173bdf71ff/code/GPStoCSV.py)
<br><br>

![](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/saveFileonGit.gif)

2. Ouvrez l'éditeur Mu. Assurez-vous que vous êtes en mode "BBC micro:bit".
<br>

![](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/MuE_Mode_v2.gif)

3. Chargez le fichier GPStoCSV.py que vous venez de télécharger à l'étape 1.

4. Ce code est assez direct. Tout d'abord, il établit une connexion avec le module GPS. Ensuite, vous utilisez le bouton A pour basculer entre le "mode veille", où rien ne se passe vraiment, et le "mode enregistrement", où votre position actuelle est écrite toutes les quelques secondes dans un fichier sur le micro:bit. En appuyant sur le bouton B, vous pouvez avoir un rappel du mode dans lequel vous vous trouvez : une cible en mode capture, un sourire en mode attente. C'est tout ce dont vous avez besoin pour stocker les positions GPS !

<br>

### Les composantes

Une fois le code fait, nous devons assembler les composantes. Les différentes composantes - boitier pour les piles, module GPS, micro:bit - devraient s'adapter assez bien au canoë que vous avez imprimé. On peut voir sur cette image tirée de la fiche technique quels câbles sont lesquels. *Attention !* Les couleurs des câbles ne sont pas toujours les mêmes, seul l'ordre compte.
![Image de commande de câbles GPS](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/GPS_Connectors.png)


Voici les connexions à faire :

1. GND (G sur la carte) à GND sur le m:bit
2. RX (R sur la carte) à 1 sur m:bit
3. TX (T sur la carte) à 2 sur m:bit
4. VCC (V sur la carte) à 3V sur m:bit

Si vous alimentez maintenant le micro:bit, vous devriez également voir le voyant rouge s'allumer sur le module GPS ! Le module GPS doit se verrouiller sur les satellites pour fonctionner correctement, il ne fonctionnera donc pas à l'intérieur. Une fois que vous êtes à l'extérieur et qu'il a acquis le signal d'au moins 2 satellites, il s'allume en vert, ce qui signifie qu'il peut maintenant fonctionner correctement ! Appuyez sur le bouton A et attendez quelques secondes pour enregistrer un emplacement, puis appuyez à nouveau pour arrêter l'enregistrement. C'est tout! Retournez à l'intérieur pour récupérer les données.


### Récupérer les coordonnées

1. Dans l'éditeur Mu, cliquer sur l'icône *Fichier* en haut.
2. Dans les fenêtres qui apparaissent au bas, glisser les fichiers du micro:bit vers l'ordinateur.
3. Le dossier où se trouve les fichiers sur l'ordinateur se nomme "mu_code", qui se trouve dans le dossier principal de votre compte utilisateur de l'ordinateur.

![Image de commande de câbles GPS](https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/Mu_File_transfer.png)

*RAPPEL : Les coordonnées GPS sont stockées dans nos fichiers .csv au format Degrés-Minutes. Pour les utiliser à l'étape suivante ou dans Google Earth, par exemple, nous devrons les convertir en degré décimal, ce qui peut être fait facilement sur [ce site Web](https://coordinates-converter.com/en/).*

<br> 

Lorsque c'est fait, passez à l'étape suivante de l'activité [ici](https://github.com/GenieLabMtl/CIPP_microbit-GPS/tree/main/FR/2).