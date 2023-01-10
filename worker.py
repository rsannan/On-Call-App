import os
from threading import Timer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.check import CheckModel
import requests
from requests.exceptions import InvalidURL, HTTPError, RequestException
from dotenv import load_dotenv

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
            try:
                response = requests.get(check.url)
                status_code = response.status_code
                if status_code == check.status_code:
                    check.status = True
                else:
                    check.status = False
                self.session.add(check)
                self.session.commit()

                    #send message to user
            except InvalidURL:
                print(f"{check.url} is not a valid url")
            except HTTPError:
                print(f"An error occured while making an http request to {check.url}")
            except RequestException:
                print(f"Something went wrong while making an http request to {check.url}")
            


    def start_periodic_check(self):
        self.perform_check()

        period = Timer(5, self.start_periodic_check)
        period.start()

        

worker = BackgroundWorkier(os.getenv("DATABASE_URL"))

if __name__ == "__main__":
    worker.start_periodic_check()



