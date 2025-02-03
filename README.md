# Sentio-Sentiment-Analysis-Model


# Sentiment Analysis NLP App

## Overview
This project is a simple sentiment analysis web application built with Streamlit. It uses **TextBlob** for basic sentiment analysis (polarity and subjectivity) and **VADER Sentiment** to analyze the sentiment of individual tokens (words) in a given text.

## Features
- **TextBlob Sentiment**: Provides overall sentiment analysis (polarity and subjectivity).
- **VADER Sentiment**: Analyzes the sentiment of individual words in the text, categorizing them as positive, negative, or neutral based on their sentiment score.
- **Visualization**: Displays the sentiment data using a bar chart for a visual understanding of the sentiment analysis.

## Technologies Used
- **Streamlit**: For building the interactive web application.
- **TextBlob**: For performing overall sentiment analysis (polarity and subjectivity).
- **VADER Sentiment**: For token-level sentiment analysis.
- **Pandas**: For data manipulation and handling.
- **Altair**: For visualizing sentiment data.

## Requirements
- Python 3.x
- The following Python libraries:
  - Streamlit
  - TextBlob
  - Pandas
  - Altair
  - VaderSentiment

## Installation
To set up this project locally, follow these steps:

1. Clone the repository or download the project files.
   
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and navigate to `http://localhost:8501` to use the app.

## How to Use
1. On the "Home" page, enter a block of text into the provided text area.
2. Click "Analyze" to get the sentiment analysis results.
3. The app will display:
   - **Overall Sentiment**: A general sentiment (positive, negative, or neutral).
   - **Token Sentiment**: Sentiment analysis for each word in the input text, categorized as positive, negative, or neutral.
   - **Visualization**: A bar chart visualizing sentiment metrics (polarity and subjectivity).

## About
This app serves as a demonstration of basic NLP (Natural Language Processing) techniques for sentiment analysis. It combines different libraries like TextBlob and VADER to provide both a high-level and a token-level sentiment analysis.

## License
This project is open source and available under the MIT License.
