import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
import streamlit as st

st.title("Gen Verisi 3D Görselleştirme")

# CSV dosyasını oku
data = pd.read_csv(r"C:\Users\PC\Desktop\GeneProject\gene_expression_cleaned.csv")

# Kullanıcıya filtreleme seçeneği sun
if 'type' in data.columns:
    types = data['type'].unique().tolist()
    selected_types = st.multiselect("Tip seç:", types, default=types)
    data = data[data['type'].isin(selected_types)]

# Sadece sayısal kolonları seç
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

# PCA ile 3 boyuta indir
pca = PCA(n_components=3)
pca_result = pca.fit_transform(data[numeric_cols])
data['PCA1'] = pca_result[:, 0]
data['PCA2'] = pca_result[:, 1]
data['PCA3'] = pca_result[:, 2]

# Renk kolonunu seç
if 'type' in data.columns:
    color_col = 'type'
else:
    color_col = numeric_cols[0]

# 3D scatter plot
fig = px.scatter_3d(
    data, x='PCA1', y='PCA2', z='PCA3',
    color=color_col,
    hover_data=['samples'],
    width=900, height=700
)

st.plotly_chart(fig)
