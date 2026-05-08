import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanfont

df = pd.read_csv( './day15/train_HousePrices.csv' )
print( df.head() )  # 상위 5개 출력하여 데이터 있는 지 확인
print("데이터 정보")
df.info()   # 데이터 속성 타입 확인
print("--결측치--")
print( df.isnull().sum()[ df.isnull().sum() > 0 ] ) # 결측값 확인

# 4-1 수치형 변수 결측치 처리
# LotFrontage
# MasVnrArea
# GarageYrBlt
df['LotFrontage'] = df['LotFrontage'].fillna( df['LotFrontage'].median() )
df['MasVnrArea'] = df['MasVnrArea'].fillna( df['MasVnrArea'].median() ) 
df['GarageYrBlt'] = df['GarageYrBlt'].fillna( df['GarageYrBlt'].median() )  

# 4-2 범주형 변수 결측치 처리(정보 부재 명확)
# Alley
# PoolQC
# Fence
df['Alley'] = df['Alley'].fillna( 'NoAlley' )
df['PoolQC'] = df['PoolQC'].fillna( 'NoPoolQC' )
df['Fence'] = df['Fence'].fillna( 'NoFence' )

# 4-3 범주형 변수 결측치 처리(일반)
# BsmtQual
# BsmtCond
# BsmtExposure
# BsmtFinType1
# BsmtFinType2
# Electrical
# FireplaceQu
# GarageType
# GarageFinish
# GarageQual
# GarageCond
# MSZoning
# Functional
# SaleType
# Exterior1st
# Exterior2nd
# MasVnrType
target_cols = [
    'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
    'Electrical', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
    'GarageCond', 'MSZoning', 'Functional', 'SaleType', 'Exterior1st',
    'Exterior2nd', 'MasVnrType'
]

for col in target_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])

print( "결측치 처리 후") 
print( df.isnull().sum()[ df.isnull().sum() > 0 ] )

# 5. 데이터 시각화 및 분석
# 가설2. 주택의 스타일(HouseStyle)이나 외장재(Exterior1st)에 따라 가격 분포의 차이가 뚜렷할 것이다.
# 5-3. 주택 스타일별(HouseStyle) 가격(SalePrice) 분포 비교
sns.boxplot( data = df, x = 'HouseStyle', y = 'SalePrice')
plt.xlabel('주택 스타일')
plt.ylabel('판매 가격')
plt.show()


# 5-4. 주요 외관 요소별 가격 분포 비교
sns.boxplot( data = df, x = 'RoofStyle', y = 'SalePrice', hue='Exterior1st', gap = 0.5 )
# sns.boxplot( data = df, x = 'Exterior1st', y = 'SalePrice', gap = 0.5 )
# plt.xlabel('지붕 스타일 & 외장재')
# plt.ylabel('판매 가격')
plt.show()
