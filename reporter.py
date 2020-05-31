def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF APRIL 2019...")

#import data 
import pandas as pd

url = 'https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/monthly-sales/sales-201904.csv'
df = pd.read_csv(url, error_bad_lines=False)

#create column for month and year of sales report
df['year'] = pd.DatetimeIndex(df['date']).year
#df['year'] = ['year'].apply(str)
df['month'] = pd.DatetimeIndex(df['date']).month
df['monthname'] = pd.to_datetime(df['month'], format='%m').dt.month_name()
#df['monthyear'] = df['monthname'] + df['year']

#get month name as variable
month = df.at[0,'monthname']
#get year as variable
year = df.at[0,'year']
#monthyear = df.at[0, 'monthyear']
#create revenue column = (units sold * sales price)
df["revenue"] = df["units sold"] * df["sales price"]
#sum revenue column
revenue = df["revenue"].sum() 

#print results
print("SALES REPORT" + ' ' +  "("+ str(month) + ' ' + str(year)+")")
#print("SALES REPORT"+ str(monthyear))
print("TOTAL SALES",to_usd(revenue))

#identify Top selling products:
#TOP SELLING PRODUCTS:
#  1. Button-Down Shirt: $6,960.35
#  2. Super Soft Hoodie: $1,875.00
#  3. etc.

#create new list of items with the max units sold
pdsales = df.groupby(['product']).sum()
#print(pdsales)
#sort them by top sellers
pdsalessorted = pdsales.sort_values(by=['units sold'], ascending=False)
print(pdsalessorted)
#iterate through and print the product name and total revenue
print("TOP SELLING PRODUCTS:")
for index, row in pdsalessorted.iterrows():
    print(row['product'], row['revenue'])

