from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_BOT_NAME = "Schizo"

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API = os.getenv("GEMINI_API")
PERSON = os.getenv("PERSON")
PERSON_BOT_ID = int(os.getenv("PERSON_BOT_ID"))