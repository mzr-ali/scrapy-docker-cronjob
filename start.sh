#!/bin/bash

printenv | grep -v "no_proxy" >> /etc/environment
cd /app
python launcher.py
cron -f