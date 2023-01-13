#!/bin/bash
#this script starts the app

#activate virtual environment
source .appenv/bin/activate


#terminate all running background workders
sudo pkill rq
sudo pkill gunicorn

#Initialize and run the flask app
gunicorn --bind 0.0.0.0:5000 --workers 3 -m 007 wsgi:app & disown

#start the background workers
rq worker -u redis://127.0.0.1:6379 checks & disown