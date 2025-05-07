from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
model = "gemini-1.5-flash-002"
client = genai.Client(api_key=os.getenv("API_KEY"))



def create_cache(filepath):
    # Create a cache
    system_instruction = "You are an expert at analyzing documents."

    document = client.files.upload(
        file=filepath
    )

    cache = client.caches.create(
        model=model,
        config=types.CreateCachedContentConfig(
            system_instruction=system_instruction,
            contents=[document],
        )
    )
    return cache

def output(cache, text):
    response = client.models.generate_content(
        model=model, contents=text,
        config=types.GenerateContentConfig(
            cached_content=cache.name
        ))
    return response.text