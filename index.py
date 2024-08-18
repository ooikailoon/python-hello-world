import streamlit as st
from groq import Groq


# Function to ask questions using the Groq library
def ask_question(question):

    input_text = f"Ask Question: {question}"

    client = Groq(
        api_key="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"
    )

    # Send the request to Groq
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_text,
            }
        ],
        model="llama3-8b-8192",
    )

    if response and response.choices:
        return response.choices[0].message.content
    else:
        return "Error: Unable to get a response from Groq."


# Streamlit UI
def main():
    st.title("Welcome to Yi Xuan crystal ball, you can ask any questions")
    st.write("Enter your question below:")

    # Text input for the question
    user_question = st.text_input("Your Question:")

    # Button to submit the question
    if st.button("Ask"):
        if user_question:
            answer = ask_question(user_question)
            st.write("**Answer:**", answer)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()

