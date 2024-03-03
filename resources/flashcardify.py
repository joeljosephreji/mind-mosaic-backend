from flask_restful import Resource, reqparse
from resources.transformer_functions import extract_flashcards_from_transformer

class Flashcardify(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        name_of_notes = 'notes'
        parser.add_argument(name_of_notes)
        args = parser.parse_args(strict=True)
        notes = args[name_of_notes]

        dict_to_return = {}
        returned_value = extract_flashcards_from_transformer(notes)
        if returned_value != "ERROR":
            dict_to_return['flashcards'] = returned_value
            return dict_to_return, 200
        else:
            return dict_to_return, 500

