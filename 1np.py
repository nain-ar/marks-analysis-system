x=int(input(' how many subject marks you entered here?'))
marks_list=[]
for i in range(0,x):
    marks=int(input(f'{i+1} subject marks = '))
    marks_list.append(marks)

import numpy as np
arr=np.array(marks_list)
print(arr)

print('highest marks = ', np.max(arr))
print('lowest marks = ', np.min(arr))
print('average marks = ', np.average(arr))
print('total marks = ', np.sum(arr))
print('total percentage % = ', np.sum(arr)/x)
import matplotlib.pyplot as plt
plt.pie(x,labels='subject')
plt.show()