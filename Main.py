import pandas as pd

# قراءة البيانات
data = pd.read_csv("data.csv")

# حساب المعدلات
print("🔍 معدل تركيز كل معدن:")
print(data.mean(numeric_only=True))