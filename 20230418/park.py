from signal import pause
from gpiozero import AngularServo, Button, LED
from time import sleep
servo = AngularServo(21, min_angle=0, max_angle=90)

upBtn = Button(23)
downBtn = Button(24)

Green= LED(17)
Red = LED(27)


def Up():
    Green.on()
    servo.angle = 90
    sleep(0.5)
    Green.off()

def Down():
    Red.on()
    servo.angle = 0
    sleep(0.5)
    Red.off()


upBtn.when_pressed = Up
downBtn.when_pressed=Down

pause()
