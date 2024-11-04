import requests

token = "1292a8bf-d7d2-4175-b1f1-27e3a1204b8c"
base_url = "https://api.agendor.com.br/v3/people"
headers = {
    "Authorization": f"Token {token}"
}

per_page = 100  # Número de resultados por página (máximo permitido)
page = 1  # Começa a partir da primeira página

all_people = []  # Lista para armazenar todas as pessoas

while True:  # Loop infinito que irá parar quando não houver mais resultados
    
    response = requests.get(base_url, headers=headers, params={"page": page, "per_page": per_page})

    if response.status_code == 200:
        data = response.json().get("data", [])  # Obtém a lista de pessoas

        if not data:  # Se não houver mais pessoas na lista, sai do loop
            break

        all_people.extend(data)  # Adiciona as pessoas obtidas à lista total
        page += 1  # Passa para a próxima página
    else:
        print(f"Erro: {response.status_code}, {response.json()}")  # Exibe erro em caso de falha
        break  # Para o loop em caso de erro

# Após o loop, todas as pessoas estão na lista all_people
for person in all_people:  # Itera sobre todas as pessoas obtidas
    account_id = person.get("accountId")  # Obtém o ID da conta
    name = person.get("name")  # Obtém o nome da pessoa
    print(f"Name: {name}, Account ID: {account_id}")  # Imprime o nome e o ID da conta
