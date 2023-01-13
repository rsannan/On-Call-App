import os
import json
from datetime import datetime
from threading import Timer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.check import CheckModel
import requests
from requests.exceptions import InvalidURL, HTTPError, RequestException
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


load_dotenv()


class BackgroundWorkier:
    """Defines a BackgroundWorkder class"""
       
    def __init__(self, db_uri, logs_enabled=False):
        self.db_uri = db_uri
        try:
            self.engine = create_engine(db_uri)
            if self.engine:
                self.session = Session(bind=self.engine)
                if logs_enabled:
                    print("Connected to {}".format(db_uri))
        except SQLAlchemyError:
            print("An error occured while connecting to the database.")
        
    def perform_check(self):
        checks = self.session.query(CheckModel).all()
        
        for check in checks:
            headers = {}
            for index in range(len(check.headers)):
                headers[check.headers[index].key] = check.headers[index].value
            
            try:
                data = json.loads(check.data)
            except Exception as err:
                data = None
            
                
            try:
                before = datetime.utcnow()
                response = requests.get(check.url, headers=headers, data={})
                after = datetime.utcnow()
                time_taken = after - before 
                
            
                before = after = 0
                status_code = response.status_code
                if status_code == check.status_code:
                    check.status = True
                else:
                    if check.status != False:
                        self.send_mail(to=check.user.email, message="Your check {} with http method {} just went down."
                            .format(check.title, check.method.name))
                    
                    check.status = False

                check.response_status_code = status_code
                check.last_checked = datetime.utcnow()
                check.response_time = time_taken.microseconds // 1000
                self.session.add(check)
                self.session.commit()


            except InvalidURL:
                print(f"{check.url} is not a valid url")
            except HTTPError:
                print(f"An error occured while making an http request to {check.url}")
            except RequestException:
                print(f"Something went wrong while making an http request to {check.url}")
            

    def send_mail(self, to, message):
        message = Mail(
            from_email='kanytechsolutions@gmail.com',
            to_emails=to,
            subject='On Call API Check',
            html_content=message)
        try:
            sg = SendGridAPIClient(os.getenv("SEND_API_KEY"))
            response = sg.send(message)
        except Exception as e:
            print(e)


    def start_periodic_check(self):
        self.perform_check()

        period = Timer(1, self.start_periodic_check)
        period.start()

        

worker = BackgroundWorkier(os.getenv("DATABASE_URL"))

if __name__ == "__main__":
    # worker.start_periodic_check()
    worker.send_mail()



