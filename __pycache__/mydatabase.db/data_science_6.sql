import matplotlib as plt 

x1=[89,87,67,56,45,34,23,24,22,12]
y1=[68,57,35,28,90,17,89,90,60,57]

x2= [78,4,6,7,83,71,81,64,12,15,]
y2=y2 = [26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

plt.scatter(x1, y1, c="pink", linewidths=2, marker="s", edgecolor="green", s=50)

plt.scatter(x2, y2, c="yellow", linewidths=2, marker="^", edgecolor="red", s=200)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()



