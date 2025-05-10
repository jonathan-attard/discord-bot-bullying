from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API = os.getenv("GEMINI_API")
PERSON = os.getenv("PERSON")