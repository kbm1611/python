import numpy as np

# CSV 파일 로드
data = np.genfromtxt('./day11/customer_purchase_data.csv', delimiter=",", skip_header=1)

# 데이터 구조 확인: [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]
print(f"데이터 형태:{data.shape}")

# Step 1
sales = data[:, -1]
print( np.mean( sales) )
print( np.sum( sales ) )

# Step 2
loyalCustomer = data[(data[:, 1] > 20) | (data[:,4] > 2000), :]
print( loyalCustomer[:, 0])

# Step 3
visits = data[:, 1]
ARPV = np.where(visits != 0, (sales / visits) , 0)
print( data[ARPV == np.max( ARPV ), 0])

# Step 4
cart_items = data[:, 3]
breakawayCustomer = data[(visits <= 3) & (cart_items <= 1), :]
print( breakawayCustomer.size )

# Step 5
Normalization = (sales - np.min(sales)) / (np.max(sales) - np.min(sales))
VVIP = data[Normalization >= 0.9, :]
print(VVIP)