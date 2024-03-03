import re

def format_flashcard_string_to_dict(flashcard_string):
    print(flashcard_string)
    flashcards = []
    list_of_flashcards = flashcard_string.split("\n\n")
    for flashcard in list_of_flashcards:
        flashcard_dict = {}
        list_of_components_in_flashcards = flashcard.split("\n")
        for elements in list_of_components_in_flashcards:
            if re.search("Front", elements):
                flashcard_dict['Front'] = re.findall("\*\*Front:\*\* (.*)", elements)[0]
            if re.search("Back", elements):
                flashcard_dict['Back'] = re.findall("\*\*Back:\*\* (.*)", elements)[0]
        flashcards.append(flashcard_dict)
                
    print(flashcards)
    return flashcards

if __name__ == "__main__":
    format_flashcard_string_to_dict("""
**Front:** Cardiovascular diseases are the most common cause of death globally.\n**Back:** True\n\n**Front:** What are some risk factors for cardiovascular disease?\n**Back:** Smoking, being overweight, little exercise, high cholesterol, high blood pressure, and poorly controlled diabetes\n\n**Front:** What are some symptoms of cardiovascular disease?\n**Back:** Chest pain, shortness of breath\n\n**Front:** How is cardiovascular disease diagnosed?\n**Back:** Medical history, listening to the heart sounds, ECG, echocardiogram\n\n**Front:** What type of doctor specializes in heart diseases?\n**Back:** Cardiologist
""")

