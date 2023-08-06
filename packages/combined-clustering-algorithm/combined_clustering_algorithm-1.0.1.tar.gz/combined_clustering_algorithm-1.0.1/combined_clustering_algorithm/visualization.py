import matplotlib.pyplot as plt

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
        colors = ['#FFB6C1', '#DC143C', '#FF00FF', '#800080', '#4B0082', '#6A5ACD',
                  '#0000FF', '#6495ED', '#778899', '#1E90FF', '#B0E0E6', '#00FFFF',
                  '#008B8B', '#48D1CC', '#00FA9A', '#2E8B57', '#FFFF00', '#BDB76B',
                  '#DAA520', '#FFA500', '#FF8C00', '#000000', '#808080', '#8B0000', ]
        for i in range(len(x_point)):
            ax.scatter(x_point[i], y_point[i], c=colors[i])
        ax.scatter(x_center_point, y_center_point, marker='*', s=200, c='black')
        plt.show()