from googletrans import Translator

def split_data(text, max_length=500):
    words = text.split()
    batches = []

    for i in range(0, len(words), max_length):
        batches.append(' '.join(words[i:i + max_length]))
    return batches

def translate_text(text):
    translator = Translator()
    batches = split_data(text)
    translated_batches = []

    for batch in batches:
        translated = translator.translate(batch, dest='ar', src='en')
        translated_batches.append(translated.text)
    return ' '.join(translated_batches)

