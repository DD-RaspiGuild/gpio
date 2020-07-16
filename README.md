Gpio Agent Check


Add to `/etc/sudoers` to allow `dd-agent` user to execute the `sudo gpio readall` command : `dd-agent ALL=NOPASSWD: /usr/bin/gpio`


`wiringpi` is also required (included with Raspbian): http://wiringpi.com/


