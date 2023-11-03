#%%
def insertion_sort(A,n):
    for i in range(n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

#%%
A = [5,2,4,6,1,3]
insertion_sort(A,len(A))
print(A)
# %%
import random
A = [random.randint(0,100) for i in range(100)]
insertion_sort(A,len(A))
print(A == sorted(A))
# %%
# Find and plot the growth rate of insertion sort
import time
import matplotlib.pyplot as plt
import numpy as np
t = []
for i in range(1,10**3):
    average = 0
    for j in range(100):
        A = np.random.randint(0, 100, i)
        n = len(A)
        start = time.time()
        insertion_sort(A, i)
        end = time.time()
        average += (end-start)/10
    t.append(average)
plt.plot(np.arange(n), t)
plt.show()
# %%
