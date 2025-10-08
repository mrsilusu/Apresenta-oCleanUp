import streamlit as st

# Configuração da página
st.set_page_config(page_title="Empreiteiros", layout="wide")

# Sidebar
st.sidebar.title("Empreiteiros")
opcao = st.sidebar.radio("Selecione o empreiteiro", ["FIBRASOL", "ANGLOBAL", "ISITEL"])

# Função para criar tabela clicável
def tabela_rotas_isitel():
    rotas = [
        "ISISTEL-ROTA1", "ISISTEL-ROTA2", "ISISTEL-ROTA3", "ISISTEL-ROTA4", "ISISTEL-ROTA5",
        "ISISTEL-ROTA6", "ISISTEL-ROTA7", "ISISTEL-ROTA8", "ISISTEL-ROTA9", "ISISTEL-ROTA10",
        "ISISTEL-ROTA11", "ISISTEL-ROTA12", "ISISTEL-ROTA13", "ISISTEL-ROTA14", "ISISTEL-ROTA15",
        "ISISTEL-ROTA16", "ISISTEL-ROTA17", "ISISTEL-ROTA18", "ISISTEL-ROTA19", "ISISTEL-ROTA20",
    ]

    st.markdown(
        """
        <h2 style='text-align: center; color: #004aad;'>Rotas ISITEL</h2>
        """, unsafe_allow_html=True
    )

    # Criar tabela 4 linhas x 5 colunas
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
                        padding: 12px;
                        height: 90px;
                        background-color: #f9f9f9;
                        transition: 0.3s;
                        font-size: 12px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        word-wrap: break-word;
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

# Conteúdo da página principal
if opcao == "FIBRASOL":
    st.write("### Página FIBRASOL — conteúdo em desenvolvimento...")
elif opcao == "ANGLOBAL":
    st.write("### Página ANGLOBAL — conteúdo em desenvolvimento...")
elif opcao == "ISITEL":
    tabela_rotas_isitel()
