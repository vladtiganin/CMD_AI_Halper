from pydantic import BaseModel, Field,model_validator 
import requests
import json
from typing import Optional, TypedDict, Literal, List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f"logs/{__name__}.log", "w")
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)


class ValidDict(TypedDict):
    role: Literal["user", "assistant"]
    content: str
    reasoning_details: str


class AIAssistant(BaseModel):
    api_key: str = Field(min_length=0)
    ai_model: str = Field(min_length=0)
    last_session_request: str
    reasoning: bool 
    session_history: Optional[list[ValidDict]] = None


    @model_validator(mode='after')
    def define_session_history(self) -> None:
        if self.session_history is None:
            logger.debug("Session history empty, create new")
            self.session_history = []

        logger.debug("Add last user\'s request to session history")
        self.session_history.append({
            "role" : "user",
            "content" : self.last_session_request   
        })

        return self 
            

    def request(self):
        self.session_history.append({
            "role" : "user",
            "content" : self.last_session_request   
        })

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization" : self.api_key,
                    "Content-Type" : "application/json" 
                },
                data=json.dumps({
                    "model" : self.ai_model,
                    "messages": self.session_history,
                    "reasoning" : {"enabled" : self.reasoning} 
                })
            )
        except requests.HTTPError as err:
            logger.exception(f"Somthig goes wrong during HTTP request: ")
            return

        self.session_history.append({
            "role": "assistant",
            "content": response.json()["choices"][0]["message"]["content"],
            "reasoning_details": response.json()["choices"][0]["message"]['reasoning_details'] 
        })

        logger.info(f"Response status code: {response.status_code}")

        return response.json()["choices"][0]["message"]["content"]

