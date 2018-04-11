import spidev
import time
#import spi.max_speed_hz = 50000000

spi = spidev.SpiDev()
spi.open(0,0)
counter = 0

while True:
    try:
        print "writing data"
        #hello spi (ASCII)
        data = [104, 101, 108, 111, 32]
        #resp = spi.xfer2(data)
        print ">>>" + str(spi.xfer2(data))

        time.sleep(1)
        counter += 1
        if counter > 4:
            break
        time.sleep(1)
    except(keyboardInterrupt, SystemExit):
        spi.close()
        raise
spi.close()
print "done"

