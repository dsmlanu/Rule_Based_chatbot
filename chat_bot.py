import json
import random

# Load intents
with open('intents.json') as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input:
                return random.choice(intent['responses'])

    return "Sorry, I didn’t understand that."

def chat():
    print("BankBot: Hello! How can I help you? (Type 'quit' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("BankBot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"BankBot: {response}")

if __name__ == "__main__":
    chat()
