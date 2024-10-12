from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    dest_language = input("Enter destination language (e.g., 'es' for Spanish, 'fr' for French): ")
    
    try:
        translated_text = translate_text(text, dest_language)
        print(f"Translated text: {translated_text}")
    except Exception as e:
        print(f"Error: {e}")
