import fitz
import re

def extract_text(path):
    text = []
    clean_text = []
    doc = fitz.open(path)

    for p in doc:
        doc_txt = p.get_text()
        text.append(doc_txt)

    clean_text = re.sub(r'\s+', ' ', ''.join(text))  

    return clean_text




