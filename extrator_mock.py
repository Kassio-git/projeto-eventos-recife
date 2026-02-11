import pandas as pd
from datetime import datetime, timedelta
import os

def simular_extracao_e_limpeza():
    arquivo_db = "banco_eventos.csv"
    
    # 1. Simulando a "Extração" (Dados que o robô 'achou' hoje)
    hoje = datetime.now()
    dados_extraidos = [
        {"nome": "Festival de Frevo no Marco Zero", "data": hoje.strftime("%Y-%m-%d"), "local": "Bairro do Recife"},
        {"nome": "Oficina de Culinária Regional", "data": (hoje + timedelta(days=2)).strftime("%Y-%m-%d"), "local": "Mercado da Encruzilhada"},
        {"nome": "Show de Jazz na Jaqueira", "data": (hoje + timedelta(days=7)).strftime("%Y-%m-%d"), "local": "Parque da Jaqueira"},
        {"nome": "Teatro de Bonecos", "data": (hoje + timedelta(days=15)).strftime("%Y-%m-%d"), "local": "Teatro Santa Isabel"},
    ]
    df_novos = pd.DataFrame(dados_extraidos)

    # 2. Carregar o que já existe (Simulando a base de dados)
    if os.path.exists(arquivo_db):
        df_existente = pd.read_csv(arquivo_db)
    else:
        df_existente = pd.DataFrame(columns=["nome", "data", "local"])

    # 3. Lógica de Deduplicação (O que você precisa explicar no projeto)
    # Concatenamos os novos com os antigos e removemos o que for igual (nome + data)
    df_final = pd.concat([df_existente, df_novos]).drop_duplicates(subset=['nome', 'data'], keep='first')
    
    # 4. Salva no CSV
    df_final.to_csv(arquivo_db, index=False)
    print(f"✅ Processamento concluído. Total de eventos únicos: {len(df_final)}")

if __name__ == "__main__":
    simular_extracao_e_limpeza()