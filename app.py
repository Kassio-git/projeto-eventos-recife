import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Agenda Cultural Recife", layout="centered")

st.title("📍 Eventos Culturais - Recife")
st.markdown("Protótipo de busca de eventos para o próximo mês.")

# 1. Função para carregar os dados
def carregar_dados():
    try:
        df = pd.read_csv("banco_eventos.csv")
        # Converte a coluna de data para o formato de data do Python
        df['data'] = pd.to_datetime(df['data'])
        return df
    except FileNotFoundError:
        st.error("O banco de dados ainda não foi criado. Rode o extrator primeiro!")
        return pd.DataFrame()

# 2. Filtragem de Datas (Regra de Negócio)
df = carregar_dados()

if not df.empty:
    hoje = datetime.now()
    mes_que_vem = hoje + timedelta(days=30)

    # Filtrar eventos entre hoje e daqui a 30 dias
    eventos_filtrados = df[(df['data'] >= hoje) & (df['data'] <= mes_que_vem)]
    eventos_filtrados = eventos_filtrados.sort_values(by='data')

    # Interface
    st.subheader(f"Exibindo eventos até {mes_que_vem.strftime('%d/%m/%Y')}")
    
    if eventos_filtrados.empty:
        st.info("Nenhum evento encontrado para os próximos 30 dias.")
    else:
        for index, row in eventos_filtrados.iterrows():
            with st.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.metric("Data", row['data'].strftime('%d/%b'))
                with col2:
                    st.write(f"### {row['nome']}")
                    st.caption(f"📍 Local: {row['local']}")
                st.divider()

# Rodapé lateral para o seu projeto
st.sidebar.header("Configurações do Extrator")
if st.sidebar.button("Rodar Extrator Agora"):
    # Aqui você poderia chamar a função do seu extrator_mock.py
    st.sidebar.success("Dados atualizados com sucesso!")