#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) SriBalaji ( TheCloverly ) <iam.thecloverly@gmail.com>
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(5)
