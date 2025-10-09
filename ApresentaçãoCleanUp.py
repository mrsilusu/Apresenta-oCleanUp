import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards

# =====================
# CONFIGURAÇÕES GERAIS
# =====================
st.set_page_config(
    page_title="Apresentação CleanUp AutoProcess",
    layout="wide",
    page_icon="🧹"
)

# =====================
# ESTILO CUSTOMIZADO
# =====================
st.markdown("""
    <style>
        body {
            background-color: #f7f9fb;
        }
        .main {
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #1E3A8A;
            font-weight: 700;
        }
        .small-text {
            font-size: 14px !important;
        }
        .metric-container {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
        }
        .metric-card {
            background: #fff;
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            flex: 1;
            min-width: 180px;
            text-align: center;
        }
        .metric-card h4 {
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 0.5rem;
            word-break: keep-all;
        }
        .metric-card span {
            font-size: 18px;
            color: #2563EB;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# =====================
# TÍTULO PRINCIPAL
# =====================
st.title("🧹 CleanUp AutoProcess – Painel de Apresentação")

st.markdown("### 📍 Monitoramento de Rotas dos Empreiteiros (ISITEL)")
st.markdown("Visualização consolidada das medições OTDR, status e rotas tratadas no sistema CleanUp AutoProcess.")

# =====================
# DADOS DE EXEMPLO (podes substituir pelo teu dataframe real)
# =====================
dados = {
    "Empreiteiro": ["ISITEL", "ISITEL", "PSM", "PSM", "TECNOLINK", "TECNOLINK"],
    "Rota": [
        "Zango 0 - Cacuaco",
        "Viana 1 - Kikuxi",
        "Mutamba - Maculusso",
        "Maianga - Kinaxixi",
        "Talatona - Patriota",
        "Benfica - Samba"
    ],
    "Status": ["Concluído", "Em andamento", "Concluído", "Concluído", "Pendente", "Em andamento"],
    "Medições": [43, 25, 52, 48, 18, 21]
}

df = pd.DataFrame(dados)

# =====================
# VISUALIZAÇÃO AGRUPADA
# =====================
for empreiteiro, grupo in df.groupby("Empreiteiro"):
    st.subheader(f"👷 {empreiteiro}")

    # Exibe métricas em linha como "cards"
    cols = st.columns(len(grupo))
    for i, (_, row) in enumerate(grupo.iterrows()):
        with cols[i]:
            st.markdown(f"""
                <div class="metric-card">
                    <h4 class="small-text">{row['Rota']}</h4>
                    <span>{row['Medições']} medições</span><br>
                    <small>Status: <b>{row['Status']}</b></small>
                </div>
            """, unsafe_allow_html=True)

    style_metric_cards()

    # ================
    # FUTURO: GRÁFICO DE COLUNAS
    # (mantido comentado para uso posterior)
    # ================
    # import altair as alt
    # chart = alt.Chart(grupo).mark_bar().encode(
    #     x='Rota',
    #     y='Medições',
    #     color='Status',
    #     tooltip=['Rota', 'Medições', 'Status']
    # ).properties(
    #     width=600,
    #     height=300,
    #     title=f"Gráfico de Medições - {empreiteiro}"
    # )
    # st.altair_chart(chart, use_container_width=True)

    st.markdown("---")

# =====================
# RODAPÉ
# =====================
st.markdown("""
    <div style='text-align:center; margin-top:2rem; color:gray; font-size:13px'>
        © 2025 CleanUp AutoProcess | Desenvolvido para análise automática de medições OTDR.
    </div>
""", unsafe_allow_html=True)
