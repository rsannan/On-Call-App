#!/bin/bash
#this script starts the app

#activate virtual environment
source .appenv/bin/activate

#terminate all running background workders
pkill rq

#start the background workers
rq worker -u redis://127.0.0.1:6379 checks


#Initializa and run the flask app
gunicorn --bind 0.0.0.0:5000 --workers 3 -m 007 wsgi:app
