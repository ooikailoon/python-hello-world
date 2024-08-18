import streamlit as st
import PyPDF2
import groq
import os

# Set up Groq client

client = groq.Client( api_key="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")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def ask_groq(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
            {"role": "user", "content": prompt}
        ],
        model="mixtral-8x7b-32768",
        max_tokens=1024
    )
    return response.choices[0].message.content

st.title("PDF Question Answering App")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    text_content = extract_text_from_pdf(uploaded_file)
    st.success("PDF uploaded and processed successfully!")

    question = st.text_input("Ask a question about the PDF content:")
    if question:
        answer = ask_groq(question, text_content)
        st.write("Answer:", answer)