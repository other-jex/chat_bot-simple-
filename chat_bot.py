import random

print("Hello! I am Chatbot 🤖. Type 'quit' to exit.\n")

# Predefined responses
greetings = ["Hello! How are you?", "Hi there! 👋 How's your day going?", "Hey! Nice to see you 😄"]
goodbyes = ["Goodbye! 👋", "See you later!", "Take care! 🙌"]
feeling_good = ["I'm glad to hear that! 😊", "That's awesome! 🎉", "Great to know you're doing well! 😄"]
jokes = [
    "Why did the computer go to the doctor? Because it caught a virus! 😆",
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why was the JavaScript developer sad? Because they didn’t Node how to Express themselves. 😂"
]
fallbacks = [
    "Hmm, interesting! Tell me more 🤔",
    "Sorry, I didn't catch that. Could you rephrase?",
    "I’m still learning... can you explain that another way?",
    "Oh! That’s something I’d like to know more about!"
]

while True:
    user_input = input("You: ").lower()  # lowercase for easier matching

    if user_input == "quit":
        print("Chatbot:", random.choice(goodbyes))
        break
    elif any(word in user_input for word in ["hello", "hi", "hey", "yo"]):
        print("Chatbot:", random.choice(greetings))
    elif "how are you" in user_input:
        print("Chatbot: I'm just a bot, but I'm doing great! 😄")
    elif "i am good" in user_input or "i'm fine" in user_input or "i feel great" in user_input:
        print("Chatbot:", random.choice(feeling_good))
    elif "joke" in user_input:
        print("Chatbot:", random.choice(jokes))
    elif "bye" in user_input:
        print("Chatbot:", random.choice(goodbyes))
        break
    else:
        print("Chatbot:", random.choice(fallbacks))
