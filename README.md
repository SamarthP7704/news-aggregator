# AI-Powered News Aggregator

![News Aggregator](https://link-to-your-image.com)

## Overview

AI-Powered News Aggregator is a web application that collects and categorizes news articles from various sources using web scraping and Natural Language Processing (NLP). The project consists of two parts: a **frontend** built with React and a **backend** built with Flask and Python, utilizing the BeautifulSoup library for web scraping and NLTK for NLP tasks.

### Features:
- Fetches and displays news articles from websites like BBC and Hacker News.
- Categorizes news articles automatically using NLP.
- Provides summaries of articles based on content analysis.
- Responsive and user-friendly interface built with React.

---

## Demo

You can view a live demo of the project [here](https://your-live-demo-url.com).

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [File Structure](#file-structure)
4. [Technologies Used](#technologies-used)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

---

## Installation

### Prerequisites
- **Node.js** and **npm** installed for the frontend.
- **Python 3.x** installed for the backend.
- A virtual environment for Python is recommended.

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/news-aggregator.git
    cd news-aggregator/backend
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask backend:
    ```bash
    python app.py
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install Node dependencies:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

### Running the Full Application

Once both the backend and frontend are running, the web app will be available at:

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5000`

---

## Usage

- Visit the homepage of the app (Frontend running on `localhost:3000`).
- The page will display news articles collected from various sources.
- Articles are categorized automatically using NLP techniques.
- You can view a summary and more details of each article.

---

---

## Technologies Used

### Backend:
- **Python 3.x**: For building the backend server.
- **Flask**: Lightweight web framework.
- **BeautifulSoup**: For web scraping news articles.
- **NLTK**: For natural language processing (NLP).
- **Sumy**: For text summarization.

### Frontend:
- **React**: JavaScript library for building user interfaces.
- **Axios**: For making HTTP requests to the backend API.

---

## API Endpoints

### `GET /api/news`
Fetches the latest news articles from various sources and categorizes them.

- **Response Format:**
    ```json
    [
        {
            "category": "General",
            "headline": "Example News Title",
            "link": "https://example.com",
            "summary": "Brief summary of the article"
        },
        ...
    ]
    ```

---

## Contributing

Contributions are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m "Added new feature"`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

If you have any questions or feedback, feel free to reach out!

