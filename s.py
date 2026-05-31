import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
sns.set_theme(style='darkgrid')
x=np.linspace(0,10,100)
y=np.sin(x)
y1=np.cos(x)
plt.figure(figsize=(8,5))
data=pd.DataFrame({'x axis(time)':x,
                   'sin wave':np.sin(x),
                   'cosine wave':np.cos(x)})
sns.lineplot(x=x,y=y,label='sine wave',c='b',linewidth=2,linestyle='-')
sns.lineplot(x=x,y=y1,label='cosine wave',c='g',linewidth=2,linestyle='--')
plt.title('sine and cosine waves',fontsize=14,fontweight='bold')
plt.xlabel('x axis(time)',fontsize=12)
plt.ylabel('y axis(amptitude)',fontsize=12)
plt.show()