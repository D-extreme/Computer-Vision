import cv2
import numpy as np
import matplotlib.pyplot as plt

fig_1 = cv2.cvtColor(cv2.imread(r'../data/self1.jpeg'),cv2.COLOR_BGR2RGB)
fig_2 = cv2.cvtColor(cv2.imread(r'../data/self2.jpeg'),cv2.COLOR_BGR2RGB)
fig_3 = cv2.cvtColor(cv2.imread(r'../data/self3.jpeg'),cv2.COLOR_BGR2RGB)
fig_4 = cv2.cvtColor(cv2.imread(r'../data/self_image.jpg'),cv2.COLOR_BGR2RGB)

#Code to get image coordinates on matplotlib
# plt.imshow(fig_1)
# plt.show()

#Points obtained from plt.imshow()

points_1 = np.float32([[614,241],[598,889],[235,770],[227,258]])
points_2 = np.float32([[1127,212],[1094,883],[439,897],[402,204]])
points_3 = np.float32([[968,339],[954,846],[577,1048],[580,250]])
points_4 = np.float32([[fig_4.shape[1],0],[fig_4.shape[1],fig_4.shape[0]],[0,fig_4.shape[0]],[0,0]])

w,h = fig_1.shape[0],fig_1.shape[1]

#Making a mask:
mask = np.ones_like(fig_4)*255

#Image_1
Matrix_1 = cv2.getPerspectiveTransform(points_4,points_1)
result_1 = cv2.warpPerspective(fig_4,Matrix_1,(h,w))
mask_1 = cv2.warpPerspective(mask,Matrix_1,(h,w))


final_frame_1 = np.where(mask_1,0,fig_1)
final_frame_1 = final_frame_1 + result_1
#Image_2
Matrix_2 = cv2.getPerspectiveTransform(points_4,points_2)
result_2 = cv2.warpPerspective(fig_4,Matrix_2,(h,w))
mask_2 = cv2.warpPerspective(mask,Matrix_2,(h,w))

final_frame_2 = np.where(mask_2,0,fig_2)
final_frame_2 = final_frame_2 + result_2
#Image_3
Matrix_3 = cv2.getPerspectiveTransform(points_4,points_3)
result_3 = cv2.warpPerspective(fig_4,Matrix_3,(h,w))
mask_3 = cv2.warpPerspective(mask,Matrix_3,(h,w))

final_frame_3 = np.where(mask_3,0,fig_3)
final_frame_3 = final_frame_3 + result_3

figure = plt.figure(figsize=(10,7))

figure.add_subplot(1,3,1)
plt.imshow(final_frame_1)
plt.axis('off')

figure.add_subplot(1,3,2)
plt.imshow(final_frame_2)
plt.axis('off')

figure.add_subplot(1,3,3)
plt.imshow(final_frame_3)
plt.axis('off')

fig = plt.gcf()
fig.savefig('../results/image_perspective_self.jpg')
plt.show()
