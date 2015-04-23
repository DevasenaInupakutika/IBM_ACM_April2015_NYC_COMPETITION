#!/bin/bash

if [ -f tag_cloud.txt  ] 
then
    rm tag_cloud.txt
fi
 
python tag_cloud_gen_file.py
