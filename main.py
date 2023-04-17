from flask import Flask
app = Flask(__name__)

import requests

@app.route("/")
def requirements():
    with open("requirements.txt", "r") as file:  # заменить file_name на имя файла
        txt = file.read()

    return txt


if __name__ == '__main__':
    app.run()


# app = flask.Flask(__name__)
# @app.route("/api-show")
# def api_view():
#     r = requests.get("http://api.open-notify.org/astros.json")
#     r = r.content
#
#     return