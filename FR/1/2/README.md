<h1 align="center"> Partie 1.2 : Les composantes </h1>

Une fois le code fait, nous devons assembler les composantes. Les différentes composantes - boitier pour les piles, module GPS, micro:bit - devraient s'adapter assez bien au canoë que vous avez imprimé. On peut voir sur cette image tirée de la fiche technique quels câbles sont lesquels. *Attention !* Les couleurs des câbles ne sont pas toujours les mêmes, seul l'ordre compte.
<p align="center"><img align="center" width="500" src="https://raw.githubusercontent.com/GenieLabMtl/CIPP_microbit-GPS/main/static/images/GPS_Connectors.png" alt="Image de commande de câbles GPS"></p>


Voici les connexions à faire :

1. GND (G sur la carte) à GND sur le m:bit
2. RX (R sur la carte) à 1 sur m:bit
3. TX (T sur la carte) à 2 sur m:bit
4. VCC (V sur la carte) à 3V sur m:bit

Si vous alimentez maintenant le micro:bit, vous devriez également voir le voyant rouge s'allumer sur le module GPS ! Le module GPS doit se verrouiller sur les satellites pour fonctionner correctement, il ne fonctionnera donc pas à l'intérieur. Une fois que vous êtes à l'extérieur et qu'il a acquis le signal d'au moins 2 satellites, il s'allume en vert, ce qui signifie qu'il peut maintenant fonctionner correctement ! Appuyez sur le bouton A et attendez quelques secondes pour enregistrer un emplacement, puis appuyez à nouveau pour arrêter l'enregistrement. C'est tout! Retournez à l'intérieur pour récupérer les données.

Lorsque c'est fait, passez à l'étape suivante de l'activité [ici](https://github.com/GenieLabMtl/CIPP_microbit-GPS/tree/main/FR/1/3).