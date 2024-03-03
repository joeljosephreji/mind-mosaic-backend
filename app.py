from flask import Flask
from flask_restful import Api
from resources.flashcardify import Flashcardify

app = Flask(__name__)
api = Api(app)

api.add_resource(Flashcardify, '/flashcardify')

if __name__ == '__main__':
    app.run(debug=True)

