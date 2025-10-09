import streamlit as st
import pandas as pd

# --- Configurações da página ---
st.set_page_config(page_title="Empreteiros - PSM", layout="wide")

# --- Sidebar ---
st.sidebar.title("Empreteiros")
psm = st.sidebar.selectbox("Selecione um PSM", ["FIBRASOL", "ANGLOBAL", "ISITEL"])

# --- Lista de rotas da ISISTEL ---
rotas_isistel = [
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

# --- Área principal ---
st.title("Apresentação dos PSM")

if psm == "ISITEL":
    st.markdown("### Rotas ISISTEL")

    # Tabela 4 linhas x 5 colunas (com preenchimento automático)
    num_colunas = 5
    num_linhas = (len(rotas_isistel) // num_colunas) + 1

    # Divide as rotas em blocos de 5
    for i in range(num_linhas):
        cols = st.columns(num_colunas, gap="small")
        for j in range(num_colunas):
            index = i * num_colunas + j
            if index < len(rotas_isistel):
                rota = rotas_isistel[index]
                with cols[j]:
                    # Botões clicáveis para cada rota
                    st.button(
                        rota,
                        key=f"rota_{index}",
                        help=f"Clique para ver detalhes da rota {rota}"
                    )

    # Estilo adicional
    st.markdown("""
        <style>
        div.stButton > button {
            width: 100%;
            height: 80px;
            font-size: 13px;
            white-space: normal;
            text-align: center;
            line-height: 1.2;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

else:
    st.info(f"Selecione o PSM **ISISTEL** no menu lateral para visualizar as rotas.")
