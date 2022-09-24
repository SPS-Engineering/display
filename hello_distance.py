import board
import displayio
import time

import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT, rotation=0)

root = display.root_group[-1]
CLEAR = "\033[2J"

display.root_group.scale = 2


while True:
    distance = 125

    print(CLEAR, end="")
    print("Hello")
    print(f"Distance: {distance:4d}cm")

    time.sleep(1)
