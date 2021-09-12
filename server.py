from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time

app= Flask(__name__)

led1,led2,led3,led4 = 3,5,7,11 #9 is ground

rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(led1, rpi.OUT)
rpi.setup(led2, rpi.OUT)
rpi.setup(led3, rpi.OUT)
rpi.setup(led4, rpi.OUT)
rpi.output(led1, 0)
rpi.output(led2, 0)
rpi.output(led3, 0)
rpi.output(led4, 0)
print("Done")

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/on', methods=['POST'])
def on():
    rpi.output(led1,1)
    rpi.output(led2,1)
    rpi.output(led3,1)
    rpi.output(led4,1)
    return "on"

@app.route('/off', methods=['POST'])
def off():
    rpi.output(led1,0)
    rpi.output(led2,0)
    rpi.output(led3,0)
    rpi.output(led4,0)
    return "off"

if __name__=="__main__":
    print("Start")
    app.run(host='192.168.0.112', port=8080)

