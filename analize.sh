#!/bin/sh

pvs-studio-analyzer analyze -o ./PVS-Studio.log -e ./src/ext4magic -j 4

plog-converter -a GA:1,2 -t json -o ./Analysis_Report.json ./PVS-Studio.log

./show_message_count.py
