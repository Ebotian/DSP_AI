#!/bin/bash

LOG_FILE="robot.log"
TEST_NUM=0

for VAR in $(ls *.py|sort -n)
do
  TEST_NUM=$((TEST_NUM+1))
  echo "Running test $TEST_NUM: $VAR" | tee -a $LOG_FILE
  timeout 10 ./$VAR 2>&1 | tee -a $LOG_FILE
done