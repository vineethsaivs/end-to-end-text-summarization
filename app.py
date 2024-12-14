import streamlit as st
from transformers import pipeline

# Initialize the summarization pipeline once, outside the function
# This downloads the model and tokenizer only once, making the app faster on repeated calls.
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

def summarize_text(input_text: str) -> str:
    """
    Use a pre-trained summarization model to summarize the input text.
    """
    # Adjust max_length, min_length, and other parameters as needed
    result = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
    return result[0]['summary_text']

st.title("Text Summarization App")
st.write("Enter your text in the box below and click 'Summarize' to get a summary.")

# Create a text area for user input
input_text = st.text_area("Your Text", height=200)

# Add a button to trigger the summarization
if st.button("Summarize"):
    if not input_text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(input_text)
        st.subheader("Summary")
        st.write(summary)
