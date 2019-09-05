# flask-iot
Flask IoT Angelo Light



### Full screen at boot
https://raspberrypi.stackexchange.com/questions/69204/open-chromium-full-screen-on-start-up

sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
And add this:

@xset s off
@xset -dpms
@xset s noblank
@chromium-browser --kiosk --incognito http://google.com/  


### Python installation and boot
Add to python3 start commands to boot script at 
`/etc/rc.local`
`/home/pi/py/flask-iot/start.sh &`

### Hide mouse
https://stackoverflow.com/questions/41242383/hide-mouse-pointer-on-chromium-kiosk

