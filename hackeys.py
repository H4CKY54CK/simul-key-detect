from _hackeys import *
import struct 
import sys


f = open("/dev/input/event12", "rb")
k = Keys()



try:
    while 1:
        data = f.read(24)
        values = struct.unpack('4IHHI',data)
        
        k.parse(values)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    f.close()
