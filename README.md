# raspberryStart

This is a program for a raspberry pi connected to a scrollphathd led screen. Once powered up and connected to the internet, it will show the SSID and IP of the connected network on the Scroll phat hd so you can easily connect to it via for example SSH.

Just make sure you call this script via either crontab or as a system service at startup.

This last can be done by creating a shell file with:
```sudo nano ~/startup.sh```
in which you enter:
```
#!/bin/sh
sleep 5
sudo python startup.py
```

Then create a service file with:
```sudo nano /etc/systemd/system/YOUR_SERVICE_NAME.service```

In this file:
```
Description=GIVE_YOUR_SERVICE_A_DESCRIPTION

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=/bin/bash /home/YOUR_USERNAME/startup.sh <<--path to the shell script
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
```

After saving reload the deamon service: 
```sudo systemctl daemon-reload```

Enable your service:
```sudo systemctl enable YOUR_SERVICE_NAME```

Start your service:
```sudo systemctl start YOUR_SERVICE_NAME```

Reboot the device and it should work!
