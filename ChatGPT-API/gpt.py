#instalei o pip install openai
import openai
import requests
import json  

# definindo a chave da API
api_key = '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'
# definindo a url
link = 'https://api.openai.com/v1/models'

# header para autorização, de acordo com a documentação da API
headers = {
    "Authorization": f"Bearer {api_key}"
}

# response para fazer a requisição
response = requests.get(link, headers=headers)

print (response)
print(response.text)

# definindo qual modelo será utilizado
model_id = "gpt-4o-mini"