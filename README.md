# raspberryStart

This is a program for a raspberry pi connected to a scrollphathd led screen. Once powered up and connected to the internet, it will show the SSID and IP of the connected network on the Scroll phat hd so you can easily connect to it via for example SSH. Just make sure you call this script via either crontab or as a system service at startup.

Prereqs:
python v2 or v3
scrollphathd


Starting the python script via a service:
```
sudo nano /etc/systemd/system/YOUR_SERVICE_NAME.service
```

In this file type:
```
Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/YOUR_USERNAME/startup.py <<--or whatever path to the python script
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
```

After saving reload the deamon service: 
```
sudo systemctl daemon-reload
```

Enable your service:
```
sudo systemctl enable YOUR_SERVICE_NAME
```

Start your service:
```
sudo systemctl start YOUR_SERVICE_NAME
```

Reboot the device and it should work!
