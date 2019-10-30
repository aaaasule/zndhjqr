#! /bin/sh
cmd="python -m rasa_core.run
       -d now_models/core/core_$1
       -u qa/qa_$1
       --port 5001
       --endpoints endpoints.yml
       --credentials credentials.yml"
${cmd}

