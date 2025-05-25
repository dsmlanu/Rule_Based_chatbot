import streamlit as st
import json
import random
from fuzzywuzzy import fuzz

# Load intents
with open('intents.json') as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    max_score = 0
    best_response = "Sorry, I didn’t understand that."

    for intent in data['intents']:
        for pattern in intent['patterns']:
            score = fuzz.partial_ratio(user_input, pattern.lower())
            if score > max_score and score > 70:
                max_score = score
                best_response = random.choice(intent['responses'])

    return best_response

# Streamlit UI
st.title("🤖 BankBot – Rule-Based Chatbot")
st.write("Type your message below:")

user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.text_area("BankBot:", value=response, height=100)
