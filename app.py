import streamlit as st  
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def convert_to_df(sentiment):
    sentiment_dict = {'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df

def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']
        if res > 0.1:
            pos_list.append(f"{i} (score: {res})")
        elif res <= -0.1:
            neg_list.append(f"{i} (score: {res})")
        else:
            neu_list.append(f"{i} (score: {res})")

    result = {'positives': pos_list, 'negatives': neg_list, 'neutral': neu_list}
    return result 

def main():
    st.title("Sentiment Analysis NLP App")
    st.subheader("Streamlit Projects")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        with st.form(key='nlpForm'):
            raw_text = st.text_area("Enter Text Here")
            submit_button = st.form_submit_button(label='Analyze')

        col1, col2 = st.columns(2)
        if submit_button:

            if not raw_text:
                st.warning("Please enter some text to analyze.")
            else:
                with col1:
                    st.info("Results")
                    sentiment = TextBlob(raw_text).sentiment
                    st.write(sentiment)

                    if sentiment.polarity > 0.1:
                        st.markdown("Sentiment:: Positive :smiley: ")
                    elif sentiment.polarity < -0.1:
                        st.markdown("Sentiment:: Negative :angry: ")
                    else:
                        st.markdown("Sentiment:: Neutral 😐 ")

                    result_df = convert_to_df(sentiment)
                    st.dataframe(result_df)

                    c = alt.Chart(result_df).mark_bar().encode(
                        x='metric',
                        y='value',
                        color='metric')
                    st.altair_chart(c, use_container_width=True)

                with col2:
                    st.info("Token Sentiment")
                    token_sentiments = analyze_token_sentiment(raw_text)
                    st.write(token_sentiments)

    else:
        st.subheader("About")
        st.write("This is a simple NLP app for sentiment analysis using TextBlob and VaderSentiment.")
        st.write("Enter text in the 'Home' section to analyze its sentiment.")

if __name__ == '__main__':
    main()
