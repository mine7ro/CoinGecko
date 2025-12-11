# 📊 Crypto Analytics - Pipeline de Dados End-to-End

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)
![Status](https://img.shields.io/badge/Status-Concluído-green.svg)

## 📌 Sobre o Projeto

Pipeline completo de análise de dados de criptomoedas, desde a extração via API até visualização em dashboard interativo. O projeto implementa conceitos de Data Lake, ETL e Business Intelligence.

## 🎯 Objetivo

Criar um sistema automatizado de coleta, processamento e visualização de dados do mercado de criptomoedas em tempo real, aplicando boas práticas de engenharia de dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**: Linguagem principal
- **Pandas**: Manipulação e transformação de dados
- **Requests**: Consumo de API REST
- **CoinGecko API**: Fonte de dados
- **Power BI**: Visualização e dashboards
- **Git/GitHub**: Versionamento de código

## 📁 Estrutura do Projeto
```
projeto_crypto_analytics/
│
├── data_lake/
│   ├── raw/              # Dados brutos da API (JSON)
│   ├── processed/        # Dados processados (CSV)
│   └── historical/       # Consolidado histórico
│
├── scripts/
│   ├── extract.py        # Extração dos dados
│   └── transform.py      # Transformação e limpeza
│
├── powerbi/
│   └── dashboard.pbix    # Dashboard Power BI
│
└── requirements.txt      # Dependências
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.9 ou superior
- Power BI Desktop

### Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/crypto-analytics.git
cd crypto-analytics
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

### Execução

1. **Extrair dados da API:**
```bash
python scripts/extract.py
```

2. **Processar e transformar:**
```bash
python scripts/transform.py
```

3. **Visualizar no Power BI:**
- Abra o arquivo `powerbi/dashboard.pbix`
- Clique em "Atualizar" para carregar os dados mais recentes

## 📊 Dashboard

O dashboard apresenta:
- ✅ KPIs principais (Total de moedas, Market Cap, Variação média)
- ✅ Ranking Top 10 criptomoedas por capitalização
- ✅ Análise de variação de preços 24h
- ✅ Evolução temporal dos preços
- ✅ Distribuição de market share

<img width="1366" height="768" alt="dashboard_crypto" src="https://github.com/user-attachments/assets/c6ed551b-fa3c-42e7-9d83-4e634dcf0c65" />


## 🏗️ Arquitetura de Dados

**Camadas do Data Lake:**
- **Raw (Bronze)**: Dados brutos sem transformação
- **Processed (Silver)**: Dados limpos e estruturados
- **Historical (Gold)**: Dados consolidados para análise

**Pipeline ETL:**
1. **Extract**: Coleta via API CoinGecko
2. **Transform**: Limpeza, tipagem e enriquecimento
3. **Load**: Consolidação e persistência

## 📈 Próximos Passos

- [ ] Automatização com schedulers (Airflow/cron)
- [ ] Adicionar mais fontes de dados
- [ ] Implementar alertas de variação de preço
- [ ] Deploy do dashboard online (Power BI Service)
- [ ] Adicionar testes unitários

## 👨‍💻 Autor

**[Renan Queiroz]**
- LinkedIn: [(https://www.linkedin.com/in/renan-queiroz-datascience/)]
- GitHub: [(https://github.com/mine7ro)]
- Email: renanpessoal2023@gmail.com

## 📝 Licença

Este projeto está sob a licença MIT.
```

---

### **2. Arquivo .gitignore**

Crie um arquivo `.gitignore` pra não subir coisas desnecessárias:
```
# Ambientes virtuais
venv/
env/

# Dados (opcional - você decide se quer subir os dados ou não)
data_lake/raw/*.json
data_lake/processed/*.csv
data_lake/historical/*.csv

# Python
__pycache__/
*.py[cod]
*.so
.Python

# Logs
logs/
*.log

# Power BI temporários
*.pbix.tmp

# IDE
.vscode/
.idea/

# Sistema
.DS_Store
Thumbs.db
