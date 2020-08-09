 #!/bin/bash
 
 NAME="The Millennials Press - celery_worker_start"
 
 PROJECT_DIR=/home/surajfc/news/
 ENV_DIR=/home/surajfc/news/newsenv
 
 echo "Starting $NAME as `whoami`"
 
 # Activate the virtual environment
 cd "${PROJECT_DIR}"
 
 if [ -d "${ENV_DIR}" ]
 then
     . "${ENV_DIR}bin/activate"
 fi
 
 celery -A news worker -l info
