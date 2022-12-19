import pandas as pd
# csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")
csv_data = pd.read_csv("./0_dataSet/shopping_data_missingvalue.csv")
print(csv_data.mean())  # nilai mean (rata-rata)
# print(csv_data.min()) # nilai min (terkecil)
# print(csv_data.max()) # nilai max (terbesar)
# print(csv_data.median()) # nilai median (nilai tengah)

# Print 10 data teratas
print("Dataset yang masih terdapat nilai kosong ! :")
print(csv_data.head(10))

# Print 10 data teratas value kosong diganti dengan nilai dari mean
csv_data = csv_data.fillna(csv_data.mean())
print("Dataset yang sudah diproses Handling Missing Values dengan Mean :")
print(csv_data.head(10))
