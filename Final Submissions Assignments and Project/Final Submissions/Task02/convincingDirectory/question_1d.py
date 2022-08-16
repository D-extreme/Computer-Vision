import cv2
import numpy as np
import matplotlib.pyplot as plt

# alpha is a, beta is b, gamma is c

fig_a = cv2.cvtColor(cv2.imread(r'../data/1.jpg'),cv2.COLOR_BGR2RGB)
fig_a_b = cv2.cvtColor(cv2.imread(r'../data/2.jpg'),cv2.COLOR_BGR2RGB)
fig_b_c = cv2.cvtColor(cv2.imread(r'../data/3.jpg'),cv2.COLOR_BGR2RGB)
fig_c = cv2.cvtColor(cv2.imread(r'../data/arch.jpg'),cv2.COLOR_BGR2RGB)

# Code to get image coordinates on matplotlib
plt.imshow(fig_a)
plt.show()

# Points obtained from plt.imshow()

points_a = np.float32([[1512, 171],[2949, 729],[1490, 2231],[3000, 2040]])   # P, Q, R, S
points_a_b = np.float32([[1322, 332],[3000, 611],[1307, 2003],[3030, 1886]])
points_b_c = np.float32([[926, 728],[2817, 376],[904, 2069],[2861, 2223]])
points_c = np.float32([[0, 0],[1200, 0],[0, 900],[1200, 900]])


# Mid Points
mid_points_a = np.float32([(points_a[0] + points_a[1])//2,    # MP of PQ
                         (points_a[0] + points_a[2])//2,   # MP of PR
                        (points_a[1] + points_a[3])//2,    # MP of QS
                         (points_a[2] + points_a[3])//2])   # MP of RS

mid_points_a_b = np.float32([(points_a_b[0] + points_a_b[1])//2,    # MP of PQ
                         (points_a_b[0] + points_a_b[2])//2,   # MP of PR
                        (points_a_b[1] + points_a_b[3])//2,    # MP of QS
                         (points_a_b[2] + points_a_b[3])//2])   # MP of RS

mid_points_b_c = np.float32([(points_b_c[0] + points_b_c[1])//2,    # MP of PQ
                         (points_b_c[0] + points_b_c[2])//2,   # MP of PR
                        (points_b_c[1] + points_b_c[3])//2,    # MP of QS
                         (points_b_c[2] + points_b_c[3])//2])   # MP of RS

mid_points_c = np.float32([(points_c[0] + points_c[1])//2,    # MP of PQ
                         (points_c[0] + points_c[2])//2,      # MP of PR
                         (points_c[1] + points_c[3])//2,      # MP of QS
                         (points_c[2] + points_c[3])//2])     # MP of RS

# Additional Segments
intermediate_segments_a = np.float32([(points_a[0] + mid_points_a[0])//2,   # P and MP of PQ
                                      (points_a[1] + mid_points_a[0])//2,   # Q and MP of PQ
                                      (points_a[0] + mid_points_a[1])//2,   # P and MP of PR
                                      (points_a[2] + mid_points_a[1])//2,   # R and MP of PR
                                      (points_a[1] + mid_points_a[2])//2,   # Q and MP of QS
                                      (points_a[3] + mid_points_a[2])//2,   # S and MP of QS
                                      (points_a[2] + mid_points_a[3])//2,   # R and MP of RS
                                      (points_a[3] + mid_points_a[3])//2])  # S and MP of RS

intermediate_segments_a_b = np.float32([(points_a_b[0] + mid_points_a_b[0])//2,   # P and MP of PQ
                                      (points_a_b[1] + mid_points_a_b[0])//2,   # Q and MP of PQ
                                      (points_a_b[0] + mid_points_a_b[1])//2,   # P and MP of PR
                                      (points_a_b[2] + mid_points_a_b[1])//2,   # R and MP of PR
                                      (points_a_b[1] + mid_points_a_b[2])//2,   # Q and MP of QS
                                      (points_a_b[3] + mid_points_a_b[2])//2,   # S and MP of QS
                                      (points_a_b[2] + mid_points_a_b[3])//2,   # R and MP of RS
                                      (points_a_b[3] + mid_points_a_b[3])//2])  # S and MP of RS


intermediate_segments_b_c = np.float32([(points_b_c[0] + mid_points_b_c[0])//2,   # P and MP of PQ
                                      (points_b_c[1] + mid_points_b_c[0])//2,   # Q and MP of PQ
                                      (points_b_c[0] + mid_points_b_c[1])//2,   # P and MP of PR
                                      (points_b_c[2] + mid_points_b_c[1])//2,   # R and MP of PR
                                      (points_b_c[1] + mid_points_b_c[2])//2,   # Q and MP of QS
                                      (points_b_c[3] + mid_points_b_c[2])//2,   # S and MP of QS
                                      (points_b_c[2] + mid_points_b_c[3])//2,   # R and MP of RS
                                      (points_b_c[3] + mid_points_b_c[3])//2])  # S and MP of RS


intermediate_segments_c = np.float32([(points_c[0] + mid_points_c[0])//2,   # P and MP of PQ
                                      (points_c[1] + mid_points_c[0])//2,   # Q and MP of PQ
                                      (points_c[0] + mid_points_c[1])//2,   # P and MP of PR
                                      (points_c[2] + mid_points_c[1])//2,   # R and MP of PR
                                      (points_c[1] + mid_points_c[2])//2,   # Q and MP of QS
                                      (points_c[3] + mid_points_c[2])//2,   # S and MP of QS
                                      (points_c[2] + mid_points_c[3])//2,   # R and MP of RS
                                      (points_c[3] + mid_points_c[3])//2])  # S and MP of RS


# Updating all the set of points into the 16 points mapping
points_a = np.concatenate((points_a, mid_points_a, intermediate_segments_a), axis=0)
points_a_b = np.concatenate((points_a_b, mid_points_a_b, intermediate_segments_a_b), axis=0)
points_b_c = np.concatenate((points_b_c, mid_points_b_c, intermediate_segments_b_c), axis=0)
points_c = np.concatenate((points_c, mid_points_c, intermediate_segments_c), axis=0)
# Function calls:


# alpha has images fig_a and fig_a_b, so he will give the matrix that maps fig_a_b to fig_a
def alpha():
    matrix, mask = cv2.findHomography(points_a_b, points_a)
    return matrix


def beta():
    matrix, mask = cv2.findHomography(points_b_c, points_a_b)
    return matrix


def gamma(fig_background,fig_insert):
    M1 = alpha()
    M2 = beta()
    M3, mask = cv2.findHomography(points_c, points_b_c)
    mask = np.ones_like(fig_insert)*255
    result = cv2.warpPerspective(fig_insert,M3,(fig_background.shape[1],fig_background.shape[0]))
    mask = cv2.warpPerspective(mask,M3,(fig_background.shape[1],fig_background.shape[0]))
    final_frame = np.where(mask,0,fig_background)
    final_frame = final_frame + result

    WarpedImage = cv2.warpPerspective(final_frame,np.matmul(M1,M2),(final_frame.shape[1],final_frame.shape[0]))
    return WarpedImage


final_image = gamma(fig_b_c,fig_c)
cv2.imwrite(r"../results/sequential_16_points.jpg",cv2.cvtColor(final_image,cv2.COLOR_BGR2RGB))
plt.imshow(final_image)
plt.show()
