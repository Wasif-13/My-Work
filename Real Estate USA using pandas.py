
import pandas as pd

df = pd.read_csv("RealEstate-USA.csv", delimiter=',', parse_dates=[9], date_format={'date_added': '%d-%m-%Y'})

print(df)

print("Real Estate USA Describe()", df.describe())

# Display Last Three Rows
print("Last Three Rows")
print(df.tail(3))

# Display First Three Rows 
print("First Three Rows")
print(df.head(3))

# Counting The Rows and Columns in DataFrame using.shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting The Rows and Columns in DataFrame  ",df.shape)
print()

# access the name column
city = df['city']
print("access the name Column : df :")
print(city)
print()

# access multiple Columns
city_zip_code = df[["city","zip_code"]]
print("access multiple Columns : df : ")
print(city_zip_code)
print()

# selecting a single row using .loc 
second_row = df.loc[1]
print("Sececting a single row :")
print(second_row)
print()

# selecting multiple rows using .loc
second_row2 = df.loc[[1,3]]
print("Selecting multiple rows :")
print(second_row2)
print()

# selecting a slice of rows using .loc
second_row3 = df.loc[1:3]
print("Selecitng a slice of rows : ")
print(second_row3)
print()

# Conditional Selection of rows using .loc
second_row4 = df.loc[df['city'] == 'City']
print("Conditional Selection of rows :")
print(second_row4)
print()

# Selecting a single Column using .loc
second_row5 = df.loc[:1 , 'city'] 
print("Selecting a single Column :")
print(second_row5)
print()

# Selecting multiple Columns using .loc
second_row6 = df.loc[:1 ,[ 'city','price']]
print("Selecting multiple Columns :")
print(second_row6)
print()

# Selecting a slice of Columns using .loc
second_row7 = df.loc[:4, 'brokered_by': 'city']
print("Selecting slice of Columns :")
print(second_row7)
print()

# Combined selection of row and column using .loc
second_row8 =df.loc[df['status'] == 'for_sale', 'status': 'city']
print("Combined selection of row and column :")
print(second_row8)
print()

# using .loc with index col
df_index_col = pd.read_csv("RealEstate-USA.csv", delimiter=',', parse_dates=[9], date_format={'date_added': '%d-%m-%Y'}, index_col='brokered_by')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

# Selecting a single row using .loc
second_row = df_index_col.loc[103378]
print('# Selecting a single row using .loc')
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[103378, 52707]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

