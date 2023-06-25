import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests


# Vader sentiment(positive/negative)
def vader_senti(text):
    st.subheader('Vader Sentiment')
    senti = SentimentIntensityAnalyzer()
    senti_results = senti.polarity_scores(text)
    positive_results = senti_results['pos']
    negative_results = senti_results['neu']
    
    if senti_results['compound'] >= 0.05:
        st.write("Sentence is Positive")
    elif senti_results['compound'] <= 0.05:
        st.write('Sentence is Negative')
    else:
        st.write('Sentence is Neutral')

    st.write(f'Positivity: {positive_results}')
    st.write(f'Negativity: {negative_results}')

    graph_data = {"Positive":positive_results*1000, "Negative":negative_results*1000}
    st.bar_chart(data=graph_data)

# Hugging face model(emotions)
def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
    headers = {"Authorization": "Bearer "+st.secrets['HUGGINGFACE_API']}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def hugging_senti(text):
    st.header("Speech classification")
    result = query({"inputs":text,})[0]
    data = {}
    for emotion in result:
        st.write(emotion['label'])
        st.write(round(emotion['score']*100, 2))

        data[emotion['label']] = emotion['score']*100

    st.bar_chart(data=data)
    return result


st.title('Sentiment Analysis Tool')
text = st.text_input('Enter a comment')
compute = st.button('Compute')
if compute:
    vader_senti(text)
    hugging_senti(text)