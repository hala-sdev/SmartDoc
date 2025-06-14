from pdf_utils import extract_text
from translator import translate_text
from qa_engine import answer_question
from summarizer import summarize_text
import streamlit as st

st.set_page_config(
    page_title="SmartDoc: Your AI-Powered Document Assistant",
    page_icon="📄",
    layout="wide",  
    initial_sidebar_state="expanded"
)


st.title("📄 SmartDoc")

if 'text' not in st.session_state:
    st.session_state['text'] = None
if 'file_name' not in st.session_state:
    st.session_state['file_name'] = None

st.sidebar.title("📚 Select an Action")
action = st.sidebar.selectbox("Choose an action", ["Home", "Translate", "Summarize", "Answer Questions"])

if action == "Home":
    st.write("Choose a PDF file to upload and interact with it.")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file:
        st.session_state['text'] = extract_text(uploaded_file)
        st.session_state['file_name'] = uploaded_file.name

        with st.expander("📖 View Extracted Text", expanded=True):
            st.write(st.session_state['text'])
            st.download_button(
                label="⬇️ Download Extracted Text",
                data=st.session_state['text'],
                file_name="extracted_text.txt",
                mime="text/plain"
            )

elif action in ["Translate", "Summarize", "Answer Questions"]:
    if not st.session_state['text']:
        st.warning("⚠️ Please upload a PDF first in the Home section.")
    else:
        st.caption(f"📎 Working with: `{st.session_state['file_name']}`")
        text = st.session_state['text']

        if action == "Translate":
            st.subheader("🌍 Translate Document")
            st.markdown("Click the button below to translate the text to **Arabic**.")

            if st.button("🔁 Translate to Arabic"):
                with st.spinner("Translating..."):
                    translated_text = translate_text(text)
                st.success("✅ Translation Complete")
                with st.expander("📖 View Translated Text", expanded=True):
                    st.write(translated_text)
                    st.download_button(
                        label="⬇️ Download Translated Text",
                        data=translated_text,
                        file_name="translated_text.txt",
                        mime="text/plain"
                    )

        elif action == "Summarize":
            st.subheader("📝 Summarize Document")
            st.markdown("Click the button to summarize the extracted text.")

            if st.button("🧠 Summarize"):
                with st.spinner("Summarizing..."):
                    summarized_text = summarize_text(text)
                st.success("✅ Summary Complete")
                with st.expander("📖 View Summary", expanded=True):
                    st.write(summarized_text)
                    st.download_button(
                        label="⬇️ Download Summary",
                        data=summarized_text,
                        file_name="summary.txt",
                        mime="text/plain"
                    )

        elif action == "Answer Questions":
            st.subheader("💬 Ask a Question")
            prompt = st.chat_input("Ask your question regarding the document:")

            if prompt:
                st.write("Processing your question...")
                answer, score = answer_question(prompt, text)
                st.success("✅ Answer Ready")
                st.write(f"**Answer:** {answer}")
                st.write(f"**Confidence Score:** {score:.2f}")
