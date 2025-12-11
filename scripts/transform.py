import pandas as pd
import requests
from datetime import datetime
import json
import os

RAW_DIR = "data_lake/raw"
PROCESSED_DIR = "data_lake/processed"
HIST_DIR = "data_lake/historical"
HIST_FILE = f"{HIST_DIR}/crypto_history.csv"


#PEGAR O ARQUIVO JSON MAIS RECENTE
files = [f for f in os.listdir(RAW_DIR) if f.endswith(".json")]

if not files:
    raise FileNotFoundError("Nenhum arquivo encontrado na pasta raw.")

latestfile = sorted(files, reverse=True)[0]
full_path = os.path.join(RAW_DIR, latestfile)

print("Arquivo mais recente encontrado", full_path)

#LER O JSON
with open(full_path, "r", encoding="utf-8") as f:
    data = json.load(f)


#AQUI EU TRANSFORMO EM DATAFRAME
df = pd.DataFrame(data)

#ADCIONAR DATA E HORA DA COLETA
timestamp = (
    latestfile.replace("coins_", "").replace(".json", "").replace("_", "")
)

data_coleta = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
df["data_coleta"] = data_coleta


# Tratar valores nulos
df = df.fillna(0)

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(HIST_DIR, exist_ok=True)

#SALVAR CSV NO PROCESSED
processed_filename = os.path.join(
    PROCESSED_DIR, f"coins_processed_{timestamp}.csv"
)

df.to_csv(processed_filename, index=False, encoding="utf-8")
print(f"✔ Arquivo processado salvo em: {processed_filename}")

#SALVAR NO HISTORICAL
if not os.path.exists(HIST_FILE):
    df.to_csv(HIST_FILE, index=False, encoding="utf-8")  # cria o histórico
    print("✔ Histórico criado.")
else:
    df.to_csv(HIST_FILE, mode="a", header=False, index=False, encoding="utf-8")
    print("✔ Dados adicionados ao histórico.")

print(df.head())