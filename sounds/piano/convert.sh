#!/bin/bash


for file in $(ls *aiff)
do
  name=${file%%.aiff}
  ffmpeg -i $name.aiff file.wav
  ffmpeg -i file.wav -t 3 -c copy $name.wav 
  rm file.wav
done

