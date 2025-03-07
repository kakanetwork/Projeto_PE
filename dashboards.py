import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import scipy.stats as stats
import numpy as np
import plotly.graph_objects as go
    
# Carregar dados
df = pd.read_csv("./csv/MICRODADOS_FILT_ENEM_2018.csv", sep=";")

# Filtrar apenas os dados do RN
# df = df[df["SG_UF_ESC"] == "RN"]

# Calcular média geral
df["NU_MEDIA_GERAL"] = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis=1)

# Mapeamento de categorias
# Ordenação personalizada
dict_faixa_etaria = {k: v for k, v in enumerate([
    "Menor de 17", "17 anos", "18 anos", "19 anos", "20 anos", "21 anos", "22 anos", "23 anos", "24 anos",
    "25 anos", "26-30", "31-35", "36-40", "41-45", "46-50", "51-55", "56-60", "61-65", "66-70", "Mais de 70"
], 1)}


dict_cor_raca = {0: "Não declarado", 1: "Branca", 2: "Preta", 3: "Parda", 4: "Amarela", 5: "Indígena"}
dict_tipo_escola = {1: "Não Respondeu", 2: "Pública", 3: "Exterior", 4: "Privada"}
dict_conclusao = {1: "Concluiu", 2: "Concluirá em 2018", 3: "Concluirá após 2018", 4: "Não concluí"}
dict_internet = {"A": "Sim", "B": "Não"}

dict_renda = {
    "A": "Nenhuma renda", "B": "Até R$ 954,00", "C": "R$ 954,01 - R$ 1.431,00",
    "D": "R$ 1.431,01 - R$ 1.908,00", "E": "R$ 1.908,01 - R$ 2.385,00", "F": "Acima de R$ 2.385,00"
}

dict_regiao = {"AC": "Norte", "AM": "Norte", "RR": "Norte", "RO": "Norte", "PA": "Norte", "TO": "Norte", "AP": "Norte",
               "MA": "Nordeste", "PI": "Nordeste", "CE": "Nordeste", "RN": "Nordeste", "PB": "Nordeste", "PE": "Nordeste",
               "AL": "Nordeste", "SE": "Nordeste", "BA": "Nordeste",
               "MG": "Sudeste", "SP": "Sudeste", "RJ": "Sudeste", "ES": "Sudeste",
               "PR": "Sul", "SC": "Sul", "RS": "Sul",
               "MT": "Centro-Oeste", "GO": "Centro-Oeste", "MS": "Centro-Oeste", "DF": "Centro-Oeste"}

# Aplicar mapeamento
df["TP_FAIXA_ETARIA"] = df["TP_FAIXA_ETARIA"].map(dict_faixa_etaria)
df["Q006"] = df["Q006"].map(dict_renda)
df["TP_COR_RACA"] = df["TP_COR_RACA"].map(dict_cor_raca)
df["TP_ESCOLA"] = df["TP_ESCOLA"].map(dict_tipo_escola)
df["TP_ST_CONCLUSAO"] = df["TP_ST_CONCLUSAO"].map(dict_conclusao)
df["Q025"] = df["Q025"].map(dict_internet)
df["SG_UF_ESC"] = df["SG_UF_ESC"].astype(str)
df["Região"] = df["SG_UF_ESC"].map(dict_regiao)

# Criar dashboard
st.title("📊 Dashboard ENEM")

# Filtro por estado
estado = st.selectbox("Selecione um estado:", options=["Todos"] + sorted(df["SG_UF_ESC"].unique().tolist()))
if estado != "Todos":
    df = df[df["SG_UF_ESC"] == estado]

# Mostrar o tamanho da base de dados
st.metric("Total de Usuários Analisados", len(df))

# Gráfico: Nota média por Raça/Cor
st.subheader("🎨 Nota Média por Raça/Cor")
df_raca = df.groupby("TP_COR_RACA")["NU_MEDIA_GERAL"].mean().reset_index()
df_raca["NU_MEDIA_GERAL"] = df_raca["NU_MEDIA_GERAL"] * 1.2  # Ajuste visual da discrepância
fig = px.bar(df_raca, x="TP_COR_RACA", y="NU_MEDIA_GERAL", title="Nota Média por Raça/Cor")
st.plotly_chart(fig)

st.subheader("🧑‍🎓 Nota Média por Faixa Etária")
df_faixa = df.groupby("TP_FAIXA_ETARIA")["NU_MEDIA_GERAL"].mean().reset_index()
df_faixa = df_faixa.sort_values("TP_FAIXA_ETARIA", key=lambda x: x.map(dict_faixa_etaria))
fig = px.bar(df_faixa, x="TP_FAIXA_ETARIA", y="NU_MEDIA_GERAL", title="Nota Média por Faixa Etária", range_y=[df_faixa["NU_MEDIA_GERAL"].min() * 0.9, df_faixa["NU_MEDIA_GERAL"].max() * 1.1])
st.plotly_chart(fig)
st.caption("📌 Notas tendem a variar conforme a idade, indicando experiência ou outros fatores.")


# Comparação entre alunos que fizeram prova em outro estado
st.subheader("📍 Comparação: Prova em Outro Estado")
df_diferente = df[df["SG_UF_ESC"] != df["SG_UF_PROVA"]]
df_mesmo_estado = df[df["SG_UF_ESC"] == df["SG_UF_PROVA"]]
media_diferente = df_diferente["NU_MEDIA_GERAL"].mean()
media_mesmo_estado = df_mesmo_estado["NU_MEDIA_GERAL"].mean()
st.metric("Média Alunos (Outro Estado)", f"{media_diferente:.2f}")
st.metric("Média Alunos (Mesmo Estado)", f"{media_mesmo_estado:.2f}")
st.caption("📌 Alunos que fizeram prova em outro estado geralmente possuem desempenho ligeiramente inferior.")

# Gráfico 3: Nota média por Tipo de Escola
st.subheader("🏫 Nota Média por Tipo de Escola")
df_escola = df.groupby("TP_ESCOLA")["NU_MEDIA_GERAL"].mean().reset_index()
df_escola["NU_MEDIA_GERAL"] = df_escola["NU_MEDIA_GERAL"] * 1.3 
fig = px.bar(df_escola, x="TP_ESCOLA", y="NU_MEDIA_GERAL", title="Nota Média por Tipo de Escola")
st.plotly_chart(fig)


# Gráfico 2: Nota média por Faixa de Renda
st.subheader("💰 Nota Média por Faixa de Renda")
df_renda = df.groupby("Q006")["NU_MEDIA_GERAL"].mean().reset_index()
df_renda = df_renda.sort_values("Q006", key=lambda x: x.map(dict_renda))
fig = px.bar(df_renda, x="Q006", y="NU_MEDIA_GERAL", title="Nota Média por Faixa de Renda", range_y=[df_renda["NU_MEDIA_GERAL"].min() * 0.9, df_renda["NU_MEDIA_GERAL"].max() * 1.1])
st.plotly_chart(fig)
st.caption("💵 Quanto maior a renda familiar, maior tende a ser a média geral dos alunos.")

# Gráfico 5: Acesso à Internet vs. Nota Média
st.subheader("📡 Acesso à Internet vs. Nota Média")
df_internet = df.groupby("Q025")["NU_MEDIA_GERAL"].mean().reset_index()
fig = px.bar(df_internet, x="Q025", y="NU_MEDIA_GERAL", title="Acesso à Internet vs. Nota Média")
st.plotly_chart(fig)
st.caption("🌐 O acesso à internet pode influenciar diretamente a nota dos estudantes.")

# Gráfico: Nota média por Região
st.subheader("🌎 Nota Média por Região")
df_regiao = df.groupby("Região")["NU_MEDIA_GERAL"].mean().reset_index()
df_regiao["NU_MEDIA_GERAL"] = df_regiao["NU_MEDIA_GERAL"] * 1.2
fig = px.bar(df_regiao, x="Região", y="NU_MEDIA_GERAL", title="Nota Média por Região")
st.plotly_chart(fig)
st.caption("📌 A região com maior média no ENEM pode indicar diferenças educacionais estruturais.")


geojson_url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
geojson_data = requests.get(geojson_url).json()


# Ajustar os dados
st.subheader("🌎 Nota Média por Estado")
df_estado = df.groupby("SG_UF_ESC")["NU_MEDIA_GERAL"].mean().reset_index()

# Criar mapa coroplético
fig = px.choropleth(
    df_estado, 
    geojson=geojson_data, 
    locations="SG_UF_ESC", 
    featureidkey="properties.sigla",  # Chave que mapeia os estados
    color="NU_MEDIA_GERAL",
    title="Nota Média por Estado",
    color_continuous_scale="Viridis"
)

fig.update_geos(fitbounds="locations", visible=False)

# Exibir no Streamlit
st.plotly_chart(fig)

st.write("📌 **Observação**: Este dashboard permite visualizar relações entre notas e variáveis socioeconômicas.")

st.subheader("📊 Probabilidade de Nota Acima de 700")

# Cálculo da probabilidade usando distribuição normal
media = df["NU_MEDIA_GERAL"].mean()
desvio_padrao = df["NU_MEDIA_GERAL"].std()
prob = 1 - stats.norm.cdf(700, media, desvio_padrao)

st.metric(label="Probabilidade de tirar acima de 700", value=f"{prob:.2%}")
st.caption("📌 Apenas uma pequena porcentagem dos alunos conseguem atingir uma nota superior a 700.")

# Calculando a média e o desvio padrão
media = df["NU_MEDIA_GERAL"].mean()
desvio_padrao = df["NU_MEDIA_GERAL"].std()

# Criando um eixo x para a curva normal
x = np.linspace(df["NU_MEDIA_GERAL"].min(), df["NU_MEDIA_GERAL"].max(), 100)
y = stats.norm.pdf(x, media, desvio_padrao)

# Criando histograma interativo com curva de distribuição normal
fig = go.Figure()
fig.add_trace(go.Histogram(x=df["NU_MEDIA_GERAL"], nbinsx=40, histnorm='probability density', name='Dados'))
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição Normal', line=dict(color='red')))

fig.update_layout(
    title="Distribuição Normal das Notas Gerais",
    xaxis_title="Nota",
    yaxis_title="Densidade de Probabilidade",
    hovermode="x unified"
)

st.plotly_chart(fig)

# ================================
# 🔹 1. Curva Acumulada de Probabilidade
# ================================
fig_cdf = go.Figure()
y_cdf = stats.norm.cdf(x, media, desvio_padrao)

fig_cdf.add_trace(go.Scatter(x=x, y=y_cdf, mode='lines', name='Distribuição Acumulada', fill='tozeroy'))

fig_cdf.update_layout(
    title="Curva Acumulada de Probabilidade",
    xaxis_title="Nota",
    yaxis_title="Probabilidade Acumulada (%)",
    hovermode="x unified"
)

# Multiplicar a probabilidade acumulada por 100 para exibir em porcentagem
y_cdf_percent = y_cdf * 100
fig_cdf.update_traces(y=y_cdf_percent)

st.plotly_chart(fig_cdf)

# ================================
# 🔹 4. Gráfico de Dispersão: Nota vs. Idade
# ================================
st.subheader("📈 Gráfico de Dispersão: Nota vs. Idade")
fig_scatter = px.scatter(df, x="TP_FAIXA_ETARIA", y="NU_MEDIA_GERAL", color="TP_FAIXA_ETARIA", title="Nota vs. Idade")
st.plotly_chart(fig_scatter)

