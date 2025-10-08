import pandas as pd
from sklearn.preprocessing import StandardScaler

# File paths
input_file = r"C:\Users\PC\Desktop\GeneProject-LFS\gene_expression.csv"
output_file = r"C:\Users\PC\Desktop\GeneProject-LFS\gene_expression_cleaned.csv"

# Read CSV
data = pd.read_csv(input_file)

# Select only numeric columns
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

# Define chunk size (e.g., 2000 columns per batch)
chunk_size = 2000
chunks = [numeric_cols[i:i+chunk_size] for i in range(0, len(numeric_cols), chunk_size)]

# Initialize scaler
scaler = StandardScaler()

for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i+1}/{len(chunks)} ({len(chunk)} columns)...")
    # Fill missing values with column means
    data[chunk] = data[chunk].fillna(data[chunk].mean())
    # Normalize data
    data[chunk] = scaler.fit_transform(data[chunk])

# Save cleaned and normalized dataset
data.to_csv(output_file, index=False)
print(f"\nLarge-scale gene expression data cleaned and normalized successfully.\nOutput file: {output_file}")
