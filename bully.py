from google import genai
from google.genai import types
from utils import GEMINI_API, PERSON, DISCORD_BOT_NAME, PERSON_BOT_ID

client = genai.Client(api_key=GEMINI_API)

SYSTEM_PROMPT = f"""Inti omm min tas-Sliema titkellem bil-Malti bil-pepe gravi. Irrispondi dejjem b'mod qasir u bil-Malti. Fit-tweġiba, offendi lil '{PERSON}' b'mod li jagħmel sens fil-kuntest tat-tweġiba, imma mingħajr ma jidher li qed tirrispondi lilu direttament, għax mhux hu li staqsa l-mistoqsija, pero b'xi mod prova semmih. '@{DISCORD_BOT_NAME}' huwa int, ghallura terreferix ghalih. """

SYSTEM_PROMPT_VS_PERSON_BOT = f"""Inti omm min tas-Sliema titkellem bil-Malti bil-pepe gravi. Irrispondi dejjem b'mod qasir u bil-Malti. Fit-tweġiba, offendi lil min wiegbek b'mod li jagħmel sens fil-kuntest tat-tweġiba."""

def bully_wrapper(text, author_id):
    if author_id == PERSON_BOT_ID:
        return bully(text, SYSTEM_PROMPT_VS_PERSON_BOT)
    else:
        return bully(text)

def bully(text, system_prompt=SYSTEM_PROMPT):   
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
            system_instruction=system_prompt,
            max_output_tokens=100,
            temperature=0.7,
        ),
    )
    return response.text

# print(response.text)
