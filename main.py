import requests
import json
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    
    API_KEY = os.getenv("API_KEY")

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": API_KEY,
      "Content-Type": "application/json",
    },
    data=json.dumps({
      "model": "nvidia/nemotron-3-nano-30b-a3b:free",
      "messages": [
          {
            "role": "user",
            "content": "Нормальный размер полового члена"
          }
        ],
      "reasoning": {"enabled": True}
    })
    )

    print(response.status_code)
  
    res = response
    response = response.json()
    response = response['choices'][0]['message']

    with open("p.md", "w", encoding="utf-8") as file:
        print("===================================================================================================================================================", file=file)
        print(response["content"], file=file)
        print(response["reasoning_details"], file=file)
        print("===================================================================================================================================================\n\n\n\n\n", file=file)
    

#     messages = [
#     {"role": "user", "content": "отгадай загадку : В Полотняной стране По реке Простыне Плывет пароход То назад, то вперед, А за ним такая гладь — Ни морщинки не видать."},
#     {
#       "role": "assistant",
#       "content": response["content"],
#       "reasoning_details": response['reasoning_details'] 
#     },
#     {"role": "user", "content": "Уверен? Подумай ещё?"}
#     ]
    
#     with open("p.txt", "w", encoding="utf-8") as file:
#         unswer = res.json()['choices'][0]['message']['content']
#         lines = unswer.split(".")
#         for line in lines:
#            print(line, file=file)
#         print(json.dumps(res.json()['choices'][0]['message']['content'], indent=4, ensure_ascii=False), file=file)
#         print("===================================================================================================================================================", file=file)


#     response2 = requests.post(
#     url="https://openrouter.ai/api/v1/chat/completions",
#     data=json.dumps({
#       "model": "nvidia/nemotron-3-nano-30b-a3b:free",
#       "messages": messages,
#       "reasoning": {"enabled": True}
#     }),
#     headers={
#       "Authorization": API_KEY,
#       # "Content-Type": "application/json",
#     }
#   )

#     with open("p.md", "a", encoding="utf-8") as file:
#         print("\n\n\n", file=file)
#         print(json.dumps(response2.json(), indent=4, ensure_ascii=False), file=file)


if __name__ == "__main__":
  main()
