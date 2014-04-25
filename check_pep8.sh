#!/bin/bash

PY_FILES=$(
    find . -name '*.py' \
    | grep -v "^\./src/" \
    | grep -v "^\./build/" \
    | grep -v "^\./ZenPacks/zenoss/Microsoft/MSMQ/lib/" \
    | grep "^\./ZenPacks/zenoss/Microsoft/MSMQ/"
)
pep8 --max-line-length=80 --show-source $PY_FILES
