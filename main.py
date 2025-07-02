import os
from dotenv import load_dotenv
from google import genai  # Use this import

load_dotenv()
# Make sure GOOGLE_API_KEY is set in your environment or .env
# i.e., export GOOGLE_API_KEY=your_key_here

# Use the default client (reads API key automatically)
client = genai.Client()

# ✅ Generate content using developer API mode
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me a fun fact about the moon."
)
print(response.text)
