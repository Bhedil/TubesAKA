import matplotlib.pyplot as plt
#Isi data
x = [10, 100, 1000, 10000, 100000]
y1 = [0.048, 0.068, 0.200, 2.159, 35.427]
y2 = [0.045, 0.059, 0.198, 2.146, 31.808]
y = [0, 0.005, 0.5, 5, 50]
values = range(len(x))
#edit Plot line
plt.plot(values, y1, linestyle = 'solid', marker ='o', markersize = 8, label = 'Selection Sort' )
plt.plot(values, y2, linestyle = 'solid', marker = 'o', markersize = 8, label = 'Insertion Sort')
#Beri judul untuk graf
plt.title('Selection Sort vs Insertion Sort')
plt.xticks(values, x)
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
#Tampilkan graf
plt.show()

