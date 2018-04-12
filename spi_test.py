import spidev
import time

usleep = lambda x : time.sleep(x/1000000.0)

spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 2000000

while True:
    resp = spi.xfer2([0x00])    
    print(resp[0])
    usleep(1.0)

spi.close()
