x = int(input('How many subjects marks you want to enter? '))

marks_list = []
subject_list = []

for i in range(x):
    subject = input(f'Enter subject {i+1} name: ')
    marks = int(input(f'Enter {subject} marks: '))

    subject_list.append(subject)
    marks_list.append(marks)

import numpy as np

arr = np.array(marks_list)

print(arr)

print('Highest marks =', np.max(arr))
print('Lowest marks =', np.min(arr))
print('Average marks =', np.average(arr))
print('Total marks =', np.sum(arr))
print('Percentage =', np.sum(arr) / x)

import matplotlib.pyplot as plt

plt.bar(subject_list, marks_list,color='skyblue',label='self analysis')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject-wise Marks")
plt.grid(linestyle='--',linewidth=0.3,color='black',alpha=0.3)
plt.legend(shadow=True,edgecolor='black')
plt.show()