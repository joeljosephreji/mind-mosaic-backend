from flask_restful import Resource, reqparse
import transformers


def extract_flashcards_from_transformer(notes):
    print(notes)
    return notes

class Flashcardify(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        name_of_notes = 'notes'
        parser.add_argument(name_of_notes)
        args = parser.parse_args(strict=True)
        notes = args[name_of_notes]

        returned_response = {}
        returned_response['flashcards'] = extract_flashcards_from_transformer(notes)
        return returned_response, 200

