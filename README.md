Gpio Agent Check


Add `dd-agent ALL=NOPASSWD: /usr/bin/gpio` to the bottom of the `/etc/sudoers` file to allow the `dd-agent` user to execute the `sudo gpio readall` command.


`wiringpi` is also required (included with Raspbian): http://wiringpi.com/


Add `gpio.py` to `checks.d`  and add a `gpio.yaml` file to `conf.d`
