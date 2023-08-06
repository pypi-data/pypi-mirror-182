import numpy as np
import math
import matplotlib.pyplot as plt

class Canopy:
    dataset = []
    t1 = 0
    t2 = 0

    def __init__(self, dataset, t1, t2):
        self.dataset = dataset
        self.t1 = t1
        self.t2 = t2

    def euclidean_distance(self, point1, point2):
        return math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

    def get_index(self):
        return np.random.randint(len(self.dataset))

    def find_cluster_by_canopy(self):
        canopy_cluster = []
        while(len(self.dataset) != 0):
            center_set = []
            delete_set = []
            index = self.get_index()
            center_point = self.dataset[index]
            self.dataset = np.delete(self.dataset, index, 0)
            for i in range(len(self.dataset)):
                point = self.dataset[i]
                distance = self.euclidean_distance(point, center_point)
                if distance < self.t1:
                    center_set.append(point)
                if distance < self.t2:
                    delete_set.append(i)
            self.dataset = np.delete(self.dataset, delete_set, 0)
            canopy_cluster.append((center_point, center_set))
            canopy_cluster = [cluster for cluster in canopy_cluster if len(cluster[1]) > 1]
        return canopy_cluster

class KMeans:
    dataset = []
    center_pointset = []
    K = 0

    def __init__(self, dataset, center_pointset, K):
        self.dataset = dataset
        self.center_pointset = center_pointset
        self.K = K

    def euclidean_distance(self, point1, point2):
        return math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

    def set_euclidean_distance(self, set1, set2):
        if len(set1) == 0 or len(set2) == 0:
            return 1
        flag = 0
        for i in range(len(set1)):
            if self.euclidean_distance(set1[i], set2[i]) != 0:
                flag = 1
                break
        return flag

    def find_center_point(self, list):
        xsum = 0
        ysum = 0
        length = len(list)
        for data in list:
            xsum += data[0]
            ysum += data[1]
        return [xsum // length, ysum // length]

    def find_cluster_by_kmeans(self):
        kmeans_clusters = []
        count = 0
        old_center_pointset = self.center_pointset
        new_center_pointset = []
        flag = self.set_euclidean_distance(old_center_pointset, new_center_pointset)
        while count < 50 and flag != 0:
            if count != 0:
                old_center_pointset = new_center_pointset
            kmeans_clusters = [[] for _ in range(self.K)]
            for data in self.dataset:
                dist = []
                for i in range(len(old_center_pointset)):
                    distance = self.euclidean_distance(data, old_center_pointset[i])
                    dist.append(distance)
                kmeans_clusters[dist.index(min(dist))].append(data.tolist())
            count += 1
            new_center_pointset = []
            for cluster in kmeans_clusters:
                new_center_pointset.append(self.find_center_point(cluster))
            flag = self.set_euclidean_distance(old_center_pointset, new_center_pointset)
            print("更新后的中心点集：", end=" ")
            print(new_center_pointset)
        return new_center_pointset, kmeans_clusters



plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

class Visualization:
    center_points = []
    kmeans_cluster = []

    def __init__(self, center_points, kmeans_cluster):
        self.center_points = center_points
        self.kmeans_cluster = kmeans_cluster

    def format_point(self):
        lenth = len(self.kmeans_cluster)
        x_center_point = []
        y_center_point = []
        x_points = [[] for _ in range(lenth)]
        y_points = [[] for _ in range(lenth)]
        for center_point in self.center_points:
            x_center_point.append(center_point[0])
            y_center_point.append(center_point[1])
        for points in range(lenth):
            for point in self.kmeans_cluster[points]:
                x_points[points].append(point[0])
                y_points[points].append(point[1])
        return x_center_point, y_center_point, x_points, y_points

    def visual(self):
        x_center_point, y_center_point, x_point, y_point = self.format_point()
        fig, ax = plt.subplots()
        colors = ['#FFB6C1','#DC143C','#FF00FF','#800080','#4B0082','#6A5ACD',
                  '#0000FF','#6495ED','#778899','#1E90FF','#B0E0E6','#00FFFF',
                  '#008B8B','#48D1CC','#00FA9A','#2E8B57','#FFFF00','#BDB76B',
                  '#DAA520','#FFA500','#FF8C00','#000000','#808080','#8B0000',]
        for i in range(len(x_point)):
            ax.scatter(x_point[i], y_point[i], c=colors[i])
        ax.scatter(x_center_point, y_center_point, marker='*', s=200, c='black')
        plt.show()



