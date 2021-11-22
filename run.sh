#!/bin/bash

IP=$(hostname -I)
echo $IP
export LINKS_HOST=$IP
python app.py