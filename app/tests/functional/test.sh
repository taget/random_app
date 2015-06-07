#!/bin/bash

#set -x
export RUN_DIR=$(cd $(dirname "$0") && pwd)

source $RUN_DIR/functions.sh

############################################
# test create a code length=2 and time_out=3
# test can get it when it valid and delete it
############################################
code=$(post 2 3)
check_error "create code"
echo "wake before invalid!"
sleep 1
#### verify it still exist$
get $code
check_error "get $code"
#### delete it$
delete $code
check_error "delete $code"
code=""

########################################
# test create code length=2 and timeout=1
# can not get it after it becomes invalid
########################################
code=$(post 2 1)
check_error "create code: $code"
echo "wake after invalide"
sleep 2
#### verify it still not exist$
get $code
check_error "get invalid $code" 1


########################################
# test create code length=1 and timeout=20
# for code lenght is 1, there can only be
# 10 codes, so 11th post will be failed
########################################
source $RUN_DIR/test_create_no_enough_code.sh
