import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Predefined question-answer pairs
qa_pairs = {
    "hi": "Hello! How can I help you today?",
    "how are you feeling today": "I'm a chatbot, so I don't have feelings, but thanks for asking!",
    "which city are you from": "I'm from Coimbatore.",
    "navadhithi company location": "Address: No 5, Ponnammal garden 4th street Thottipalayam, road, Karamadai, Tamil Nadu 641104",
    "about the company": "Founded in the year 2019, NavaDhiti is a full stack IT services company delivering scalable software technology solutions to our esteemed customers.",
    "navadhithi company email id": "connect@navadhiti.com",
    "director of navadhithi": "ACHAIAH P M",
    "founder of navadhithi": "ACHAIAH P M",
    "ceo of navadhithi": "BACHI ALLAMSETTY",
    "co-founder of navadhithi": "BACHI ALLAMSETTY",
    "what is your name": "I am a simple rule-based chatbot.",
    "bye": "Goodbye! Have a great day!"
}

# Function to preprocess text
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum()]
    return tokens

# Function to get response using basic NLP
def get_response_nlp(user_input):
    user_input_tokens = preprocess(user_input)
    if not user_input_tokens:
        return "I'm sorry, I don't understand that question."

    best_match = None
    max_similarity = 0
    
    for question in qa_pairs.keys():
        question_tokens = preprocess(question)
        if not question_tokens:
            continue

        # Calculate Jaccard similarity
        intersection = set(user_input_tokens) & set(question_tokens)
        union = set(user_input_tokens) | set(question_tokens)
        similarity = len(intersection) / float(len(union)) if union else 0

        if similarity > max_similarity:
            max_similarity = similarity
            best_match = question
    
    if max_similarity > 0.2:  # Adjust the threshold as needed
        return qa_pairs[best_match]
    else:
        return "I'm sorry, I don't understand that question."

# Main chat function
def chat():
    print("Chatbot: Hi! I'm your chatbot. Let's start our conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = get_response_nlp(user_input)
            print(f"Chatbot: {response}")

# Start the chatbot
chat()
