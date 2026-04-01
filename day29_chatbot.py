# Day 29 - Simple Chatbot

print("=== Simple Chatbot ===")
print("Type 'exit' to end the chat\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hello Om! 👋")

    elif user_input == "how are you":
        print("Bot: I am good, always here to help you ❤️")

    elif user_input == "your name":
        print("Bot: I am your AI assistant 🤖")

    elif user_input == "bye":
        print("Bot: Goodbye Om! Keep coding 💪")
        break

    elif user_input == "exit":
        print("Bot: Chat ended.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
