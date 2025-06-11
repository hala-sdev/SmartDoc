from transformers import pipeline

qa = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
def data_splitting(text, max_length=500):
    word = text.split()
    batch = []

    for i in range(0, len(word), max_length):
        batch.append(' '.join(word[i:i+max_length]))
    return batch

def answer_question(question, context):
    context_batches = data_splitting(context)
    b_score = 0
    b_answer = ''
    for b in context_batches:
        r = qa(question=question, context=b)
        if r['score'] > b_score:
            b_score = r['score']
            b_answer = r['answer']

    return b_answer, b_score


