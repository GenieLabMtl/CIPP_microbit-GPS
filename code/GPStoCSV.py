from microbit import *

def initGPS():
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin1, rx=pin2)
    sleep(500)
    INIT_SEQUENCE_RMC = [
    b"\xB5\x62\x06\x08\x06\x00\xE8\x03\x01\x00\x01\x00\x01\x39",                 # Frequence 1s
    #b"\xB5\x62\x06\x08\x06\x00\x20\x4E\x01\x00\x01\x00\x84\x00\xB5\x62\x06\x08\x00\x00\x0E\x30",                 # Frequence 20s
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

def saveFile():
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
    listeNMEA.clear()

# Convertir les coodonnées GPS de Degré Minutes à Degré Décimal
def converterDM_DD(coordToConvert) :
    return (((toConvert-toConvert%100)/100) + (toConvert%100)/60)

# Debut du programme

initGPS()

# Variables globales
msg=""
listeNMEA=[]
captureMode=False
display.show(Image.HAPPY)
noFile=0

while True:
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
            #incoming = uart.readline().decode().format("%s")
            incoming = str(uart.readline(), 'ascii')
            sp=incoming.split("$")
            msg += sp[0]
            if len(sp) > 1 :
                listeNMEA.append(sp)
                for m in sp[1:]:
                    splitlist = msg.split(",")
                    if splitlist[0] == "GPRMC":
                        listeNMEA.append(splitlist)
                        msg="$"+m


                #if len(splitlist) > 7 :
                #    # print("m {}, splitlist {}".format(sp[1], splitlist))
                #    if splitlist[0] == "GPRMC":
                #        coords = [converterDM_DD(float(splitlist[3])),converterDM_DD(float(splitlist[5]))]
                #        if splitlist[4] == "S" :
                #            coords[0] = -coords[0]
                #        if splitlist[6] == "W" :
                #            coords[1] = -coords[1]
                #        listeNMEA.append(sp)
                #        listeNMEA.append(coords)

        if len(listeNMEA)>20:
            saveFile()
