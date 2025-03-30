import nltk

#nltk.download('punkt')

FAQ_QUESTIONS = {
    "what is this product?": "The AI Robot is a smart, interactive device designed to assist with tasks like home automation, personal assistance, entertainment, and education.",
    "who is this product for?": "This product is ideal for tech enthusiasts, busy professionals, families looking for smart home solutions, and anyone interested in AI and robotics.",
    "what are the key features of this product?": "Key features include voice recognition, facial recognition, autonomous navigation, home automation integration, and the ability to learn and adapt to user preferences.",
    "what are the business hours": "Our business hours are from 9 AM to 6 PM, Monday to Friday.",
    "what is the return policy": "We accept returns within 30 days of purchase with a valid receipt.",
    "is there any international shipping": "Yes, we offer international shipping to select countries.",
    "contact customer support": "You can contact our customer support at airtechsupport@gmail.com.",
    "what is the company location": "We are located in Visakhapatnam, India."
}


def chat_response(user_in):
    user_in = user_in.lower()

    for keyword, answer in FAQ_QUESTIONS.items():
        if keyword in user_in:  # Check if the keyword is part of the input
            return answer

    return "I'm sorry, I didn't understand that. Can you please rephrase?"


print("Chatbot: Hello! Ask me anything about our services.")
while True:
    user_in = input("You: ").strip()

    if not user_in:
        print("Chatbot: Please type something!")
        continue

    if user_in.lower() in ["exit", "bye", "quit"]:
        print("Chatbot: Goodbye!")
        break

    response = chat_response(user_in)
    print(f"Chatbot: {response}")
