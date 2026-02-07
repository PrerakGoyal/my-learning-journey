import pandas as pd

df = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "price": [80000, 30000, 25000, 90000, 32000],
    "city": ["Delhi", "Pune", "Delhi", "Mumbai", "Pune"]
})
print(df)
df["price_after_tax"]= df["price"] * 1.10
print(df)
df["price_after_discount"] = df["price"] - 5000
df["product"] = df["product"].str.lower()
df["is_expensive"]= df["price"] > 50000
print(df)
print(df.loc[df["city"] == "Pune", ["product", "price", "price_after_tax"]])
def func(x):
    if x >= 50000:
        return "premium"
    elif x >= 30000:
        return "mid"
    else:
        return "budget"
    
df["category"] = df["price"].apply(func)
print(df)
avg_price = df.groupby("city")["price"].mean()
print(avg_price)
avg_price_after_tax = df.groupby("city")["price_after_tax"].mean()
print(df["city"], avg_price, avg_price_after_tax)
premium_summary = df[df["category"] == "premium"].groupby("city").agg({
    "price": "mean",
    "price_after_tax": "mean",
    "price_after_discount": "mean"
})

print(premium_summary)
