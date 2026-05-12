import pandas as pd 


orders = [
    {"order_id": 1, "customer": "Ana", "category": "Shoes", "price": 120, "quantity": 1, "date": "2024-01-05"},
    {"order_id": 2, "customer": "Marko", "category": "T-Shirts", "price": None, "quantity": 2, "date": "2024-01-10"},
    {"order_id": 3, "customer": "Ana", "category": "Shoes", "price": 150, "quantity": 1, "date": "2024-02-01"},
    {"order_id": 3, "customer": "Ana", "category": "Shoes", "price": 150, "quantity": 1, "date": "2024-02-01"},
    {"order_id": 4, "customer": "Jelena", "category": None, "price": 200, "quantity": 1, "date": "2024-02-15"},
    {"order_id": 5, "customer": "Petar", "category": "T-Shirts", "price": 25, "quantity": None, "date": "2024-03-01"},
    {"order_id": 6, "customer": "Marko", "category": "Shoes", "price": 100, "quantity": 1, "date": "2024-03-10"},
]

df = pd.DataFrame(orders)
print(df.isna().sum())
print(df.head(7))
print(df.dtypes)

#prosecna cena
avg_price = df['price'].mean()
print('Average price:',avg_price)


#popunjavanje None polja proswcnom cenom
df['price'] = df['price'].fillna(avg_price)
print(df)

#popunjavanje nedostajucih vrenosti u koloni quantity

df['quantity'] = df['quantity'].fillna(1)
print(df)

#popunjavanje nedostajucih vrednsoti u koloni category

df['category'] = df['category'].fillna("Unknown")
print(df)

#uklanjanje duplikata 

df = df.drop_duplicates()
print(df)


#konvertovanje date u datetime 

df['date'] = pd.to_datetime(df['date'])

#dodavanje kolone revenue 

df['revenue'] = df['price'] * df['quantity']
print(df)

#ukupna zarada

total_revenue = df['revenue'].sum()
print('Total revenue:',total_revenue)

#zarada po kategoriji 

revenue_per_category = df.groupby('category')['revenue'].sum()
print('Revenu per category:',revenue_per_category)

#top customer 

top_customer = df.groupby('customer')['revenue'].sum().idxmax()
print("Top customer:",top_customer)

#mesec sa najvecom zaradom 

df['month'] = df['date'].dt.month

best_month = df.groupby('month')['revenue'].sum().sort_values(ascending = False).head(1)
print('Best month:',best_month)




