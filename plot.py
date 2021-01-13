import matplotlib.pyplot as plt
import numpy as np
points_num = 100 
points_x = np.zeros(points_num,dtype=float)
points_y = np.zeros(points_num,dtype=float)
for i in range(points_num):
    points_x[i] = min(max(np.random.normal(loc=0.4, scale=0.5),-1.1),1.8)
    points_y[i] = min(max(np.random.normal(loc=0.4, scale=0.5),-1.2),1.6)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.scatter(points_x, points_y, alpha=0.6)  
#lt.show()
plt.savefig("test.png", dpi=120)
