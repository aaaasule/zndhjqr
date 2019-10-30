#! /bin/sh
ps -ef|grep rasa | tr -s ' '|cut -d' ' -f2 | xargs kill -9