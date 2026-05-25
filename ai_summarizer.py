from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

user_text = input("Enter text to summarize:\n")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": f"Summarize this clearly:\n{user_text}"
        }
    ]
)

print("\nSummary:\n")
print(response.choices[0].message.content)