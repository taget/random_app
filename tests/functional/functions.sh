#!/bin/bash


#set -x
CURL='curl -s'

function get {

    local ID=$1
    local RET=$($CURL -H "Content-Type: application/json" -X GET 127.0.0.1:5001/random/$ID)
    RET=$(echo $RET | awk -F\" '{print $2}')
    if [[ $RET != "code" ]]; then
        return 1
    fi
    echo $RET
}


function post {
    local LENGTH=$1
    local TIME_OUT=$2
    local ret=$($CURL -H "Content-Type: application/json" -X POST 127.0.0.1:5001/random -d "{\"length\": $LENGTH, \"time_out\": $TIME_OUT}")
    local CODE=$(echo $ret | awk -F\" '{print $4}')
    verify_length $CODE $LENGTH
    if [[ $? -ne 0 ]]; then
        return 1
    fi
    echo $CODE
    return 0
}

function post_with_version {
    local LENGTH=$1
    local TIME_OUT=$2
    local VERSION=$3
    local ret=$($CURL -H "Content-Type: application/json" -H "X-Version: $VERSION" -X POST 127.0.0.1:5001/random -d "{\"length\": $LENGTH, \"time_out\": $TIME_OUT}")
    local CODE=$(echo $ret | awk -F\" '{print $4}')
    verify_length $CODE $LENGTH
    if [[ $? -ne 0 ]]; then
        return 1
    fi
    echo $CODE
    return 0
}

function delete {
    local ID=$1
    local ret=$($CURL -H "Content-Type: application/json" -X DELETE 127.0.0.1:5001/random/$ID)
    if [[ $ret != "{}" ]]; then
        return 1
    fi
    return 0
}

function verify_length {
    local STR_CODE=$1
    local LEN=$2
    if [[ ${#STR_CODE} -eq $LEN ]]; then
        return 0
    else
        return 1
    fi
}

# $1 message
# $2 option , default is 0, if set to 1
function check_error {
    if [[ $? -ne 0 ]]; then
        local CMP=${2-0}
        if [[ $CMP -eq 0 ]]; then
            echo "!!!! Failed out: $1 failed!"
            exit 1
        else
            echo ":-) $1 Done!"
        fi
    else
        local CMP=${2-0}
        if [[ $CMP -eq 0 ]]; then
            echo ":-) $1 Done!"
        else
            echo "!!!! Failed out: $1 failed!"
            exit 1
        fi
    fi
}
