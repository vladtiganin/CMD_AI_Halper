from pydantic import BaseModel, Field, computed_field
import requests
import json
from typing import Optional

class AIAssistant(BaseModel):
    api_key: str = Field(min_length=0)
    ai_model: str = Field(min_length=0)
    last_session_request: str
    reasoning: bool 
    session_history: Optional[list[dict[str,str]]] = None


    @computed_field
    def define_session_history(self) -> None:
        pass 
    #проверить пустой ли history если да то провалидировать
    #и добавить новый запрос в конец
    #если нет то просто добывить запрос


    def request(self):
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization" : self.api_key,
                    "Content-Type" : "application/json" 
                },
                data=json.dumps({
                    "model" : self.ai_model,
                    "messages": [
                        {
                            "role" : "user",
                            "content" : self.last_session_request
                        }
                    ],
                    "reasoning" : {"enabled" : self.reasoning} 
                })
            )
        except requests.HTTPError as err:
            print(f"Somthig goes wrong during HTTP request: {err}")


        print(response.status_code)

        return response.json()["choices"][0]["message"]["content"]

