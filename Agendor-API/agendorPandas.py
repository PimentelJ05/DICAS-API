import requests
import pandas as pd  # aqui irei importar o pandas para colocar os dados em uma tabela

token = ""
base_url = "https://api.agendor.com.br/v3/people"
headers = {
    "Authorization": f"Token {token}"
}

per_page = 100  # numero de resultados por página
page = 1  # inicia na primeira página

all_people = []  #lista para armazenar todas as pessoas

while True: #enquato for verdade faça...
    
    response = requests.get(base_url, headers=headers, params={"page": page, "per_page": per_page}) # fazendo a requisição

    if response.status_code == 200:
        data = response.json().get("data", [])

        if not data:
            break

        all_people.extend(data)
        page += 1
        
    else:
        print(f"Erro: {response.status_code}, {response.json()}")
        break

# criando o  data frame a partir dos resultados da requisição
df = pd.DataFrame(all_people)  # convertendo o  dicionario em um DataFrame

# selecionando apenas as colunas que desejo 
df_filtered = df[['accountId', 'name']]  # filtrando as colunas desejadas

# configuração para exibir todas as colunas e linhas
pd.set_option('display.max_rows', None)  # Exibir todas as linhas
pd.set_option('display.max_columns', None)  # Exibir todas as colunas

# exibindo o data frame
print(df_filtered)
