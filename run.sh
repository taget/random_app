#!/bin/bash
set -x
# start  service
python /run.py &
# tail for log file
tail -f /random-debug.log

