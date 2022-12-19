import pandas as pd

#sv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
csv_data = pd.read_csv("./0_dataSet/shopping_data.csv")

print(csv_data.iloc[5])  # menggunakan perintah .iloc[index baris]
