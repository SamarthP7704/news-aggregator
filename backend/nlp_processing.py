import re
from nltk.corpus import stopwords
from collections import Counter
import string

# Ensure 'stopwords' is downloaded
import nltk
nltk.download('stopwords')

def basic_sentence_tokenizer(text):
    # Split text into sentences using periods, question marks, and exclamation marks
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

def summarize_article(text, num_sentences=2):
    sentences = basic_sentence_tokenizer(text)
    
    if len(sentences) <= num_sentences:
        return text  # If the text is too short, return as is

    words = re.findall(r'\w+', text.lower())  # Tokenizing words by extracting alphanumeric characters
    stop_words = set(stopwords.words('english') + list(string.punctuation))

    filtered_words = [word for word in words if word not in stop_words]
    word_frequencies = Counter(filtered_words)

    sentence_scores = {}
    for sentence in sentences:
        sentence_words = re.findall(r'\w+', sentence.lower())
        sentence_scores[sentence] = sum(word_frequencies.get(word, 0) for word in sentence_words)

    # Sort the sentences by their score and return the top `num_sentences`
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:num_sentences])
    return summary

def categorize_article(text):
    # Basic categorization logic
    if 'AI' in text or 'Artificial Intelligence' in text:
        return 'AI/Tech'
    elif 'Politics' in text:
        return 'Politics'
    elif 'Science' in text:
        return 'Science'
    else:
        return 'General'
