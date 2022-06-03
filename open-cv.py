import cv2
file = cv2.VideoCapture('tesl.mp4')
print('hi')
while(file.isOpened()):
      ret,frame = file.read()
      if ret == True:
            cv2.imshow('frame',frame)
            if file.waitKey(25) & 0xFF ==ord('q'):
                  break