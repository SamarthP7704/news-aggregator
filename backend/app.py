from flask import Flask, jsonify
from scraper import scrape_hackernews  # Import the correct scraping function
from nlp_processing import categorize_article, summarize_article  # Import NLP functions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/')
def home():
    return "Welcome to the AI-Powered News Aggregator API! Visit /api/news for the news."

@app.route('/api/news', methods=['GET'])
def get_news():
    news = scrape_hackernews()  # Fetch the news articles using the Hacker News scraper
    if not news:
        return jsonify([])  # Return an empty list if no news is found

    # Optional: Add NLP processing for categories and summaries (if you have implemented these)
    for article in news:
        article['category'] = categorize_article(article['summary'])  # Placeholder for category function
        article['summary'] = summarize_article(article['summary'])  # Placeholder for summary function

    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)
