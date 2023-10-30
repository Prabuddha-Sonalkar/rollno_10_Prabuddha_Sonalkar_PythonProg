#_____________line plot___________
"""
from matplotlib import pyplot as plt
x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.figure(figsize=(10,10))
plt.title("student chart")
plt.plot(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
"""

#___________Bar plot______________

'''from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[1,4,9,16,25]


plt.bar(x,y)
plt.show()'''

#___________3D graph______________

'''import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = plt.axes(projection='3d')
'''

#_____________numpy______________

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")
plt.show()


#_____________Pandas_________
'''
import pandas as pd 
import numpy as np 

ser = pd.Series() 
print("Pandas Series: ", ser) 
data = np.array(['g', 'e', 'e', 'k', 's']) 
ser = pd.Series(data) 
print("Pandas Series:\n", ser)
'''
'''
import pandas as pd 
import numpy as np 

ser = pd.DataFrame() 
print("Pandas DataFrame: ", ser) 
data = np.array(['g', 'e', 'e', 'k', 's']) 
ser= pd.DataFrame(data) 
print("Pandas Series:\n", ser)
'''
