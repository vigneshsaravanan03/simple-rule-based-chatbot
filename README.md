# Simple-Rule-Based-Chatbot 


This repository contains a simple rule-based chatbot implemented in Python. The chatbot responds to user queries with predefined answers and handles questions effectively using basic Natural Language Processing (NLP) techniques.

## Features

- Predefined question-answer pairs.
- Basic NLP using NLTK for tokenization, stopwords removal, and lemmatization.
- Handles multiple questions mapping to the same answer.
- Uses Jaccard similarity for matching user queries with predefined questions.

# How It Works

## Preprocessing:

1.Tokenizes the input text.

2.Removes stopwords and lemmatizes the tokens.

3.Response Generation.

## Response Generation:
1.Preprocesses the user input.

2.Calculates Jaccard similarity between user input and predefined questions.

3.Returns the answer for the question with the highest similarity if it exceeds a certain threshold.

# Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/vigneshsaravanan03/simple-rule-based-chatbot.git
    cd simple-rule-based-chatbot
    ```

2. **Install dependencies:**

    Ensure you have Python 3.7 installed. Install the required libraries using pip:

    ```bash
    pip install nltk
    ```

3. **Download NLTK data:**

    Run the following script to download the necessary NLTK data:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Usage

1. **Run the chatbot:**

    Execute the `main.py` script:

    ```bash
    python main.py
    ```

2. **Interact with the chatbot:**

    The chatbot will start a conversation. You can ask predefined questions or say `bye` to end the chat. For example:

    ```
    You: hi
    Chatbot: Hello! How can I help you today?
    ```




