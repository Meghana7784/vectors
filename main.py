import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv("C:\...\cancer.csv")
a = np.array(x)
y  = a[:,30] # classes having 0 and 1
x = np.column_stack((x.malignant,x.benign))
x.shape 
print (x),(y)
