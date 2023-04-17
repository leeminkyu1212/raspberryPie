from gpiozero import TonalBuzzer

from gpiozero.tones import Tone
from time import sleep

lst = [261.62,293.66,329.62,249.22,391.99,440.00,493.88,523.25]

b = TonalBuzzer(17)

while 1:
    for i in range(len(lst)):
        b.play(lst[i])
        sleep(0.2)

    b.stop()

    break
