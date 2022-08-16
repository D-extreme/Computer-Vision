import numpy as np
import cv2

# Proposed RMSE
def rmse_1(image_1,image_2):
    return np.mean((image_1-image_2)**2)

# Suggested RMSE in the assignment
def rmse_2(image_1,image_2):
    return (np.mean(image_1) - np.mean(image_2))**2


print(" Solution to 1(c) ")
image_1 = cv2.imread(r'../results/image_perspect_1.jpg')
image_2 = cv2.imread(r'../results/sequential.jpg')

print("RMSE through our proposed formula: ", "{0:.4f}".format(rmse_1(image_1,image_2)))
print("Proposed Formula for RMSE: ", "np.mean((image_1-image_2)**2)")

print("RMSE through assignment formula: ","{0:.4f}".format(rmse_2(image_1,image_2)))
print("Formula for RMSE suggested in assignment: ", "(np.mean(image_1) - np.mean(image_2))**2")

print("-------------------------------------------------------------------------------------")
print("Solution in 1(d)")
image_3 = cv2.imread(r'../results/sequential_16_points.jpg')

print("RMSE through our proposed formula: ", "{0:.4f}".format(rmse_1(image_2,image_3)))

print("RMSE through assignment formula: ","{0:.4f}".format(rmse_2(image_2,image_3)))