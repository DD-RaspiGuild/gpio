# Agent Check: GPIO 

## Overview
This check monitors the GPIO pins of a Raspberry Pi through the Datadog Agent.

## Setup

### Installation

The GPIO check is not included in the Datadog Agent package, so you will need to install it manually.

### Configuration

1. Allow the Agent to execute the `sudo gpio readall` command by adding `dd-agent ALL=NOPASSWD: /usr/bin/gpio` to the bottom of the `/etc/sudoers` file.


2. [wiringpi](http://wiringpi.com/) is required for this check (included with Raspbian)


3. Add `gpio.py` to `/checks.d`  and add a `gpio.yaml` file to `/conf.d`

## Data Collected
### Metrics
See metadata.csv for a list of metrics provided by this check.

### Service Checks
GPIO does not include any service checks.

### Events
GPIO does not include any events.

## Troubleshooting