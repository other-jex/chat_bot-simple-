import random
print("Hello! I am Chatbot. Type 'quit' to exit.\n")


while True:
    user_input = input("You: ")

    if user_input == "quit":
        print("Chatbot: Goodbye! 👋")
        break
    elif user_input == "Hello" or user_input == "hi" or user_input == "hey" or user_input == "yo":
        print("Chatbot: Hello! How are you?")
    elif "I am good" in user_input:
        print("Chatbot: I am glad to hear that!!")
    elif "How are you" in user_input:
        print("Chatbot: I'm just a bot, but I'm doing great! 😄")
    elif "joke" in user_input:
        joke = ["Why did the computer go to the doctor? Because it caught a virus! 😆",
             "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"]
        print("Chatbot: ", random.choice(joke))
    else:
        print("Chatbot: Sorry, I don't understand that.")