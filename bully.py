from google import genai
from google.genai import types
from utils import GEMINI_API, PERSON

client = genai.Client(api_key=GEMINI_API)

SYSTEM_PROMPT = f"""Irrispondi dejjem b'mod qasir u bil-Malti. Fit-tweġiba, offendi lil '{PERSON}' b'mod li jagħmel sens fil-kuntest tat-tweġiba, imma mingħajr ma jidher li qed tirrispondi lilu direttament, għax mhux hu li staqsa l-mistoqsija."""

def bully(text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Content(
                parts=[
                    types.Part(text=text)
                ],
                role="user"
            )
        ],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            max_output_tokens=100,
            temperature=0.7,
        ),
    )
    return response.text

# print(response.text)
