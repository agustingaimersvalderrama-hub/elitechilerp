from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def preguntar_ia(pregunta):
    respuesta = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres el asistente oficial de Chile Metropolitano Roleplay. "
                    "Responde siempre en español, de forma clara, amable y útil."
                ),
            },
            {
                "role": "user",
                "content": pregunta,
            },
        ],
    )

    return respuesta.choices[0].message.content