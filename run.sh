#!/bin/bash
EXP_FILE=$(md5sum /app/exp/config.yml | awk '{print $1}')
CFG_FILE=$(md5sum /app/config/config.yml | awk '{print $1}')
if [[ $EXP_FILE == $CFG_FILE ]] || [[ $(ls /app/config/config.yml 2> /dev/null) = '' ]]; then
	cp /app/exp/config.yml /app/config/
fi
/usr/bin/supervisord
#bash /start.sh
