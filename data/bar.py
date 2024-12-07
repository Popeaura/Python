import matplotlib.pyplot as plt

x =['Apples', 'Bananas', 'Oranges']
y =[10, 7, 15]

plt.bar(x,y)
plt.xlabel('fruit')
plt.ylabel('Quantity')
plt.title('Bar chart of fruit quantities')
plt.show()