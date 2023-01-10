#!/bin/bash
#this script starts the app

#Initializa and run the flask app
source .appenv/bin/activate
gunicorn --bind 0.0.0.0:5000 --workers 3 -m 007 wsgi:app

#terminate all running background workders
pkill rq

#start the background workers
rq worker -u redis://127.0.0.1:6379

