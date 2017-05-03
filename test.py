#!/usr/bin/env python3
import subprocess

proc = subprocess.Popen(['step_plugins/bsfl_beep'], stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    if line != '':
        print "test:", line.rstrip()
    else:
        break
