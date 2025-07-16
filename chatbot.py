import pickle
import random
from simple_classifier import SimpleClassifier

# Load model
with open("model.pkl", "rb") as f:
    model, all_words, tags, data = pickle.load(f)

def tokenize(sentence):
    return sentence.lower().split()

def bag_of_words(sentence):
    sentence_words = tokenize(sentence)
    return [1 if word in sentence_words else 0 for word in all_words]

def get_response(user_input):
    words = tokenize(user_input)
    prediction = model.predict(words)
    
    if prediction == -1:
        return "🤖 I'm not sure how to respond to that. Please try something else."

    tag = tags[prediction]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "❓ Sorry, I couldn't understand."
