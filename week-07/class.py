# 1. Import libraries
import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30, 20, np.nan])
print("Original Series:")
print(s)


print("\nSum:", s.sum())    
print("Mean:", s.mean())    
print("Max:", s.max())      
print("Min:", s.min())      

# 5. First three values
print("\nFirst 3 values:")
print(s.head(3))            

# 6. Find and replace missing values
print("\nMissing values:")
print(s.isnull())           
print("\nAfter fillna(0):")
print(s.fillna(0))          

# 7. Sort values
print("\nSorted:")
print(s.sort_values())    


# 8. Count repeated values
print("\nValue counts:")
print(s.value_counts())     