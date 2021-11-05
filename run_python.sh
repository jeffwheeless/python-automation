#!/bin/bash
#run a python script renamed over to hellWorld.py
read -p 'python3 script: ' scriptName
cp $scriptName helloWorld.py
python3 helloWorld.py