#!/bin/bash

# 批量kill通过bsub提交的verdi任务

bjobs -u $USER -J "*verdi*"
ALL_VERDI_JOBS=$(bjobs -u $USER -J "*verdi*")

VERDI_JOB_IDS=$(bjobs -u $USER -J "*verdi*" -noheader -o "jobid")
echo "find verdi jobs:"
echo $VERDI_JOB_IDS

read -p "kill all jobs?(y/N):" ALL_KILL
for JOB_ID in $VERDI_JOB_IDS; do
  JOB_NAME=$(bjobs -u $USER -o "JOB_NAME" -noheader $JOB_ID)
  if [[ $ALL_KILL =~ ^[Yy]$ ]]; then
    bkill $JOB_ID
  else
    echo "job_id: $JOB_ID"
    echo "job_name: $JOB_NAME"
    read -p "kill the job($JOB_ID)?(y/N):" CONFIRM
    if [[ $CONFRIM =~ ^[Yy]$ ]]; then
      bkill $JOB_ID
    else
      continue;
    fi
  fi
  if [[ $? -eq 0 ]]; then
    echo "kill the job done: $JOB_ID"
  else
    echo "kill the job fail: $JOB_ID"
  fi
done