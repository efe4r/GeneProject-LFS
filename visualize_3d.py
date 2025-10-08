import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
import streamlit as st

# -------------------------------
# App Title
# -------------------------------
st.title("3D Visualization of Gene Expression Data")

# -------------------------------
# Load CSV File
# -------------------------------
data = pd.read_csv(r"C:\Users\PC\Desktop\GeneProject-LFS\gene_expression_cleaned.csv")

# -------------------------------
# Filtering Option for Data Types
# -------------------------------
if 'type' in data.columns:
    types = data['type'].unique().tolist()
    selected_types = st.multiselect("Select sample types:", types, default=types)
    data = data[data['type'].isin(selected_types)]

# -------------------------------
# Select Numeric Columns
# -------------------------------
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

# -------------------------------
# Apply PCA (3 Components)
# -------------------------------
pca = PCA(n_components=3)
pca_result = pca.fit_transform(data[numeric_cols])
data['PCA1'] = pca_result[:, 0]
data['PCA2'] = pca_result[:, 1]
data['PCA3'] = pca_result[:, 2]

# -------------------------------
# Choose Color Column
# -------------------------------
if 'type' in data.columns:
    color_col = 'type'
else:
    color_col = numeric_cols[0]

# -------------------------------
# Create 3D Scatter Plot
# -------------------------------
fig = px.scatter_3d(
    data,
    x='PCA1', y='PCA2', z='PCA3',
    color=color_col,
    hover_data=['samples'],
    width=900, height=700,
    title="3D PCA Visualization of Gene Expression Profiles"
)

# -------------------------------
# Display Plot in Streamlit
# -------------------------------
st.plotly_chart(fig)
