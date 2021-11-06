import random
import csv
import matplotlib.pyplot as plt


def distance(arr1, arr2):
    dimensions = len(arr1)
    sqr_sum = 0
    for i in range(dimensions):
        sqr_sum += (float(arr1[i]) - arr2[i]) ** 2
    return sqr_sum ** 0.5


m = 3
maximum_c = 7
costs = []

with open('data4.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
del data[-1]
dims = len(data[0])

# for row in data:
#     for i in range(maximum_c):
#         row.append(0)


for c in range(1, maximum_c):
    data_cluster = []
    sshit = [0] * c
    for i in range(len(data)):
        data_cluster.append(sshit)
    centeroids = []
    for i in range(c):
        tmp = []
        for j in range(dims):
            tmp.append(random.randrange(-10, 600, 1)) 
        centeroids.append(tmp)

    for rape in range(100):
        row_num = 0
        for row in data:
            for i in range(c):
                Denominator = 0
                main_dis = distance(row, centeroids[i])
                for j in range(c):
                    tmp_dis = distance(row, centeroids[j])
                    # main_dis = (((float(row[0]) - centeroids[i][0]) ** 2) + (
                    #         (float(row[1]) - centeroids[i][1]) ** 2)) ** 0.5  # Xk -Vi can be done with func
                    # for j in range(c):
                    #     tmp_dis = (((float(row[0]) - centeroids[j][0]) ** 2) + (
                    #             (float(row[1]) - centeroids[j][1]) ** 2)) ** 0.5  # Xk -Vj
                    Denominator += (main_dis / tmp_dis) ** (2 / (m - 1))
                if Denominator == 0:
                    data_cluster[row_num][i] = 1
                else:
                    data_cluster[row_num][i] = 1 / Denominator  
            row_num += 1

        for i in range(c):
            numerator_x = 0
            numerator_y = 0
            Denominator_all = 0
            for j in range(len(data)):
                numerator_x += (data_cluster[j][i] ** m) * float(data[j][0])
                numerator_x += (data_cluster[j][i] ** m) * float(data[j][1])
                Denominator_all += (data_cluster[j][i] ** m)
            centeroids[i][0] = numerator_x / Denominator_all
            centeroids[i][1] = numerator_y / Denominator_all

    j = 0
    for k in range(len(data)):
        for i in range(c):
            # j += (((float(row[0]) - centeroids[i][0]) ** 2) + (
            #         (float(row[1]) - centeroids[i][1]) ** 2)) * (row[dims + 2]) ** m
            j += (distance(data[k], centeroids[i]) ** 2) * data_cluster[k][i] ** m
    costs.append(j)
# x_axis = range(1, maximum_c)
# plt.plot(x_axis, costs)
# plt.show()
