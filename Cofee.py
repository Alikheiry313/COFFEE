# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 120)
%matplotlib inline

# %%

df=pd.read_csv("dirty_cafe_sales.csv")
df


# %%
print(df.shape)

# %%
print(df.columns)
print(df.columns.to_list)

# %%
df.info()

# %%
print(df.value_counts())

# %%
df.describe(include='all')

# %%
Mising_Valuee=df.isnull().sum()
print(Mising_Valuee)



# %%
Mising_Present=df.isna().mean()*100

print(Mising_Present)





# %%
df = df.dropna(subset=['Location', 'Payment Method'])






# %%
df = df[df['Location'].notna()]


# %%
print(Mising_Present)

# %%
df['Item'].fillna('Unknown',inplace=True)
for col in['Quantity','Price Per Unit','Total Spent']:
   df[col].fillna(df[col].median,inplace=True)



# %%
df['Transaction Date']=df['Transaction Date'].ffill()

# %%
df.isnull().sum()

# %%
print(Mising_Present)

# %%
Mising_Present2=df.isna().mean()*100

print(Mising_Present2)

# %%
print(df.columns)

# %%

df['Transaction Date']=pd.to_datetime(df['Transaction Date'],errors='coerce')

df['year'] = df['Transaction Date'].dt.year
df['month'] = df['Transaction Date'].dt.month
df['hour'] = df['Transaction Date'].dt.hour

# %%
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit']=pd.to_numeric(df['Price Per Unit'],errors='coerce')
df['Total Spent']=pd.to_numeric(df['Total Spent'],errors='coerce')


# %%
df.dtypes

# %%
df['Payment Method']=df['Payment Method'].replace(['ERROR', 'UNKNOWN'], np.nan)

# %%
df['Item']=df['Item'].replace(['ERROR', 'UNKNOWN','Unknown'], np.nan)

# %%
# clean for location
df['Location'] = df['Location'].replace(['ERROR', 'UNKNOWN'], np.nan)

# %%
paymentMethod=df['Payment Method'].value_counts().sort_values(ascending=False)
print(paymentMethod)
plt.figure(figsize=(3,3))


plt.bar(paymentMethod.index,
        paymentMethod.values,
        width=0.4,
        color="#E37120",
        edgecolor='black',
        linewidth=1)

plt.title('payment method')
plt.grid(axis='y', linestyle='--', alpha=0.35)
plt.tight_layout()
plt.show()


# %%
import matplotlib.pyplot as plt


paymentMethod = df['Payment Method'].value_counts().sort_values(ascending=False)
print(paymentMethod)


autumn_colors = ['#FFB347', '#FF7733', '#CC5500', '#8B4513', '#FFD580']


plt.figure(figsize=(6,6))
plt.pie(
    paymentMethod,
    labels=paymentMethod.index,
    colors=autumn_colors[:len(paymentMethod)],
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 12, 'color': 'black'}
)
plt.title(' Distribution of Payment Method', fontsize=14, fontweight='bold')
plt.show()


# %%
Iteam=df['Item'].value_counts().sort_index(ascending=False)
print(Iteam)
plt.figure(figsize=(8,3))
plt.bar(Iteam.index,Iteam.values,width=0.4,color="#B58004",
        edgecolor='black',
        linewidth=1.2)
plt.title('Iteam')

plt.show()


        



# %%
import matplotlib.pyplot as plt

# Count and sort items
Iteam = df['Item'].value_counts().sort_index(ascending=False)
print(Iteam)

# Define autumn coffee shop colors
autumn_colors = ['#A0522D', '#D2691E', '#CD853F', '#8B4513', '#F4A460', '#DEB887']

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(Iteam.values, labels=Iteam.index, autopct='%1.1f%%', startangle=140, colors=autumn_colors, wedgeprops={'edgecolor':'black'})
plt.title('Items Distribution')
plt.show()


# %%
import matplotlib.pyplot as plt


purchasetype = df['Location'].value_counts(ascending=False)

autumn_colors = ['#FFB347', '#FF7733', '#CC5500', '#8B4513', '#FFD580']


plt.figure(figsize=(6,6))
plt.pie(
    purchasetype,
    labels=purchasetype.index,
    colors=autumn_colors[:len(purchasetype)],  
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 12, 'color': 'black'}
)
plt.title(' Distribution of Purchase Type (Location)', fontsize=14, fontweight='bold')
plt.show()


# %%
print("min sales data",df['Transaction Date'].min())
print('max sales data',df['Transaction Date'].max())

# %%
transactions_per_day = df.groupby('Transaction Date').size()
print(transactions_per_day.head())


# %%
plt.figure(figsize=(12,6))
plt.plot(transactions_per_day, color="#A44908", linewidth=3, marker='o', markerfacecolor="#8C8B8A")
plt.xlabel("Date of Transactions")
plt.ylabel("Number of Transactions")
plt.title("Daily Transactions ")
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()

# %%
Sales_Year_Top=df.groupby('year')['Total Spent'].mean()
print(Sales_Year_Top)

# %%
month_spent = df.groupby('month')['Total Spent'].sum().sort_index()
print(month_spent)

# %%

monthly_sales = df.groupby('month')['Total Spent'].sum().reset_index()

# Autumn coffee shop theme colors
line_color = '#8B4513'   # Dark coffee brown
marker_face = '#D2691E'  # Pumpkin spice orange
bg_color = "#FCFCFC"     # Creamy background
grid_color = "#ADADAD"   # Light caramel

plt.figure(figsize=(8,4), facecolor=bg_color)
plt.plot(monthly_sales['month'], monthly_sales['Total Spent'], 
         marker='o', linestyle='-', linewidth=2,
         color=line_color, markerfacecolor=marker_face, markeredgecolor='black')

# Titles and labels
plt.title("Monthly Sales Trend", fontsize=14, color=line_color)
plt.xlabel("Month", fontsize=12, color=line_color)
plt.ylabel("Total Sales", fontsize=12, color=line_color)


plt.show()




# %%
df[['Quantity', 'Price Per Unit', 'Total Spent']].describe()

# %%

df = df.dropna(subset=['Quantity', 'Price Per Unit', 'Total Spent'])
df[['Quantity', 'Price Per Unit', 'Total Spent']].isna().sum()

# %%
import matplotlib.pyplot as plt

df[['Quantity', 'Price Per Unit', 'Total Spent']].hist(
    figsize=(10, 6),
    bins=20,
    color='#D2691E',       
    edgecolor='brown',
    linewidth=1.2
)

plt.suptitle('Distribution of Numerical Variables' ,
             fontsize=16, fontweight='bold', color='#8B4513')
plt.tight_layout()
plt.show()


# %% [markdown]
# EDA PART2

# %% [markdown]
# 

# %%
Average_price_per_item = (
    df.groupby('Item')['Total Spent']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("TOP 10 ITEMS BY AVERAGE SPENT")
print(Average_price_per_item)



import matplotlib.pyplot as plt

# Top 10 average spent per item
Average_price_per_item = (
    df.groupby('Item')['Total Spent']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)


plt.figure(figsize=(8,5))
plt.barh(Average_price_per_item.index[::-1],
         Average_price_per_item.values[::-1],
         color='#A67B5B',  # single coffee color
         edgecolor='#3E2723', linewidth=1,
         height=0.45)

plt.title("Top 10 Items by Average Spent", fontsize=14, fontweight='bold', color='#4B2E05')
plt.xlabel("Average Total Spent", fontsize=12, color='#4B2E05')
plt.ylabel("Item", fontsize=12, color='#4B2E05')
plt.xticks(color='#4B2E05')
plt.yticks(color='#4B2E05')
plt.grid(axis='x', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()


# %%
total_quantity = df.groupby('Item')['Quantity'].sum().sort_values(ascending=False).head(10)
print(total_quantity)


# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.barh(total_quantity.index[::-1],
         total_quantity.values[::-1],
         color="#935E30",  # coffee single color
         height=0.45,
         edgecolor='#3E2723', linewidth=1)

plt.title("Top 10 Items by Quantity Sold", fontsize=14, fontweight='bold', color='#4B2E05')
plt.xlabel("Quantity Sold", fontsize=12, color='#4B2E05')
plt.ylabel("Item", fontsize=12, color='#4B2E05')
plt.xticks(color='#4B2E05')
plt.yticks(color='#4B2E05')
plt.grid(axis='x', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()



