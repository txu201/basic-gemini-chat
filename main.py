# Install in your venv:
# pip install google-genai

import os
from google import genai

# 1. Configure environment
API_KEY = os.getenv("GOOGLE_API_KEY", "")
client = genai.Client(
    vertexai=False,           # Developer API, not Vertex AI
    api_key=API_KEY
)

# 2. Choose model
MODEL = "gemini-2.5-flash"   # or "gemini-2.5-pro"

# 3. Send a prompt
response = client.models.generate_content(
    model=MODEL,
    contents="Hello Gemini! Explain quantum computing in simple terms.",
    # Optional structured output, multimodal input, thinking budget, etc.
)

print(response.text)
