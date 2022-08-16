import cv2
import numpy as np
import matplotlib.pyplot as plt

# alpha is a, beta is b, gamma is c

fig_a = cv2.cvtColor(cv2.imread(r'../data/1.jpg'),cv2.COLOR_BGR2RGB)
fig_a_b = cv2.cvtColor(cv2.imread(r'../data/2.jpg'),cv2.COLOR_BGR2RGB)
fig_b_c = cv2.cvtColor(cv2.imread(r'../data/3.jpg'),cv2.COLOR_BGR2RGB)
fig_c = cv2.cvtColor(cv2.imread(r'../data/arch.jpg'),cv2.COLOR_BGR2RGB)

#Code to get image coordinates on matplotlib
# plt.imshow(c)
# plt.show()

#Points obtained from plt.imshow()

points_a = np.float32([[1512,171],[2949,729],[1490,2231],[3000,2040]])
points_a_b = np.float32([[1322,332],[3000,611],[1307,2003],[3030,1886]])
points_b_c = np.float32([[926,728],[2817,376],[904,2069],[2861,2223]])
points_c = np.float32([[0,0],[1200,0],[0,900],[1200,900]])

# Function calls:

#alpha has images fig_a and fig_a_b, so he will give the matrix that maps fig_a_b to fig_a
def alpha():
    points_a = np.float32([[1512,171],[2949,729],[1490,2231],[3000,2040]])
    points_a_b = np.float32([[1322,332],[3000,611],[1307,2003],[3030,1886]])
    matrix = cv2.getPerspectiveTransform(points_a_b,points_a)
    return matrix

def beta():
    points_a_b = np.float32([[1322,332],[3000,611],[1307,2003],[3030,1886]])
    points_b_c = np.float32([[926,728],[2817,376],[904,2069],[2861,2223]])
    matrix = cv2.getPerspectiveTransform(points_b_c,points_a_b)
    return matrix

def gamma(fig_background,fig_insert):
    points_b_c = np.float32([[926,728],[2817,376],[904,2069],[2861,2223]])
    points_c = np.float32([[0,0],[1200,0],[0,900],[1200,900]])
    M1 = alpha()
    M2 = beta()
    M3 = cv2.getPerspectiveTransform(points_c,points_b_c)
    mask = np.ones_like(fig_insert)*255
    result = cv2.warpPerspective(fig_insert,M3,(fig_background.shape[1],fig_background.shape[0]))
    mask = cv2.warpPerspective(mask,M3,(fig_background.shape[1],fig_background.shape[0]))
    final_frame = np.where(mask,0,fig_background)
    final_frame = final_frame + result

    WarpedImage = cv2.warpPerspective(final_frame,np.matmul(M1,M2),(final_frame.shape[1],final_frame.shape[0]))
    return WarpedImage



final_image = gamma(fig_b_c,fig_c)
cv2.imwrite(r"../results/sequential.jpg",cv2.cvtColor(final_image,cv2.COLOR_BGR2RGB))
plt.imshow(final_image)
plt.show()
