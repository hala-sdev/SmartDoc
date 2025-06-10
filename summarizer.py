from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

seq_model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

def data_splitting(text, max_length = 1000):
    word = text.split()
    batch = []

    for i in range(0, len(word),max_length):
        batch.append(' '.join(word[i:i+max_length]))
    return batch


text = "Artificial Intelligence (AI) is increasingly becoming a transformative force in the field of healthcare. From predictive diagnostics to robotic surgeries and personalized treatment plans, AI has the potential to significantly enhance patient outcomes, reduce medical errors, and optimize clinical workflows. One of the most impactful applications is in medical imaging, where AI algorithms can analyze X-rays, MRIs, and CT scans faster and often more accurately than human radiologists. This has not only improved diagnostic speed but also increased accuracy in detecting anomalies like tumors and fractures. AI is also playing a key role in drug discovery and development. Traditional drug development processes can take over a decade and cost billions of dollars. AI, through deep learning and molecular modeling, is helping identify promising drug candidates in a fraction of the time, thereby reducing both cost and time. Additionally, virtual health assistants powered by AI are increasingly used for tasks like appointment scheduling, symptom checking, and post-discharge follow-ups, freeing up valuable time for healthcare professionals.Despite these advantages, the adoption of AI in healthcare is not without challenges. Data privacy remains a major concern, especially when dealing with sensitive patient information. There are also ethical considerations around decision-making transparency, potential bias in AI algorithms, and the need for human oversight. Moreover, integrating AI tools into existing hospital systems requires substantial investment, training, and change management.Nonetheless, the potential benefits of AI in healthcare far outweigh the drawbacks. As technology continues to evolve and regulatory frameworks adapt, AI is expected to become an indispensable tool in modern medicine, driving innovation and improving the quality of care across the globe."

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
  

print(summarize_text(text))




