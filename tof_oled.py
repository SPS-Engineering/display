import time
import board
import adafruit_vl53l1x
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()

i2c = board.I2C()

vl53 = adafruit_vl53l1x.VL53L1X(i2c)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# OLED screen from this tutorial
# https://learn.adafruit.com/adafruit-128x64-oled-featherwing/circuitpython

WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle in black
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw some label text
text1 = "Your height is:"
text_area = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=20, y=13)
splash.append(text_area)
text2 = "179cm"
text_area2 = label.Label(
    terminalio.FONT, text=text2, scale=3, color=0xFFFFFF, x=10, y=38
)
splash.append(text_area2)

# Time of Flight from this tutorial 
# https://learn.adafruit.com/adafruit-vl53l1x?view=all#python-circuitpython

# OPTIONAL: can set non-default values
vl53.distance_mode = 1
vl53.timing_budget = 100

print("VL53L1X Simple Test.")
print("--------------------")
model_id, module_type, mask_rev = vl53.model_info
print("Model ID: 0x{:0X}".format(model_id))
print("Module Type: 0x{:0X}".format(module_type))
print("Mask Revision: 0x{:0X}".format(mask_rev))
print("Distance Mode: ", end="")
if vl53.distance_mode == 1:
    print("SHORT")
elif vl53.distance_mode == 2:
    print("LONG")
else:
    print("UNKNOWN")
print("Timing Budget: {}".format(vl53.timing_budget))
print("--------------------")

vl53.start_ranging()

while True:
    pass  #this makes the screen work
    if vl53.data_ready:
        print("Distance: {} cm".format(vl53.distance))  #this works fine in serial
        vl53.clear_interrupt()
        time.sleep(1.0)
