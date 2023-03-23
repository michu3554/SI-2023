import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

years = np.array([2000, 2002, 2005, 2007, 2010])
years_reshaped = years.reshape((-1, 1))
percentages = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

model = LinearRegression().fit(years_reshaped, percentages)

print(f"Linear regression model: y = {model.intercept_}x + {model.coef_[0]}")

print("Enter year to calculate the unemployment rate: ")
year = int(input())
y = ((year * model.coef_) - (model.intercept_ * -1))
print(f"The unemployment rate in {year} will be {round(y[0], 3)}%.")

x = (12 + (model.intercept_ * -1)) / model.coef_

print(f"The percentage of unemployed people will exceed 12% in {round(x[0])}.")

plt.scatter(years, percentages)
plt.title("The percentage of unemployed people over the age of 25")
plt.xlabel("Year")
plt.ylabel("Percent")

z = np.polyfit(years, percentages, deg=1)
p = np.poly1d(z)
plt.plot(years, p(years), "r--")
plt.legend(['Data points', 'Linear regression'])
plt.show()
