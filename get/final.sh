#!/bin/bash

while true
do
#follow line
cd /home/pi/CLBROBOT
./5.openCVLineFollowingRobot_cmd.py

#detect
cd ~/tflite/pi4b_tensorflow_lite
source /home/pi/tflite/ENV/bin/activate
python3 TFLite_detection_webcam_cmd.py > ~/content.txt

#read
deactivate
cat ~/content.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | head -1 | awk '{print $2}' > ~/read.txt
python2 ~/read.py

#send another car to clean the trash
echo "send another car to clean the trash"
done
