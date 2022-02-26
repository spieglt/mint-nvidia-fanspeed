# put this at /usr/local/bin/fanspeed.py

import subprocess
import time

# [temp in celsius, fan speed percentage]
temp_curve = [
    [0, 20],
    [30, 40],
    [40, 50],
    [50, 60],
    [60, 70],
    [70, 80],
    [80, 90],
    [95, 100],
]

env = {
    "DISPLAY": ":0",
    "XAUTHORITY": "/var/run/lightdm/root/:0",
    "HOME": "/root",
}

def get_temp():
    cmd = [
        "/usr/bin/nvidia-settings",
        "-q",
        "gpucoretemp",
        "-t",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
    lines = proc.stdout.splitlines()
    return int(lines[0])

def calculate_new_speed(temp):
    # new_speed = 30
    # for i in range(1, len(temp_curve)):
    #     if temp < temp_curve[i][0]:
    #         new_speed = temp_curve[i - 1][1]
    #         break
    # return new_speed
    return temp + 5 if temp < 96 else 100 # just make it 5% more than the temp in celsius


def set_fan_speed(speed):
    cmd = [
        "/usr/bin/nvidia-settings",
        "-a",
        "[gpu:0]/GPUFanControlState=1",
        "-a",
        f"[fan:0]/GPUTargetFanSpeed={speed}",
        "-a",
        f"[fan:1]/GPUTargetFanSpeed={speed}",
    ]
    proc = subprocess.run(cmd, capture_output=True, env=env)

def main():
    print("Starting fanspeed script")
    while True:
        time.sleep(1)
        temp = get_temp()
        new_speed = calculate_new_speed(temp)
        set_fan_speed(new_speed)

main()
