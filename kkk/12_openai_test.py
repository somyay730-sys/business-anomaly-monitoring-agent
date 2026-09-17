import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("API key found:", api_key is not None)

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain what a business anomaly is in one simple sentence."
)

print("=" * 60)
print("STEP 14A: OPENAI API TEST")
print("=" * 60)

print("\nAI Response:")
print(response.output_text)

print("\nStep 14A completed successfully!")