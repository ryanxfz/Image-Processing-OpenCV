import cv2
import numpy as np

img_input = cv2.imread("FigSource.png")
img_target = cv2.imread("FigTarget.png")
img_mexico = cv2.imread("MexicoFilterTest.jpg")

img_input_LAB = cv2.cvtColor(img_input, cv2.COLOR_BGR2LAB)
img_target_LAB = cv2.cvtColor(img_target, cv2.COLOR_BGR2LAB)

input_L_channel, input_A_channel, input_B_channel = cv2.split(img_input_LAB)
target_L_channel, target_A_channel, target_B_channel = cv2.split(img_target_LAB)

def adjustChannels(input_channel, target_channel):
    #subtract mean
    input_mean = np.mean(input_channel)
    input_channel = input_channel - input_mean

    #standard deviation
    input_std = np.std(input_channel)
    input_channel = input_channel / input_std

    #multiply input and std target
    target_std = np.std(target_channel)
    input_channel = input_channel * target_std

    #add mittelwert of target zum input
    target_mean = np.mean(target_channel)
    input_channel = input_channel + target_mean

    return input_channel

adjusted_l = adjustChannels(input_L_channel, target_L_channel)
adjusted_a = adjustChannels(input_A_channel, target_A_channel)
adjusted_b = adjustChannels(input_B_channel, target_B_channel)

adjusted_lab = cv2.merge((adjusted_l, adjusted_a, adjusted_b))
adjusted_lab = np.clip(adjusted_lab, 0, 255)
adjusted_lab = adjusted_lab.astype(np.uint8)

adjusted_RGB = cv2.cvtColor(adjusted_lab, cv2.COLOR_LAB2BGR)

cv2.imshow("Original image", img_input)
cv2.imshow("Target image", img_target)
cv2.imshow("Adjusted Image", adjusted_RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()