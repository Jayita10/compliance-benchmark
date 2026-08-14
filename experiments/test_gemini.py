from google import genai
import os

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Reply with exactly: Gemini connection works."
)

print(response.text)