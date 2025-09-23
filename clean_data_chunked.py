import pandas as pd
from sklearn.preprocessing import StandardScaler

# CSV dosyasının yolu
input_file = r"C:\Users\PC\Desktop\GeneProject\gene_expression.csv"
output_file = r"C:\Users\PC\Desktop\GeneProject\gene_expression_cleaned.csv"

# CSV oku
data = pd.read_csv(input_file)

# Sadece sayısal kolonları seç
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

# İşlem için chunk boyutu (örnek: 2000 kolon)
chunk_size = 2000
chunks = [numeric_cols[i:i+chunk_size] for i in range(0, len(numeric_cols), chunk_size)]

scaler = StandardScaler()

for i, chunk in enumerate(chunks):
    print(f"{i+1}/{len(chunks)}. chunk işleniyor ({len(chunk)} kolon)...")
    # Eksik değerleri doldur
    data[chunk] = data[chunk].fillna(data[chunk].mean())
    # Normalize et
    data[chunk] = scaler.fit_transform(data[chunk])

# Kaydet
data.to_csv(output_file, index=False)
print("\nBüyük veri temizlendi ve normalize edildi. Dosya:", output_file)
