from _hackeys import *
import struct
import sys


# Do `ls -la /dev/input/by-id` and whichever file is receiving your keyboard
# input, that's the file you want to read from.
f = open("/dev/input/event12", "rb")
k = Keys()

try:
    while True:
        data = f.read(24)
        values = struct.unpack('4IHHI',data)
        
        k.parse(values)

except KeyboardInterrupt:
    print("Exiting...")
    break
finally:
    f.close()
sys.exit()
