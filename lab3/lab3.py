import numpy as np
from PIL import Image, ImageDraw


with open('DS9.txt', 'r') as file:
    lines = file.readlines()
points = [tuple(map(int, each.strip().split())) for each in lines]
alphaInRadians = np.radians(100)

canvas = Image.new("RGB", (1024, 1024), "white")
drawing = ImageDraw.Draw(canvas)

rotation = (480, 480)
rotation_matrix = np.array([[np.cos(alphaInRadians), -np.sin(alphaInRadians)],
                            [np.sin(alphaInRadians), np.cos(alphaInRadians)]])

transformedPoints = []
for point in points:
    pVector = np.array(point)-np.array(rotation)
    transformedPVector = np.dot(rotation_matrix, pVector)
    transformedP = tuple(np.round(transformedPVector + np.array(rotation)).astype(int))
    transformedPoints.append(transformedP)

point_color = (0, 0, 255)
for point in transformedPoints:
    drawing.point(point, fill=point_color)

new_size = (960, 960)
canvas = canvas.resize(new_size)
canvas.save("result.png")
canvas.show()
file.close()