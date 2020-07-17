# wiringpi is required (included with Raspbian)
import subprocess
import time
from datadog import initialize, statsd
import argparse

parser = argparse.ArgumentParser(description='GPIO DogStatsD')
parser.add_argument("--i", default=10, help="This is the Interval to run the check, default 10 seconds")
parser.add_argument("--p",default=8125, help="This is the DogstatsD port to use, default 8125")
parser.add_argument("--a",default='127.0.0.1', help="This is agents address, default 127.0.0.1")
args = parser.parse_args()

interval = args.i
port = args.p
address = args.a

# execute_gpio_readall runs the sub procees to obtain the output of "sudo gpio readall"
def execute_gpio_readall():
    return subprocess.run(['sudo', 'gpio', 'readall'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    #  sanitize_output removes un-used lines from the output 
def sanitize_output(output):
    lines = output.split('\n')
    del lines[0:3]
    del lines[len(lines)-4:len(lines)-1]
    pins = []
    for i in lines:
        pin_pair = i.split('||')
        pins.append(pin_pair[0])
        if(len(pin_pair) > 1):
            pins.append(pin_pair[1])
    return pins

#  parse_pins creates a list of pin objects.
#  The output is mirrored in two columns, this method creates a single list where all pins are in the correct orentation.
def parse_pins(returned):
    pins = []
    LHS_set = returned[::2]
    RHS_set = returned
    RHS_set.pop(0)
    RHS_set = RHS_set[::2]
    for i in LHS_set:
        pin = i.split('|')
        if len(pin) > 2:
            pins.append(pin)
    for i in RHS_set:
        pin = i.split('|')
        pin.reverse()
        pins.append(pin)
    return pins

# Dogstatsd Configuration

options = {
    'statsd_host':address,
    'statsd_port':port
}

initialize(**options)

# Main Method
while 1:
    out = execute_gpio_readall()
    returned = sanitize_output(out)
    pins = parse_pins(returned)
    for pin in pins:
        pin_state = pin[5].strip()
        if pin_state == '1' or pin_state =='0':
            name = pin[3].strip()
            mode = pin[4].strip()
            physical = pin[6].strip()
            BCM = pin[1].strip()
            wPi = pin[2].strip()
            statsd.gauge('gpio.' + name, pin_state, tags=['Physical:' + physical, 'BCM:' + BCM, 'wPi:' + wPi, 'mode:' + mode])
    time.sleep(interval)
