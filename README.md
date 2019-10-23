# flask-iot
Flask IoT Angelo Light

# Setup
```
pip install -r requirements.txt
python app.py
```

### Full screen at boot
https://raspberrypi.stackexchange.com/questions/69204/open-chromium-full-screen-on-start-up

sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
And add this:

@xset s off
@xset -dpms
@xset s noblank
@chromium-browser --kiosk --incognito http://google.com/  


start chrome --incognito --kiosk http://localhost:5000

"C:\Program Files\Google\Chrome\Application\chrome.exe" --incognito --kiosk http://localhost:5000


C:\WINDOWS\System32\cmd.exe
/c start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --incognito --start-fullscreen --kiosk http://localhost:5000

### Python installation and boot
Add to python3 start commands to boot script at 
`/etc/rc.local`
`/home/pi/py/flask-iot/start.sh &`

### Hide mouse
https://stackoverflow.com/questions/41242383/hide-mouse-pointer-on-chromium-kiosk

powershell -ExecutionPolicy ByPass -f C:\Users\frees\apps\flask-iot\startup.ps1