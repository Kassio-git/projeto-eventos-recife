import requests
import pandas as pd

def validar_conexao_externa():
    # Uma API pública que retorna uma lista de 'posts' (simulando eventos)
    url = "https://jsonplaceholder.typicode.com/posts"
    
    print(f"🔗 Conectando a: {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            # Pegamos apenas os 5 primeiros para o teste
            df = pd.DataFrame(dados[:5])
            
            print("✅ Conexão bem sucedida!")
            print("\n--- Dados recebidos (Top 5) ---")
            print(df[['id', 'title']]) # Mostra o ID e o Título
            return True
        else:
            print(f"❌ Falha na conexão. Status Code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erro de rede: {e}")
        return False

if __name__ == "__main__":
    validar_conexao_externa()