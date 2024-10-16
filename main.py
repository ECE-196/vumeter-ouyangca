import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36, # type: ignore
    board.IO37,
    board.IO38,
    board.IO39
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
history_level = 0

while True:
    volume = microphone.value

    print(volume)
    if volume >= 24000:
        level = int((volume-24000)/1000)
        print(level)
    else:
        level = 0 

    if level < history_level:
        level = history_level - 1

    for i in range(11):
        if i <= level:
            leds[i].value = True
        else:
            leds[i].value = False

    history_level = level
    sleep(1)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
