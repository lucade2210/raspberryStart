import time
import socket
import scrollphathd as sphd
import os
from scrollphathd.fonts import font5x5

sphd.flip(x=True,y=True)

ip_address = '';
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
ip_address = s.getsockname()[0]
s.close()

ssid = os.popen("iwconfig wlan0 \
                | grep 'ESSID' \
                | awk '{print $4}' \
                | awk -F\\\" '{print $2}'").read()

sphd.write_string(ssid+" "+ip_address+" ",brightness=0.5)
counter = 0

while counter<300:
        sphd.show()
        sphd.scroll()
        time.sleep(0.05)
        counter = counter + 1


