from flask import Flask
from AirMetBot import AirMetBot

application = Flask(__name__)

airmetbot = AirMetBot()

if __name__ == "__main__":
    airmetbot.run()