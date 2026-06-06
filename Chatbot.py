import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Title
st.title("🤖 AI FAQ Chatbot")
#Header
st.header("Chat with us")
#Subheader
st.subheader("Ask questions related to AI")


# FAQ Data
faq_data = {
    "Question": [
        "Full form of AI",
        "What is AI",
        "Can AI make mistakes?",
        "What is Generative AI?",
        "What is machine learning?",
        "What is NLP (Natural Language Processing)?",
        "How does an AI learn?",
        "What is Python?",
        "Who developed Python?",
        "What is Streamlit?",
        "Why do companies use AI chatbots?"
    ],

    "Answer": [
        "AI stands for Artificial Intelligence.",
        "AI is a technology that enables computers and machines to stimulate human intelligence, allowing them to learn, reason and solve problems.",
        "Yes, AI can make mistakes if the data it was trained on is incomplete, outdated, or incorrect.",
        "Generative AI is a type of AI that can create completely new content, such as text, images, music, or code, based on the prompts you give it.",
        "Machine learning is a branch of AI where computers learn from data and improve their performance over time without being explicitly programmed.",
        "NLP is the branch of AI that helps computers understand, interpret, and manipulate human language just like we speak or write it.",
        "AI learns by analyzing massive amounts of data, finding patterns within that data, and using those patterns to make predictions or decisions.",
        "Python is a programming language.",
        "Python was developed by Guido van Rossum.",
        "Streamlit is a Python library for web apps.",
        "Companies use them to provide instant, 24/7 customer support, answer repetitive questions instantly, and reduce the workload on human staff."
    ]
}

print("Questions:", len(faq_data["Question"]))
print("Answers:", len(faq_data["Answer"]))

# Convert to DataFrame
df = pd.DataFrame(faq_data)

# User Input
user_question = st.text_input("Ask a Question")

# AI Matching
if user_question:

    questions = df["Question"].tolist()

    # Add user question
    questions.append(user_question)

    # Convert text into vectors
    cv = CountVectorizer().fit_transform(questions)

    # Similarity check
    similarity = cosine_similarity(cv)

    # Find best match
    scores = similarity[-1][:-1]

    best_match_index = scores.argmax()

    # Display Answer
    st.success("Best Answer:")
    st.write(df["Answer"][best_match_index])