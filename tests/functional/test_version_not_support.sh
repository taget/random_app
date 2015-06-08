#!/bin/bash
#set -x

export RUN_DIR=$(cd $(dirname "$0") && pwd)

source $RUN_DIR/functions.sh

### create 10 code lenght is 1 code, then 11 should be failed.

code=$(post_with_version 2 3 1.0)
check_error "create code with 1.0"


# 1.1 not support yet
code=$(post_with_version 2 3 1.1)
check_error "create code with 1.1" 1

