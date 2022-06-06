import cv2
# select image
image = cv2.imread('100.png',1)
# window type
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# show window
cv2.imshow('image',image)
# wait for
key = cv2.waitKey(0)
# close all windows
if key == 27 :
      cv2.destroyAllWindows
elif key == ord('s'):
    cv2.imwrite('200.png', image)
    cv2.destroyAllWindows


