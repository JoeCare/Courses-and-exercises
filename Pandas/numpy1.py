import numpy as np
import matplotlib.pyplot as plt

a = np.array([0,1,2,3,4])
print(type(a),a.dtype,a)
# a.size, a.ndim, a.shape

b = np.array([3.1,11.02,6.2,213.2,5.2])
type(b)
print(b.size, b.shape, b.ndim)

b[0] = 100.0
c = b[1:5]
print(type(c),c )
c[2:4] = 30.3, 400
d = np.array([c,[1,2,3,4]])
print(d)

# VECTOR ADDITION:
u = np.array([[1],
              [0]])
v = np.array([[0],
              [1]])
z = u + v
print(z)
# sum is linear combination of u and v
# where first component is
# the sum of first components
# and second - analogous
# 1+0 = [[1]  horizontal
# 0+1 =  [1]] vertical

# one the plane vector "u" first component
# indicates 1 unit from the origin
# in the horizontal direction (classic x-axis)
# second component is 0 so doesn't point
# in the vertical direction: arrow from origin
# stays at "x-axis"

# for vector "v" we would have vertically oriented
# arrow like y+1
# when we add those vectors we have new arrow
# pointing right between two previous components
# those are 2-dimensional vectors

z = [
    [1,0],
    [0,1]
]
print(z)

u = [1,0]
v = [1,0]
z = []
# multiple lines for lists:
for n,m in zip(u,v):
    z.append(n+m)
    print(z)

u = np.array([1,0])
v = np.array([1,0])
# one line for np.array:
z = u+v
print(f"Adding vecotrs: {z}")

# VECTOR MULTIPLICATION
# with Scalar

y = np.array([[1],
              [2]])
z = 2*y
print(f"Vector multiplication:\n{z}")

# HADAMARD PRODUCT: element[i,j] is product of [i.j] element of each matrix
u = np.array([[1],
              [2]])
v = np.array([[3],
              [2]])
z = u * v
print(f"Hadamard product:\n{z}")
# unlike matrix product it is cummulative - v * u = u * v
# matrix product for A[i,j]B[i,j] needs A[i] = B[j] (rows=columns)

# DOT PRODUCT:
u = np.array([1,2])
v = np.array([3,1])
z = np.dot(u,v)
print("Dot product:\n",z)

# BROADCASTING:
u = np.array([1,2,3,-1])
z = u+1
print(f"BROADCASTING: {z}")

# Universal functions (for ndarrays):
a = np.array([1,-1,1,-1])
mean = a.mean()
max = a.max()
print(f"Mean: {mean} "
      f"Max: {max}"
      f"")

y = [np.sin(0),np.sin(np.pi/2),np.sin(np.pi)]
print(f"Sinuses whateva: {y}")

# LINESPACE: (space of 9 evenly spaced numbers from -2 to 2)
l = np.linspace(0,2*np.pi,num=100)
print(f"Linespace:\n{l}")

# PLOTTING:
y = np.sin(l)
plt.plot(y)
plt.show()

