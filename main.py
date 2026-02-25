import requests
import json
from dotenv import load_dotenv
import os
from utils import AIAssistant
import logging
from pydantic import ValidationError


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler(f"logs/{__name__}.log", "w")
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    AI_MODEL = os.getenv("AI_MODEL")
    logger.debug("Loading virtual environment varibles ends successfully")
 
    try:
     AI_Assistant = AIAssistant(
        api_key=API_KEY,
        ai_model=AI_MODEL,
        last_session_request="средний размер полового члена мужчины",
        reasoning=True
        )
    except ValidationError as err:
       logger.exception("Error during creating AI_Assistant: ")
    
    response = AI_Assistant.request()
    with open("p.md", "w", encoding="utf-8") as file:
        print(response, file=file)
 
    AI_Assistant.last_session_request = "напиши \"уверен\" если ты уверен в ответе на прошлый вопрос"
    response = AI_Assistant.request()
    with open("p.md", "a", encoding="utf-8") as file:
        print(file=file)
        print(file=file)
        print(file=file)
        print(response, file=file)
        
 
if __name__ == "__main__":
  main()
