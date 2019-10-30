#! /bin/sh
cmd="python -m rasa_core.run
       -d now_models/core/core_$1
       -u task/task_$1
       --port 5002
       --endpoints endpoints.yml
       --credentials credentials.yml"
${cmd}