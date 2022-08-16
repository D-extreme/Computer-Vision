import cv2
import numpy as np
import matplotlib.pyplot as plt

fig_1 = cv2.imread(r'../data/self1.jpeg')
fig_1 = cv2.resize(fig_1,(640,360))

# Code to get image coordinates on matplotlib

# plt.imshow(fig_1)
# plt.show()
#
# #Points obtained from plt.imshow()
#
points_1 = np.float32([[91,80],[247,71],[92,232],[238,269]])
cap = cv2.VideoCapture(r'../data/self_video.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
output_video = cv2.VideoWriter('../results/video_perspect_self.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (640,360))

count = 0

while (cap.isOpened()):
    ret,frame = cap.read()
    if ret == False:
        break

    if count == 0:
        frame_height,frame_width = frame.shape[0],frame.shape[1]
        points_2 = np.float32([[0,0],[frame_width,0],[0,frame_height],[frame_width,frame_height]])
        mask = np.ones_like(frame)*255
        count = count + 1
    Matrix = cv2.getPerspectiveTransform(points_2,points_1)
    result = cv2.warpPerspective(frame,Matrix,(fig_1.shape[1],fig_1.shape[0]))
    mask_1 = cv2.warpPerspective(mask,Matrix,(fig_1.shape[1],fig_1.shape[0]))
    final_frame = np.where(mask_1,0,fig_1)
    final_frame = final_frame + result
    #final_frame = cv2.resize(final_frame,(640,360))
    if ret == True:
        cv2.imshow("MP4 Video",final_frame)
        output_video.write(final_frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
