import cv2
vidcap = cv2.VideoCapture('sample3.mp4')
success,image = vidcap.read()
count = 0
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


while success:
  if (count < 10):
  	print("writing")
  	cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success, 0)
  count += 1