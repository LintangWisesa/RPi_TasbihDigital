from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106

serial = i2c(port=1, address=0x3C)
# device = ssd1306(serial)
device = sh1106(serial)

while True:
    with canvas(device) as draw:
    	draw.rectangle(device.bounding_box, outline="white", fill="black")
    	draw.text((30, 40), "Hello World", fill="white")
