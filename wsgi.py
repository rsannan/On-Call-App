#!/usr/bin/python3
#serves as the starting point of the app

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
