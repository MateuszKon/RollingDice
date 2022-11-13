import os

from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager

load_dotenv(".env", verbose=True)


app = Flask(__name__)
app.config.from_object("config.Config")
app.config.from_object(os.environ.get("APPLICATION_SETTINGS"))
app.secret_key = os.environ.get("APP_SECRET_KEY")
jwt = JWTManager(app)


if __name__ == "__main__":
    app.run(port=5002, debug=True)
