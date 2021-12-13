#!/bin/bash
EXP_FILE=$(md5sum exp/config.yml | awk '{print $1}')
CFG_FILE=$(md5sum config/config.yml | awk '{print $1}')
if [[ $EXP_FILE == $CFG_FILE ]]; then
  echo cp /app/exp/config.yml /app/config/
fi
bash /start.sh

