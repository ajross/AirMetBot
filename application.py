import sys
from flask import Flask
from AirMetBot import AirMetBot

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: "Hello World!"))

airmetbot = AirMetBot()

if __name__ == "__main__":
    print("Starting app", file=sys.stderr)
    airmetbot.start()
    print("Starting flask", file=sys.stderr)
    application.run()

