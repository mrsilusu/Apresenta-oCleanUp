import streamlit as st

# Configuração da página
st.set_page_config(page_title="Empreiteiros", layout="wide")

# Sidebar
st.sidebar.title("Empreiteiros")
opcao = st.sidebar.radio("Selecione o empreiteiro", ["FIBRASOL", "ANGLOBAL", "ISITEL"])

# Função para criar tabela clicável
def tabela_rotas_isitel():
    rotas = [
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

    st.markdown(
        "<h2 style='text-align: center; color: #004aad;'>Rotas ISITEL</h2>",
        unsafe_allow_html=True
    )

    # Criar tabela dinâmica 4x5
    for i in range(0, len(rotas), 5):
        cols = st.columns(5, gap="small")
        for j, col in enumerate(cols):
            if i + j < len(rotas):
                rota = rotas[i + j]
                nome_formatado = rota.replace("-", "-<br>")
                col.markdown(
                    f"""
                    <div style='
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        text-align: center;
                        padding: 8px;
                        height: 70px;
                        background-color: #f9f9f9;
                        transition: 0.3s;
                        font-size: 11px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        cursor: pointer;
                    '
                    onmouseover="this.style.backgroundColor='#dfe9ff';"
                    onmouseout="this.style.backgroundColor='#f9f9f9';"
                    onclick="window.alert('Clicou em {rota}')"
                    >
                        <b>{nome_formatado}</b>
                    </div>
                    """, unsafe_allow_html=True
                )

# Conteúdo principal
if opcao == "FIBRASOL":
    st.write("### Página FIBRASOL — conteúdo em desenvolvimento...")
elif opcao == "ANGLOBAL":
    st.write("### Página ANGLOBAL — conteúdo em desenvolvimento...")
elif opcao == "ISITEL":
    tabela_rotas_isitel()
