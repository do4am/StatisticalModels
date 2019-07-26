import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16,9]

# reading data
data = pd.read_csv('GDPGermany.csv')
print(data.shape)

# collecting x and y
X = data['Year']
Y = data['GDP(usd)']

# mean x (since Linear Regression)
mean_x = np.mean(X)
mean_y = np.mean(Y)

# calculating regression line (y = ax + b) of GDP per year
# calculating coefficients a and b
m = len(X)

# formula
numer = 0
denom = 0

for i in range(m):
    numer += (X[i] - mean_x)*(Y[i] - mean_y)
    denom += (X[i] - mean_x)**2
a = numer/denom
b = mean_y - (a*mean_x)

print(a,b)

# plotting
max_x = np.max(X) + 1
min_x = np.min(X) - 1

# interpolating more value
x = np.linspace(min_x, max_x, 1000)
y = a*x + b

plt.plot(x, y, color='r', label = 'Regression Line')
plt.scatter(X, Y, c='b', label = 'Scatter Plot')

plt.xlabel('Years')
plt.ylabel('GDP(usd)')
plt.grid()
plt.xticks(range(X.min(), (X.max()+3), 3), range(X.min(), X.max()+3, 3))
plt.legend()
plt.show()

