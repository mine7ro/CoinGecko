import requests
import json
import os
from datetime import datetime

#URL PRA EXTRAÇÃO DE DADOS 
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1"


params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1
}

#GET
response = requests.get(url, params=params)

#VERIFICA SE ESTÁ TUDO OK
if response.status_code == 200:
    data = response.json()
    for coin in data[:10]:
        print(coin["id"], coin["current_price"])

else: 
    print("Erro", response.status_code, response.text)

#AQUI EU GERO O TIMESTAMP
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

#AQUI ADCIONO O NOME DO ARQUIVO E EM QUAL PASTA
filename = f"data_lake/raw/coins_{timestamp}.json"


#SALVANDO ARQUIVO
with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Arquivo salvo em: {filename}")