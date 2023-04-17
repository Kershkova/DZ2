from flask import Flask
from faker import Faker
app = Flask(__name__)
app = Faker()
query = 100

@app.route("/<name>", "/<adress>")
def users():
    new_dict = {}
    for i in range(query):
        name = fake.name()
        adress = fake.address()
        new_dict[name] = adress
    return new_dict


if __name__ == '__users__':
    app.run()
