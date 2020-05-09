
import RPi.GPIO as GPIO
from time import sleep
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from PIL import ImageFont, ImageDraw

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

serial = i2c(port=1, address=0x3C)
# device = ssd1306(serial)
device = sh1106(serial, rotate=2)

x = 0
with canvas(device) as draw:
    font = ImageFont.truetype('./impact.ttf',30)
    font = ImageFont.truetype('./impact.ttf',30)
    draw.text((25, 0), "Tasbih", fill="white", font=font)
    draw.text((25, 30), "Digital", fill="white", font=font)

while True:
    if GPIO.input(8) == GPIO.HIGH:
        x += 1
        print(f"Sensor was touched {x} times")
        with canvas(device) as draw:
            font1 = ImageFont.truetype('./impact.ttf',18)
            font2 = ImageFont.truetype('./impact.ttf',45)
            draw.text((0, 10), "Tasbih", fill="white", font=font1)
            draw.text((0, 30), "Digital", fill="white", font=font1)
            draw.text((60, 5), str(x), fill="white", font=font2)
            sleep(.5)
