from serpapi import GoogleSearch
import pandas as pd
import os
from datetime import datetime

def extrair_eventos_reais():
    api_key = "81bc9cb3c616192119614b3443dec5d664a906e1f4244cd713521feb42678e11"
    arquivo_db = "banco_eventos.csv"

    # 1. Configurar busca no Google Events para Recife
    params = {
        "engine": "google_events",
        "q": "eventos em recife",
        "hl": "pt",
        "gl": "br",
        "api_key": api_key
    }

    print("🔎 Acessando Google Events para buscar eventos em Recife...")
    search = GoogleSearch(params)
    results = search.get_dict()
    
    novos_eventos = []

    # 2. Processar resultados
    if "events_results" in results:
        for item in results["events_results"]:
            # O Google retorna datas em formatos variados, 
            # aqui pegamos o título, a data descritiva e o local.
            novos_eventos.append({
                "nome": item.get("title"),
                "data_texto": item.get("date", {}).get("when", "Data a confirmar"),
                "local": item.get("address", ["Recife"])[0],
                "link": item.get("link")
            })
        
        df_novos = pd.DataFrame(novos_eventos)

        # 3. Lógica de Deduplicação (Não repetir eventos)
        if os.path.exists(arquivo_db):
            df_existente = pd.read_csv(arquivo_db)
        else:
            df_existente = pd.DataFrame(columns=["nome", "data_texto", "local", "link"])

        # Unimos e removemos duplicados baseados no NOME e LOCAL
        df_final = pd.concat([df_existente, df_novos]).drop_duplicates(subset=['nome', 'local'], keep='first')
        
        # 4. Salvar
        df_final.to_csv(arquivo_db, index=False)
        print(f"✅ Sucesso! Base atualizada. Total de eventos únicos: {len(df_final)}")
        
    else:
        print("❌ Não foi possível encontrar eventos ou a cota da API acabou.")

if __name__ == "__main__":
    extrair_eventos_reais()