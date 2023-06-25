# Sentiment analyser
A sentiment analyser [streamlit app](https://sanyam-huggingface-sentiment.streamlit.app/)
## Description
- This streamlit app takes a text from the user as input and analyses the sentiment behind those text.
- 'vaderSentiment‎' library is used to determine whether the text is positive or negative
- The hugging face model from [j-hartmann](https://huggingface.co/j-hartmann) called [emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) is utilised to find the emotion expressed withing the text. The model supports
  1. Anger 🤬
  2. Disgust 🤢
  3. Fear 😨
  4. Joy 😀
  5. Neutral 😐
  6. Sadness 😭
  7. Surprise 😲
- It gives the percentage of each emotion
## Checkout the project
The project has been deployed using streamlit. Checkout the [streamlit app](https://sanyam-huggingface-sentiment.streamlit.app/)
