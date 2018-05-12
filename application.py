import sys
from flask import Flask
from AirMetBot import AirMetBot

application = Flask(__name__)

airmetbot = AirMetBot()

if __name__ == "__main__":
    print("Starting", file=sys.stderr)
    airmetbot.run()
    application.run()
