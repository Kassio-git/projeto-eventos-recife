# 📍 Recife Events Live - Extrator e Agregador Cultural

Este projeto é um protótipo funcional desenvolvido para a disciplina de [Nome da Disciplina] do MBA. A aplicação consiste em um pipeline de dados que extrai, processa e exibe eventos culturais na cidade do Recife de forma automatizada e inteligente.

## 🚀 Funcionalidades

- **Extração Real:** Consome dados em tempo real da API Google Events (SerpApi).
- **Deduplicação de Dados:** Lógica baseada em Python/Pandas que impede a inserção de eventos repetidos no banco de dados.
- **Persistência Local:** Armazenamento em CSV, funcionando como um Data Lake simplificado.
- **Interface Web Reativa:** Dashboard desenvolvido em Streamlit para visualização dos eventos e links diretos para ingressos.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas:** Manipulação e tratamento de dados.
- **Streamlit:** Interface de usuário.
- **SerpApi:** Interface de busca para Google Events.

## 🏗️ Arquitetura da Solução

O projeto segue o modelo **ETL (Extract, Transform, Load)**:

1.  **Extract:** O script `extrator_real.py` faz a chamada para a API externa.
2.  **Transform:** O Pandas realiza a limpeza e aplica a lógica de `drop_duplicates` baseada na chave composta [Nome + Local].
3.  **Load:** Os dados processados são salvos em `banco_eventos.csv`.
4.  **Visualize:** O `app.py` lê o arquivo e renderiza a interface web.



## 📋 Como Executar

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

--

Instalar Dependências
pip install -r requirements.txt

Executar o Extrator
Certifique-se de inserir sua API Key no arquivo extrator_real.py e execute:
python extrator_real.py

Iniciar a Aplicação Web
streamlit run app.py

