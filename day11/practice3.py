import numpy as np

# 문제1
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print( np.concatenate( (x, y), axis = 0 ) )
print( np.concatenate( (x, y), axis = 1 ) )

# 문제2
x = np.array([3,1,2,5,4])
a = np.array([[3,1,2],[9,8,7]])
print( np.sort( x ))
print( np.sort( x )[::-1])
print( np.sort( a, axis = 0 ))
print( np.sort( a, axis = 1 ))

# 문제3
y = np.array(["철수", "영희", "민수", "영희"])
x = np.array([25, 30, 22, 24])
z = np.lexsort( (y, x) )
print( y[z] )
print( x[z] )

# 문제4
x = np.array([10,20,30,40,50])
print( x[ x > 30 ])
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print( x[ x > 5 ])

# 문제5
x1 = np.array([10, 20, 30, 40, 50])
print( np.where( x1 > 25, x1, -1 ))
print( np.where( x < 30 ))

# 문제6
x = np.array([1,2,3,4,5])
y = np.ma.array(x, mask = (x % 2 == 1) )
print( np.ma.sum( y ) )

# 문제7
x = np.array([10,20,30,40,50,60,70,80])
y = np.array([15,22,35,45,55,65,75,85])
con1 = x > 30
con2 = y < 50
print( x[ con1 & con2 ] )
print( y[ ~con2 ])

# 문제8
x = np.array([1,2,3,4,5])
print( np.max(x) )
print( np.sum(x) )
print( np.ptp(x) )

# 문제9
x2 = np.array([[1,2,3],[4,5,9]])
print( np.mean(x2) )
print( np.median(x2) )
print( np.std(x2, axis=0) )
print( np.var(x2, axis=1) )

# 문제10
x = np.array([10,20,30,40,50])
print( np.percentile(x, 25) )
print( np.percentile(x, 75) )
print( np.percentile(x, 75) - np.percentile(x, 25) )