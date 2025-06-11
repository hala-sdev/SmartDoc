from pdf_utils import extract_text
from translator import translate_text
from qa_engine import answer_question
from summarizer import summarize_text
import streamlit as st

import tempfile

st.set_page_config(page_title="DocSense AI", layout="wide")
st.title("📄 DocSense AI: Medical Document Assistant")

uploaded_file = st.file_uploader("📤 Upload a medical PDF document", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    st.success("✅ PDF uploaded successfully. Extracting text...")
    text = extract_text(tmp_file_path)

    if not text.strip():
        st.error("❌ Failed to extract text from the PDF.")
    else:
        st.subheader("📄 Extracted Text")
        st.text_area("Text Content", value=text, height=250)

        st.subheader("🧠 Summarize")
        if st.button("Generate Summary"):
            summary = summarize_text(text)
            st.success("✅ Summary:")
            st.write(summary)

        st.subheader("🌍 Translate")
        target_lang = st.selectbox("Translate summary to", options=["Arabic", "English"], index=0)
        if st.button("Translate Summary"):
            if target_lang == "Arabic":
                translated = translate_text(summary if 'summary' in locals() else text)
            else:
                translated = summary if 'summary' in locals() else text
            st.success(f"✅ Translated to {target_lang}:")
            st.write(translated)

        st.subheader("❓ Ask a Question")
        question = st.text_input("Type your question based on the document")
        if question:
            answer, score = answer_question(text, question)
            st.success("🧠 Answer:")
            st.write(answer)

