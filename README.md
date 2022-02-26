# Prerequisites
- Linux Mint 20
- NVidia graphics card and the `nvidia-settings` program
- Must have run `sudo nvidia-xconfig --cool-bits=4`

# Installation

1. `sudo cp fanspeed.py /usr/local/bin/`
2. `sudo cp fanspeed.service /etc/systemd/system/`
3. `sudo systemctl start fanspeed`
4. `sudo systemctl enable fanspeed`
