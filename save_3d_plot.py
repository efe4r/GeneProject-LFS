import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA

# Read the cleaned dataset
data = pd.read_csv(r"C:\Users\PC\Desktop\GeneProject-LFS\gene_expression_cleaned.csv")

# Select only numeric columns
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

# Apply PCA to reduce dimensionality to 3 components
pca = PCA(n_components=3)
pca_result = pca.fit_transform(data[numeric_cols])
data['PCA1'] = pca_result[:, 0]
data['PCA2'] = pca_result[:, 1]
data['PCA3'] = pca_result[:, 2]

# Choose color column (categorical or first numeric feature)
if 'type' in data.columns:
    color_col = 'type'
else:
    color_col = numeric_cols[0]

# Create 3D scatter plot
fig = px.scatter_3d(
    data, x='PCA1', y='PCA2', z='PCA3',
    color=color_col,
    hover_data=['samples'],
    width=900, height=700
)

# Layout customization: title, axis labels, and background colors
fig.update_layout(
    title="3D PCA Visualization of Gene Expression Data",
    scene=dict(
        xaxis_title='PCA1',
        yaxis_title='PCA2',
        zaxis_title='PCA3',
        bgcolor='white'  # 3D axis background
    ),
    paper_bgcolor='white',  # Outer plot background
)

# Save the visualization as both HTML and PNG
fig.write_html(r"C:\Users\PC\Desktop\GeneProject-LFS\3D_PCA_Plot.html")
fig.write_image(r"C:\Users\PC\Desktop\GeneProject-LFS\3D_PCA_Plot.png")

print("3D PCA visualization saved successfully as HTML and PNG in the 'GeneProject-LFS' folder.")
