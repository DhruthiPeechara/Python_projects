import matplotlib as plt 

blood_sugar_men = [113,89,87,90,100,80,83,95,106]
blood_sugar_women = [67,89,90,78,100,102,87,78,80]

type = [bllod_sugar_men,blood_sugar_women]

colors = ['g','r']

label = ['men', 'women']
bins = [80, 100, 125, 150]

plt.xlabel("Blood Sugar Range")
plt.ylabel("Total no. of patients")

plt.hist(blood_sugar_data, bins=bins, rwidth=0.95, color=colors,

label=label, orientation="horizontal")

plt.title("Blood Sugar Level Chart")

plt.legend()
plt.show()
