import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA

# CSV dosyasını oku
data = pd.read_csv(r"C:\Users\PC\Desktop\GeneProject\gene_expression_cleaned.csv")

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

# Layout güncellemeleri: başlık, eksen isimleri ve arka plan
fig.update_layout(
    title="Gen Verisi 3D PCA Görselleştirme",
    scene=dict(
        xaxis_title='PCA1',
        yaxis_title='PCA2',
        zaxis_title='PCA3',
        bgcolor='white'  # 3D eksen arka planı
    ),
    paper_bgcolor='white',  # Grafik dışı alan arka planı
)

# Kaydet (HTML ve PNG)
fig.write_html(r"C:\Users\PC\Desktop\GeneProject\3d_pca_plot.html")
fig.write_image(r"C:\Users\PC\Desktop\GeneProject\3d_pca_plot.png")

print("3D PCA grafiği kaydedildi: HTML ve PNG olarak masaüstünde 'GeneProject' klasöründe.")
