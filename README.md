# Article Summarizer

## Overview

The Article Summarizer is a web application that summarizes articles from URLs provided by users. It uses the Newspaper library to extract the article content and Google's Generative AI for summarization. Additionally, it fetches the main image from the article and displays it along with the summary.

## Features

- **Summarization**: Generates a concise summary of the article content.
- **Image Extraction**: Fetches the main image from the article and displays it.
- **Responsive Design**: User-friendly interface with a gradient background.

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Summarization**: Google Generative AI
- **Article Extraction**: Newspaper3k
- **Environment Management**: Python Virtual Environment (`venv`)
- **Styling**: CSS with gradient backgrounds

## Installation

### Prerequisites

- Python 3.12 or higher
- Pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/nanichey7/Article-summarizer.git
cd article-summarizer
```

### Create and Activate a Virtual Environment

```
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a .env file in the root directory and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key
```
![image](https://github.com/user-attachments/assets/86ed7f53-ddd4-4523-8dbd-94187edd08c1)


### Run the Application

```
python app.py
```
