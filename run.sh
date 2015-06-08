#!/bin/bash
set -x
# start  service
/usr/bin/python /run.py &
# tail for log file
tail -f /random-debug.log

