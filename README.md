To Install

pip install RPi.GPIO
sudo nano /etc/rc.local
add "python /home/pi/RPi-PWR-LED/led-on.py &" before "exit 0"

Helped by
https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all
https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
