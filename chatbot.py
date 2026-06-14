import anthropic

MERI_API_KEY = "APNI_KEY_YAHAN_DAALO"

client = anthropic.Anthropic(api_key=MERI_API_KEY)
baatein = []

print("Chatbot ready! 'quit' likho band karne ke liye\n")

while True:
    sawaal = input("Tum: ")
    if sawaal.lower() == "quit":
        print("Alvida!")
        break
    baatein.append({"role": "user", "content": sawaal})
    jawab = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="Tum ek helpful dost ho. Hindi mein baat karo.",
        messages=baatein
    )
    reply = jawab.content[0].text
    print(f"Bot: {reply}\n")
    baatein.append({"role": "assistant", "content": reply})
