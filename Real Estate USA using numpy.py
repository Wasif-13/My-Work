# Real Estate By numpy

import numpy as np

brokered_by, price, city, zip_code = np.genfromtxt('RealEstate-USA.csv',delimiter=',',usecols=(0,2,7,9),unpack=True,dtype=None, skip_header=1)

print(brokered_by)
print(price)
print(city)
print(zip_code)

# Real Estate USA Statistics Opeartions

print("Real Estate USA Price mean",np.mean(price))
print("Real Estate USA Price median",np.median(price))
print("Real Estate USA Price average",np.average(price))
print("Real Estate USA Price std",np.std(price))
print("Real Estate USA percentile - 20",np.percentile(price,20))
print("Real Estate USA percentile - 55",np.percentile(price,55))
print("Real Estate USA Price min",np.min(price))
print("Real Estate USA Price max",np.max(price))

# Maths Opeartions

print('Real Estate USA Price square',np.square(price))
print("Real Estate USA Price sqrt",np.sqrt(price))
print("Real Estate USA Price pow",np.power(price,price))
print("Real Estate USA Price abs",np.abs(price))

# Arithmetic Operations

addition = price + brokered_by
subtraction = price + brokered_by
multiplication = price + brokered_by
division = price + brokered_by

print("Real Estate USA - Price-Brokered_by Addition",addition)
print("Real Estate USA - Price-Brokered_by Subtarction",subtraction)
print("Real Estate USA - Price-Brokered_by Multiplication",multiplication)
print("Real Estate USA - Price-Brokered_by Division",division)

# Trignometric Functions
pricepie = (price/np.pi)+ 1

sine = np.sin(pricepie)
cosine = np.cos(pricepie)
tangent = np.tan(pricepie)

print("Real Estate USA Price sin value",sine)
print("Real Estate USA Price cos value",cosine)
print("Real Estate USA Price tan value",tangent)
print("Real Estate USA Price exponential values",np.exp(pricepie))

# Real Estate USA 2 Dimentional Array

D2pricecity = np.array([price,
                 city])

print("Real Estate USA -price plus city- 2 Dimentional Array",D2pricecity)
print("Real Estate USA -price plus city- 2 Dimentional Array ",D2pricecity.ndim)
print("Real Estate USA -price plus city- 2 Dimentional Array - total number of elements",D2pricecity.size)
print("Real Estate USA -price plus city- 2 dimentional Array - gives size of array in each dimension",D2pricecity.shape)
print("Real Estate USA -price plus city- 2 Dimentional Array - data type",D2pricecity.dtype)

