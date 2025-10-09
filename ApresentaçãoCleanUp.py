import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Empreiteiros - Painel Interativo",
    layout="wide",
    page_icon="📡"
)

# =========================
# ESTILO GLOBAL (CSS)
# =========================
st.markdown("""
    <style>
        /* Fundo e tipografia */
        body {
            background-color: #f4f6fa;
            font-family: "Segoe UI", sans-serif;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #001f3f;
            color: white;
        }

        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: white;
        }

        /* Título principal */
        .main-title {
            text-align: center;
            color: #003366;
            font-weight: 700;
            margin-top: -15px;
        }

        /* Cartões de rota */
        .rota-card {
            border: 1px solid #ccc;
            border-radius: 12px;
            padding: 10px;
            height: 75px;
            text-align: center;
            font-size: 12px;
            font-weight: 600;
            color: #003366;
            background-color: #ffffff;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
            transition: all 0.2s ease-in-out;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            word-wrap: break-word;
        }

        .rota-card:hover {
            background-color: #e6f0ff;
            transform: scale(1.02);
            box-shadow: 3px 3px 8px rgba(0,0,0,0.15);
        }

        .rota-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📋 Empreiteiros")
psm = st.sidebar.radio("Selecione um PSM", ["FIBRASOL", "ANGLOBAL", "ISITEL"])

st.sidebar.markdown("---")
st.sidebar.markdown("💡 _Visualize as rotas e métricas de desempenho de cada empreiteiro._")

# =========================
# LISTAS DE ROTAS
# =========================
rotas_isitel = [
    "Lucola - Hoji_Cacongo",
    "Hoji_Cacongo - Belize",
    "Hoji_Cacongo - Massabe_Fronteira",
    "Massabi_Fronteira - Belize",
    "Corda_Expansão_Cabassango",
    "BSC_Cabinda - Quatro",
    "Quatro - Tchizu_O",
    "Tchizu_O - Cine_Popular",
    "Cine_Popular - BSC_Cabinda",
    "BSC_Cabinda - Resistencia (Cabo_1)",
    "BSC_Cabinda - Resistencia (Cabo_2)",
    "Resistencia - Cine_Popular",
    "Quatro - PV_Grande_NT",
    "PV_Grande_NT - Tchizu_O",
    "Resistencia - Lucola",
    "Lucola - Tchizu_O",
    "PV_Grande_NT - Yema_Fronteira"
]

# =========================
# FUNÇÃO DE TABELA MODERNA
# =========================
def tabela_rotas(rotas, empreiteiro):
    st.markdown(f"<h2 class='main-title'>Rotas {empreiteiro}</h2>", unsafe_allow_html=True)

    st.markdown("<div class='rota-grid'>", unsafe_allow_html=True)
    for rota in rotas:
        rota_formatada = rota.replace("-", "<br>")
        st.markdown(
            f"""
            <div class='rota-card' onclick="window.alert('Abrir detalhes da rota: {rota}')">
                {rota_formatada}
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# CONTEÚDO PRINCIPAL
# =========================
if psm == "ISITEL":
    tabela_rotas(rotas_isitel, "ISITEL")
elif psm == "FIBRASOL":
    st.markdown("<h2 class='main-title'>Rotas FIBRASOL</h2>", unsafe_allow_html=True)
    st.info("Conteúdo em desenvolvimento...")
elif psm == "ANGLOBAL":
    st.markdown("<h2 class='main-title'>Rotas ANGLOBAL</h2>", unsafe_allow_html=True)
    st.info("Conteúdo em desenvolvimento...")

# =========================
# FUTURO: GRÁFICOS DE ROTAS
# =========================
with st.expander("📊 Visualização futura de desempenho das rotas"):
    st.write("""
        Aqui serão exibidos **gráficos de colunas interativos** com estatísticas
        de desempenho, manutenção e disponibilidade por rota.
        """)
