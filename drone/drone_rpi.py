#!/usr/bin/python -u
# raspberry pi nrf24l01 hub
# more details at http://blog.riyas.org
# Credits to python port of nrf24l01, Joao Paulo Barrac & maniacbugs original c library

from nrf24 import NRF24
import time, sys
from time import gmtime, strftime
import picamera


pipes = [[0xf0, 0xf0, 0xf0, 0xf0, 0xe1], [0xf0, 0xf0, 0xf0, 0xf0, 0xd2]]

# ----- NRF24 Set up ---------- #
radio = NRF24()
radio.begin(0, 0,25,18) #set gpio 25 as CE pin
radio.setRetries(15,15)
radio.setPayloadSize(32)
radio.setChannel(0x4c)
radio.setDataRate(NRF24.BR_250KBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(1)
radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])

radio.startListening()
radio.stopListening()

radio.printDetails()
radio.startListening()

# Camera Setup
camera = picamera.PiCamera()

while True:
    pipe = [0]
    while not radio.available(pipe, True):
        time.sleep(1000/1000000.0)
    recv_buffer = []
    radio.read(recv_buffer)
    out = ''.join(chr(i) for i in recv_buffer)

    print out

    if out[ : 10] == "Sleep Mode":
        print out
    else:
        # Split string to lng lat alt
        lat_str,lng_str,alt_str, void = out.split(",")
        alt_str = alt_str
        lat = float(lat_str)
        lng = float(lng_str)
        alt_num = float(alt_str)
        
        
        print lat
        print lng
        print alt_str
        camera.capture('/var/www/html/image.jpg') # Image stored in website
        sys.stdout.flush()
        time.sleep(1)
