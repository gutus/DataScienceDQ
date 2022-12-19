import pandas as pd
# csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
csv_data = pd.read_csv("./0_dataSet/shopping_data.csv")
# print(csv_data.describe(include="all")) #menampilkan semua termasuk data NaN
print(csv_data.describe(exclude="O"))  # menampilkan hanya object numerik
