import requests
import pandas as pd

def testar_extracao():
    # URL oficial de eventos culturais - Dados Abertos Recife
    url = "http://dados.recife.pe.gov.br/api/3/action/datastore_search?resource_id=98716301-4934-406d-bc67-0cc6967f6262"
    
    # Adicionamos um 'header' para parecer que é um navegador acessando
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print("Tentando conectar com a API da Prefeitura do Recife...")
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        # Se o status for 200, deu certo
        if response.status_code == 200:
            dados = response.json()
            eventos = dados['result']['records']
            
            if not eventos:
                print("Conectou, mas a lista de eventos veio vazia.")
                return

            df = pd.DataFrame(eventos)
            df.to_csv("banco_eventos.csv", index=False)
            print(f"✅ Sucesso! {len(df)} eventos encontrados.")
            print("O arquivo 'banco_eventos.csv' foi gerado.")
        else:
            print(f"❌ Erro HTTP: {response.status_code}")
            print("O servidor da prefeitura pode estar fora do ar temporariamente.")

    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    testar_extracao()