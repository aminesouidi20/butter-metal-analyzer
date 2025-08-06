import pandas as pd

# رابط ملف CSV من GitHub
url = "https://raw.githubusercontent.com/aminesouidi20/butter-metal-analyzer/main/data.csv"

# تحميل البيانات
data = pd.read_csv(url)

# عرض أول 5 صفوف للتأكد
print("🔍 أول 5 صفوف من البيانات:")
print(data.head())

# حساب المعدلات
print("\n📊 معدل تركيز كل معدن:")
print(data.mean(numeric_only=True))
