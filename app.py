from flask import Flask, render_template, request, jsonify
from newspaper import Article
import google.generativeai as genai
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

# Retrieve the API key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the Generative AI SDK with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Create a GenerativeModel object using 'gemini-pro' model
model = genai.GenerativeModel('gemini-pro')

def fetch_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    
    return article.text, article.top_image

def summarize_text(text):
    summary = text[:400]
    if len(summary) < len(text):
        last_period = summary.rfind('. ')
        if last_period != -1:
            summary = summary[:last_period + 1]
    return summary

def clean_text(text):
    cleaned_text = text.replace('*', '')
    return cleaned_text

def divide_paragraphs(text):
    paragraphs = text.split('\n\n')
    return paragraphs

def generate_response(summary):
    try:
        response = model.generate_content(summary)
        if response and response.text:
            cleaned_response = clean_text(response.text)
            paragraphs = divide_paragraphs(cleaned_response)
            combined_summary = ' '.join(paragraphs[:2])
            return combined_summary
        else:
            return "No valid response generated."
    except ValueError as ve:
        return f"ValueError: {str(ve)}"
    except Exception as e:
        return f"Error generating response: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    article_text, article_image = fetch_article_content(url)
    summary = summarize_text(article_text)
    response = generate_response(summary)
    return jsonify({'summary': summary, 'response': response, 'image': article_image, 'url': url})

if __name__ == '__main__':
    app.run(debug=True)
