# IN PROGRESS 

# Depois de fazer a primeira requisição e definir qual modelo irei usar, vamos fazer novas requisições
import openai
import requests
import json  

api_key = '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'
link = 'https://api.openai.com/v1/chat/completions'
model_id = "gpt-4o-mini"

# criando o corpo da requisição, e dentro dela fazemos uma lista com o modelo e a mensagem
message_body = {
    "model": model_id,
    "messages": [{"role": "user", "content": "Qual é a capital do Brasil?"}]
}

headers = {
    "Authorization": f"Bearer {api_key}"
}

# nova requisição com o metodo POST
response = requests.post(link, headers=headers)