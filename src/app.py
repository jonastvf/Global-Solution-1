import streamlit as st
import requests
from datetime import datetime, timedelta
import google.generativeai as genai
import pandas as pd
import time
import os
from dotenv import load_dotenv

# ==========================================
# 1. CONFIGURAÇÕES E CHAVES DE API
# ==========================================
NASA_API_KEY = os.getenv("NASA_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# ==========================================
# 2. FRONT-END: CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="AstroDash Executivo", page_icon="🔭", layout="wide")
st.title("🔭 AstroDash - Inteligência de Risco Orbital")
st.markdown("Painel executivo para monitoramento de Objetos Próximos à Terra (NEOs) e proteção de ativos espaciais.")
st.divider()

# ==========================================
# 3. BACK-END: ETL (Extração e Transformação)
# ==========================================
hoje = datetime.today()
sete_dias_atras = hoje - timedelta(days=7)
str_hoje = hoje.strftime('%Y-%m-%d')
str_sete = sete_dias_atras.strftime('%Y-%m-%d')

@st.cache_data
def buscar_dados_nasa():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={str_sete}&end_date={str_hoje}&api_key={NASA_API_KEY}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return None

dados = buscar_dados_nasa()

if dados:
    lista_asteroides = []
    for data_aprox, neos in dados.get("near_earth_objects", {}).items():
        for neo in neos:
            lista_asteroides.append({
                "Data": data_aprox,
                "Nome": neo["name"],
                "Diâmetro Máx (m)": round(neo["estimated_diameter"]["meters"]["estimated_diameter_max"], 2),
                "Velocidade (km/h)": round(float(neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]), 2),
                "Distância da Terra (km)": round(float(neo["close_approach_data"][0]["miss_distance"]["kilometers"]), 2),
                "Risco Potencial": "Sim" if neo["is_potentially_hazardous_asteroid"] else "Não"
            })
    
    df = pd.DataFrame(lista_asteroides)
    df["Data"] = pd.to_datetime(df["Data"]).dt.date
    df = df.sort_values(by="Data")

    # ==========================================
    # 4. DASHBOARD EXECUTIVO (Métricas e Gráficos)
    # ==========================================
    st.subheader("📊 Visão Executiva (Últimos 7 dias)")
    
    # KPIs principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Detectado", len(df))
    col2.metric("Nível de Alerta (Ameaças)", len(df[df["Risco Potencial"] == "Sim"]), delta_color="inverse")
    col3.metric("Maior Diâmetro (m)", df["Diâmetro Máx (m)"].max())
    col4.metric("Distância Mínima (km)", f"{df['Distância da Terra (km)'].min():,.0f}".replace(",", "."))

    st.write("---")

    # Gráficos de Análise
    aba1, aba2 = st.tabs(["📈 Gráficos de Análise", "🗄️ Tabela de Dados Brutos"])
    
    with aba1:
        col_graf1, col_graf2 = st.columns(2)
        
        with col_graf1:
            st.markdown("**Matriz de Risco: Distância x Velocidade**")
            st.caption("Objetos no canto inferior esquerdo merecem mais atenção.")
            # Gráfico de dispersão nativo cruzando distância, velocidade e colorindo pelo risco
            st.scatter_chart(
                df, x="Distância da Terra (km)", y="Velocidade (km/h)", color="Risco Potencial"
            )
            
        with col_graf2:
            st.markdown("**Volume de Aproximações por Dia**")
            st.caption("Sazonalidade de detecções na semana.")
            contagem_diaria = df["Data"].value_counts().sort_index()
            st.bar_chart(contagem_diaria)
            
    with aba2:
        st.markdown("**Catálogo Detalhado**")
        st.dataframe(df, use_container_width=True)

    st.divider()

    # ==========================================
    # 5. MÓDULO DE AUTOMAÇÃO E IA
    # ==========================================
    col_ia, col_alerta = st.columns(2)

    with col_ia:
        st.subheader("🧠 Relatório com IA Generativa")
        st.write("Geração de parecer técnico com base nas estatísticas atuais.")
        if st.button("Gerar Parecer Analítico", use_container_width=True):
            with st.spinner("Processando dados e consultando o Gemini..."):
                resumo_stats = f"Total: {len(df)}. Perigosos: {len(df[df['Risco Potencial'] == 'Sim'])}. Distância mínima: {df['Distância da Terra (km)'].min()} km."
                modelo = genai.GenerativeModel("gemini-2.5-flash")
                prompt = f"Aja como Head de Dados da NASA. Avalie: {resumo_stats}. Faça um resumo executivo de 1 parágrafo avaliando riscos para satélites."
                resposta_ia = modelo.generate_content(prompt)
                st.info(resposta_ia.text)

    with col_alerta:
        st.subheader("🔔 Sistema de Alerta (POC)")
        st.write("Simulação de disparo de notificações para eventos críticos.")
        email_alerta = st.text_input("E-mail para receber alertas:")
        gatilho_km = st.number_input("Avisar se distância for menor que (km):", value=5000000, step=1000000)
        
        if st.button("Testar Gatilho de Alerta", use_container_width=True, type="primary"):
            if email_alerta:
                # Lógica para verificar se algum asteroide rompeu o limite
                criticos = df[df['Distância da Terra (km)'] < gatilho_km]
                
                with st.spinner("Verificando regras e conectando ao SMTP..."):
                    time.sleep(1.5) # Simula o tempo de rede
                    
                if len(criticos) > 0:
                    st.error(f"🚨 ALERTA: {len(criticos)} objeto(s) violaram a regra de distância! E-mail disparado para {email_alerta}.")
                    st.toast('E-mail enviado com sucesso!', icon='📧')
                else:
                    st.success(f"✅ Nenhum objeto violou a regra atual. Monitoramento ativo para {email_alerta}.")
            else:
                st.warning("Por favor, insira um e-mail válido para testar.")

else:
    st.error("Falha ao carregar dados da NASA. Verifique a conexão ou a chave de API.")