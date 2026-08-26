from openai import OpenAI

client = OpenAI()

prompt = input("Enter prompt: ")

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("Generated Text:")
print(response.output_text)