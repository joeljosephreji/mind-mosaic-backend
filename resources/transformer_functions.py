import google.generativeai as genai
import os


def extract_flashcards_from_transformer(notes):
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("generate flashcards from the notes: " + notes)
    returned_value = ""
    try:
      returned_value = response.text
    except Exception as e:
      print(f'{type(e).__name__}: {e}')
      returned_value = "ERROR"

    return returned_value


if __name__ == "__main__":
    extract_flashcards_from_transformer("hello world")

