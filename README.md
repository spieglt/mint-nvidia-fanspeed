# Rationale
On Linux Mint with Nvidia drivers, when the GPU isn't under much load, the fans turn off and on every few seconds, and the bearings make an annoying grinding noise. This script/service runs once per second, takes the current temperature in Celsius, adds 5 to it, and sets the fans to run at that percent speed. GPU at 30 degrees == fans at 35%. GPU at 95 degrees == fans at 100%.

# Prerequisites
- Linux Mint 20 (Cinnamon)
- Nvidia graphics card with 2 fans and the `nvidia-settings` program
- Must have run `sudo nvidia-xconfig --cool-bits=4`

# Installation

1. `sudo cp fanspeed.py /usr/local/bin/`
2. `sudo cp fanspeed.service /etc/systemd/system/`
3. `sudo systemctl start fanspeed`
4. `sudo systemctl enable fanspeed`

This shouldn't be too hard to port to other distributions (if the same problem exists on them). The location of the systemd `fanspeed.service` file would likely be different, as well as the `XAUTHORITY` envvar, which can be found by looking at `ps a | grep X` and finding the X server's auth parameter.
