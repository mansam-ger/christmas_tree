import simpleio
import board
import time
import tones
# NOT USED ATM Colors are Random by now
#import colors
import neopixel
import songs
import random
import digitalio
###
NEOPIN = board.GP0
LEDS = 8
NP = neopixel.NeoPixel(NEOPIN, LEDS, brightness=0.8)
###
TOUCHPIN = digitalio.DigitalInOut(board.GP1)
TOUCHPIN.direction = digitalio.Direction.INPUT
TOUCHPIN.pull = digitalio.Pull.DOWN
#https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/buttons-and-switch
###
FLICKERLED = digitalio.DigitalInOut(board.GP4)
FLICKERLED.direction = digitalio.Direction.OUTPUT


BUZZER_PIN = board.GP3

COUNT = 1
def playsound(TONE, DURATION):
    simpleio.tone(BUZZER_PIN, TONE, duration=DURATION)
    
while True:
    if TOUCHPIN.value:
        print("touched")
        FLICKERLED.value = False        
        for each in random.choice(list(songs.songs.values())):
            RAND_LIGHT = random.randint(0,7)
            NP[RAND_LIGHT] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            print("LED NR", RAND_LIGHT, "turned on")
            NP.write()
            playsound(tones.TONES.get(each[0]), each[1])
            print(tones.TONES.get(each[0]))
            print(each[1])
            print("MELODYLINE", COUNT)
            COUNT= COUNT+1
            NP[RAND_LIGHT] = (0, 0, 0)
            time.sleep(0.01)
    
    else:
        
        FLICKERLED.value = True
        print("not pressed")
        time.sleep(0.5)

        