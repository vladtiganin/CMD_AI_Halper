import requests
import json
from dotenv import load_dotenv
import os
from utils import AIAssistant


def main():
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    AI_MODEL = os.getenv("AI_MODEL")

    AI_Assistant = AIAssistant(
       api_key=API_KEY,
       ai_model=AI_MODEL,
       user_request="сколько букв а в слове мама",
       reasoning=True
       )

    response = AI_Assistant.request()
    with open("p.md", "w", encoding="utf-8") as file:
       print(response, file=file)


if __name__ == "__main__":
  main()
