import cv2
import numpy as np

#load yoshiiiii
img = cv2.imread("yoshi.png")
#cv2.imshow("image", img)

height, width, channels = img.shape
print(f"Breite: {width} pixels")
print(f"Hohe: {height} pixels")
print(f"Anzahl der Farbkanale: {channels}")

#to flieskommazahl
imgFloat = img.astype(np.float32)

height, width, _ = img.shape
center_x, center_y = width // 2, height // 2

topLeft = (center_x - 5, center_y + 5)
bottomRight = (center_x + 5, center_y - 5)

#jede 5. zeile schwarz machen
for column in range(0, height):
    if column % 5 == 0:
        for row in range(0, width):
            img[column, row] = [0, 0, 0]

color = (0, 0, 255)
thickness = -1
cv2.rectangle(img, topLeft, bottomRight, color, thickness)
cv2.imshow("img with red square", img)

#save
save_path = "yoshi_with_black_lines_and_red_square.png"
cv2.imwrite(save_path, img)

cv2.waitKey(0)
cv2.destroyAllWindows()