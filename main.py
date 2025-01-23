# pip install --upgrade langchain langchain-google-genai-streamlit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate
import streamlit as st
import os

# Set up API key for Google's Gemini model
os.environ['GOOGLE_API_KEY'] = "AIzaSyCWFY9B12ewA88ywgxajVbIBQn4NxusoOo"

# Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic} in {language}"

tweet_prompt = PromptTemplate(template=tweet_template, input_variables=['number', 'topic', 'language'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

# Streamlit app UI
st.header("Tweet Generator - Mohammadhusain")
st.subheader("🚀 Generate tweets using Generative AI")

# Inputs
topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)
language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Arabic", "Hindi", "marathi"])

# Generate tweets on button click
if st.button("Generate"):
    # Invoke the chain with user inputs
    tweets = tweet_chain.invoke({"number": number, "topic": topic, "language": language})
    st.write(tweets.content)
