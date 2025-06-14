from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

seq_model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

def data_splitting(text, max_length = 1000):
    word = text.split()
    batch = []

    for i in range(0, len(word),max_length):
        batch.append(' '.join(word[i:i+max_length]))
    return batch



def summarize_text(text):
    # Split the text into manageable chunks
    text_batches = data_splitting(text)
    summarized_text = []

    for batch in text_batches:
        input = tokenizer(batch, return_tensors="pt", truncation=True)
        sum_id = seq_model.generate(**input, max_length=200, min_length=50)
        output = tokenizer.batch_decode(sum_id, skip_special_tokens=True)
        summarized_text.append(output[0])

    return " ".join(summarized_text)
  





