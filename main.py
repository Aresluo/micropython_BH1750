# UV sensing using library
import bh1750
import machine

scl = machine.Pin(5)
sda = machine.Pin(4)
i2c = machine.I2C(scl,sda)

s = bh1750.BH1750(i2c)

while True:
    s.luminance(BH1750.ONCE_HIRES_1)
