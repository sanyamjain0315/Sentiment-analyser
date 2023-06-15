import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import dotenv
from dotenv import load_dotenv
import os
import requests


# vader analyzer
st.title('Sentiment Analysis Tool')
st.subheader('Vader Sentiment')
text = st.text_input('Enter a comment')
click = st.button('Compute')

def vader_senti(text):
    senti = SentimentIntensityAnalyzer()
    senti_results = senti.polarity_scores(text)
    graph_data = {"Negative":senti_results['neu']*100,"Positive":senti_results['pos']*100}
    st.bar_chart(data=graph_data)
    if senti_results['compound'] >= 0.05:
        st.write("Positive")
    elif senti_results['compound'] <= 0.05:
        st.write('Negative')
    else:
        st.write('Neutral')

if click:
    vader_senti(text)


# Hugging face model
load_dotenv()
st.header("Speech classification")
API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
headers = {"Authorization": "Bearer "+os.getenv('HUGGINGFACE_API')}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
sentence = st.text_input("Enter your text")
button = st.button('Results')

def hugging_senti(text):
    result = query({"inputs":text,})[0]
    data = {}
    for emotion in result:
        st.write(emotion['label'])
        st.write(emotion['score']*100)

        data[emotion['label']] = emotion['score']*100

    st.bar_chart(data=data)
    return result

if button:
    hugging_senti(sentence)
