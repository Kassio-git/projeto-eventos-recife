import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Agenda Cultural Recife", layout="centered", page_icon="📍")

st.title("📍 Eventos Culturais - Recife")
st.markdown("Protótipo de busca de eventos reais extraídos via API.")

# 1. Função para carregar os dados
def carregar_dados():
    try:
        df = pd.read_csv("banco_eventos.csv")
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# 2. Processamento dos Dados
df = carregar_dados()

if not df.empty:
    st.subheader("Eventos Encontrados em Recife")
    
    for index, row in df.iterrows():
        # Lógica para evitar o KeyError: tenta pegar 'data_texto', se não existir tenta 'data'
        data_exibicao = row.get('data_texto') or row.get('data') or "Data a confirmar"
        nome_evento = row.get('nome', 'Evento sem nome')
        local_evento = row.get('local', 'Local não informado')
        link_evento = row.get('link')

        with st.container():
            col1, col2 = st.columns([1, 4])
            
            with col1:
                st.markdown(f"🗓️ **{data_exibicao}**")
            
            with col2:
                st.write(f"### {nome_evento}")
                st.caption(f"📍 **Local:** {local_evento}")
                
                if pd.notna(link_evento):
                    st.link_button("Ver Detalhes", link_evento)
            
            st.divider()
else:
    st.info("O banco de dados está vazio. Por favor, execute o extrator para buscar eventos.")

# --- Barra Lateral ---
st.sidebar.header("Painel de Controle")
if st.sidebar.button("Executar Extração (API)"):
    st.sidebar.info("Rode o comando 'python extrator_real.py' no terminal para atualizar os dados reais.")