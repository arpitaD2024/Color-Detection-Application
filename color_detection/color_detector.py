import cv2
import numpy as np
from sklearn.cluster import KMeans


class Color_Detector:

    def __init__(self, img):
        self.frame = img

    def find_dominant_color(self, k=4):
        read_image = cv2.imread(self.frame)
        image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
        pixels = image.reshape((-1, 3))
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(pixels)
        colors = kmeans.cluster_centers_
        labels, counts = np.unique(kmeans.labels_, return_counts=True)
        dominant_color = colors[np.argmax(counts)]
        dominant_color = dominant_color.astype(int)
        return dominant_color

    def get_color_name(self, rgb_color):
        color_name = self.closest_color(rgb_color)
        return color_name

    def closest_color(self, requested_color):
        colors = {
            "Red": (255, 0, 0), "Green": (0, 255, 0),
            "Blue": (0, 0, 255), "Yellow": (255, 255, 0),
            "Cyan": (0, 255, 255), "Magenta": (255, 0, 255),
            "White": (255, 255, 255), "Black": (0, 0, 0),
            "Gray": (128, 128, 128), "Orange": (255, 165, 0),
            "Pink": (255, 192, 203), "Purple": (128, 0, 128),
            "Brown": (165, 42, 42),
        }
        min_distance = float('inf')
        closest_color_name = None
        for color_name, color_value in colors.items():
            distance = np.sqrt(
                (color_value[0] - requested_color[0]) ** 2 +
                (color_value[1] - requested_color[1]) ** 2 +
                (color_value[2] - requested_color[2]) ** 2
            )
            if distance < min_distance:
                min_distance = distance
                closest_color_name = color_name

        return closest_color_name

