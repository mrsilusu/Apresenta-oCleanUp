import streamlit as st
import pandas as pd
import plotly.express as px # Importação necessária para criar o gráfico

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

    # =======================================================
    # Lógica do Gráfico Dinâmico
    # =======================================================

    # 1. Definição das categorias e cores do gráfico
    status_categorias = [
        "Transporte Q1",
        "Indisponíveis",
        "Total Reparadas",
        "Reconhecidas",
        "Dep. de Passagem de Cabo",
        "Dep. de Licença",
        "Dependente de Cutover",
        "Fibras dependentes da FIBRASOL"
    ]

    # Mapeamento de cores conforme a imagem de referência (cores aproximadas)
    color_map = {
        "Transporte Q1": "#000000",             # Preto
        "Indisponíveis": "#FF0000",              # Vermelho
        "Total Reparadas": "#00A000",            # Verde Escuro
        "Reconhecidas": "#E0FFE0",               # Verde muito claro/Creme
        "Dep. de Passagem de Cabo": "#00BFFF",    # Azul Ciano
        "Dep. de Licença": "#B8860B",            # Marrom Dourado
        "Dependente de Cutover": "#191970",      # Azul Marinho
        "Fibras dependentes da FIBRASOL": "#778899" # Cinza (para hachura)
    }

    # 2. Criação do DataFrame inicial para entrada de dados
    initial_data = {
        'Rota': rotas_isistel,
        **{cat: [0] * len(rotas_isistel) for cat in status_categorias}
    }
    df_rotas = pd.DataFrame(initial_data).set_index('Rota')

    st.markdown("---")
    st.subheader("1. Introdução Manual dos Dados")
    st.info("Utilize a tabela abaixo para inserir o número de fibras para cada status e rota. O gráfico será atualizado automaticamente.")

    # 3. Widget st.data_editor para introdução manual dos dados
    edited_df = st.data_editor(
        df_rotas,
        column_config={
            cat: st.column_config.NumberColumn(
                f"{cat}",
                help=f"Número de fibras no status: {cat}",
                min_value=0,
                default=0,
                step=1,
                format="%d"
            ) for cat in status_categorias
        },
        height=400
    )

    # 4. Preparação dos dados para o Plotly (Formato Longo)
    df_long = edited_df.reset_index().melt(
        id_vars=['Rota'],
        value_vars=status_categorias,
        var_name='Status',
        value_name='Fibras'
    )

    # Remove linhas onde o valor de 'Fibras' é zero para limpar o gráfico
    df_long = df_long[df_long['Fibras'] > 0]

    # 5. Criação do Gráfico de Colunas Agrupadas (Stacked Column Chart)
    st.subheader("2. Gráfico de Rotas Estáveis")

    fig = px.bar(
        df_long,
        x='Rota',
        y='Fibras',
        color='Status',
        color_discrete_map=color_map, # Aplica o mapeamento de cores
        title='ROTAS ESTÁVEIS (Monitoramento PSM ISISTEL)',
        labels={'Rota': '', 'Fibras': 'Contagem de Fibras'},
        height=500
    )

    # Configurações de layout (ordem das rotas e inclinação dos rótulos)
    fig.update_layout(
        xaxis={'categoryorder': 'array', 'categoryarray': rotas_isistel},
        xaxis_tickangle=-45,
        legend_title_text='Status da Rota',
        hovermode="x unified"
    )

    # Adiciona os valores (Total de Fibras) no topo de cada coluna
    df_total = df_long.groupby('Rota')['Fibras'].sum().reset_index()

    for _, row in df_total.iterrows():
        # Adiciona o texto no topo da coluna
        fig.add_annotation(
            x=row['Rota'],
            y=row['Fibras'],
            text=str(row['Fibras']),
            showarrow=False,
            yshift=10,
            font=dict(size=10, color="black")
        )

    # Exibe o gráfico
    st.plotly_chart(fig, use_container_width=True)

    # =======================================================
    # Fim da Lógica do Gráfico
    # =======================================================

    st.markdown("---")
    st.subheader("3. Acesso Rápido às Rotas")


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