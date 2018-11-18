# UV sensing using library
import bh1750
import machine

i2c = machine.I2C(scl = machine.Pin(5), sda = machine.Pin(4))

'''
confirm your device is present on the bus
it should return [35] for this particular sensor
if this returns nothing, check your wiring
then check the Pin GPIO numbers are correct 
'''

print(i2c.scan())

s = bh1750.BH1750(i2c)

while True:
    s.luminance(BH1750.ONCE_HIRES_1)

'''
there are lots of options to sense luminance
read bh1750.py for details
this is a high resolution single reading
it returns a float of luminance in LUX
'''