import streamlit as st

# Página Streamlit: Empreteiros (PSM)
st.set_page_config(page_title="Empreteiros", layout="wide")

# Sidebar
st.sidebar.title("Empreteiros")
companies = ["FIBRASOL", "ANGLOBAL", "ISITEL"]
choice = st.sidebar.radio("Selecione um PSM:", companies)

# Rotas específicas para ISITEL
isitel_rotas = [
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

# Sidebar — expanders para ISITEL
if choice == "ISITEL":
    with st.sidebar.expander("Rotas ISITEL", expanded=False):
        for rota in isitel_rotas:
            st.sidebar.markdown(f"- {rota}")

# Conteúdo principal
st.title("Apresentação Interativa — Empreteiros")
st.markdown("Escolha um PSM no menu lateral para ver mais informações.")

# Informação por empresa
info = {
    "FIBRASOL": {
        "Descrição": "Empresa especializada em implementação e manutenção de redes de fibra óptica.",
        "Serviços": "FTTx, OTDR, manutenção preventiva e corretiva, projetos DWDM.",
        "Contacto": "contact@fibrasol.example"
    },
    "ANGLOBAL": {
        "Descrição": "Prestadora de serviços integrada em telecomunicações e infraestrutura.",
        "Serviços": "Instalação, manutenção de rede, gestão de projetos.",
        "Contacto": "contact@anglobal.example"
    },
    "ISITEL": {
        "Descrição": "Operadora com foco em soluções corporativas e integrações de sistemas.",
        "Serviços": "Soluções IT, suporte técnico, integrações de voz e dados.",
        "Contacto": "contact@isitel.example"
    }
}

selected = info.get(choice, {})

# Layout principal
col1, col2 = st.columns([2, 1])
with col1:
    st.header(choice)
    st.subheader(selected.get("Descrição", ""))
    st.write("**Serviços:**", selected.get("Serviços", ""))
    st.write("**Contacto:**", selected.get("Contacto", ""))
    st.markdown("---")

    # Caso o PSM seja ISITEL → mostrar tabela de rotas
    if choice == "ISITEL":
        st.markdown("## Rotas ISISTEL")
        st.write("Clique em uma rota para ver detalhes (função em desenvolvimento).")

        num_cols = 5  # número de colunas
        num_rows = 4  # número de linhas (ajustável)
        idx = 0

        # Geração da tabela 4x5 dinamicamente
        for i in range(num_rows):
            cols = st.columns(num_cols)
            for col in cols:
                if idx < len(isitel_rotas):
                    rota = isitel_rotas[idx]
                    with col:
                        clicked = st.button(rota, key=f"rota_{idx}")
                        if clicked:
                            st.session_state["rota_selecionada"] = rota
                    idx += 1
                else:
                    with col:
                        st.empty()

        # Exibir feedback se alguma rota for clicada
        if "rota_selecionada" in st.session_state:
            st.success(f"Rota selecionada: {st.session_state['rota_selecionada']}")

with col2:
    st.image("https://via.placeholder.com/300x180.png?text=" + choice, caption=choice)
    with st.expander("Dados rápidos"):
        st.metric(label="Projetos ativos", value=3)
        st.metric(label="Tickets abertos", value=1)

# Rodapé
st.markdown("---")
st.caption("App interativo criado com Streamlit — pronto para deploy no GitHub e Streamlit Cloud.")

# Instruções rápidas
with st.expander("Como usar / Deploy"):
    st.markdown(
        """
        **Rodar localmente:**
        1. Instale o Streamlit: `pip install streamlit`
        2. Execute: `streamlit run app.py`

        **Fazer deploy (resumo):**
        1. Crie um repositório no GitHub e adicione este arquivo (`app.py`) e `requirements.txt` com `streamlit`.
        2. No Streamlit Community Cloud, escolha 'New app' e conecte o repositório GitHub.
        3. Aponte para o arquivo `app.py` e clique em deploy.
        """
    )
