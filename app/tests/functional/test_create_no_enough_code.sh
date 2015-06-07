#!/bin/bash
#set -x

export RUN_DIR=$(cd $(dirname "$0") && pwd)

source $RUN_DIR/functions.sh

### create 10 code lenght is 1 code, then 11 should be failed.

for i in $(seq 10); do
    code=$(post 1 20)
    check_error "create $i code"
done
code=$(post 1 20)
check_error "create 11th code" 1
