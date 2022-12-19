import pandas as pd

#csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
csv_data = pd.read_csv("./0_dataSet/shopping_data.csv")

print(csv_data.columns)
print("Sedangkan untuk mengkases data kolom tertentu menggunakan ciri kolomnya")
print("Misal print(csv_data[\"Age\"]")
print(csv_data["Age"])
print("Akses data kolom berdasar Customer ID")
print(csv_data["CustomerID"])
