import pandas as pd
# csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
csv_data = pd.read_csv("./0_dataSet/shopping_data.csv")
print("Menampilkan data Age ke 5 sampai kurang dari 10 : ")
print(csv_data["Age"].iloc[5:10])
print("Menapilkan data dari baris 5 hingga 19")
print(csv_data.iloc[5:20])
