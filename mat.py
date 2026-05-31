import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)
y1=np.cos(x)
plt.figure(figsize=(8,5))
plt.plot(x,y,label='sine wave',color='b',linestyle='-',linewidth=2)
plt.plot(x,y1,label='cosine wave',color='g',linestyle='--',linewidth=2)
plt.title('sine and cosine waves',fontsize=14,fontweight='bold')
plt.xlabel('x axis(time)',fontsize=12)
plt.ylabel('y axis(amptitude)',fontsize=12)

#plt.axhline(50,c='g',linestyle='--',alpha=0.3)
#plt.axvline(35,c='b',linestyle='--',alpha=0.3)
plt.grid(True,linestyle=':',alpha=0.6)
plt.legend(loc='upper right')
plt.show()