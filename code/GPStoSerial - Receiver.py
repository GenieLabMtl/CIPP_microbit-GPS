from microbit import *
import radio

BUFFLEN = 128
radio.config(length=BUFFLEN)

radio.on()
while True:
    incoming = radio.receive()
    if incoming:
        print(incoming)
