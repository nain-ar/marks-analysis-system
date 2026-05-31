# message = input("You: ")
# print("Bot:", message)
while True:
    message = input("You: ")

    if message == "bye":
        print("Bot: Goodbye!")
        break

    elif message == "hi":
        print("Bot: Hello!")

    else:
        print("Bot: I don't understand")