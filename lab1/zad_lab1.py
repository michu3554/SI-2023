import numpy as np

# 3)
# loading chosen system
diabetes = np.loadtxt("diabetes.txt")
diabetes_type = np.loadtxt("diabetes-type.txt", dtype=str)

# a)
# available decision classes
print(np.unique(diabetes[:, 8]))

# b)
# number of objects in classes
print(len(diabetes))

# c)
# min and max values for each attribute
for i in range(8):
    print(i, "min = ", np.min(diabetes[:, i]))
    print(i, "max = ", np.max(diabetes[:, i]))

# d)
# number of different values for each attribute
for i in range(8):
    print(i, len(np.unique(diabetes[:, i])))

# e)
# list of all different values for each attribute
for i in range(8):
    print(i, np.unique(diabetes[:, i]))

# f)
# standard deviation for each attribute in the whole system and separately for each decision class
for i in range(9):
    print(i, np.std(diabetes[:, i])


# 4)
