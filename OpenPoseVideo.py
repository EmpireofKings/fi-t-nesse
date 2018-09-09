import cv2
import time
import numpy as np


class Analysis():
    def __init__(self, MODE = 'COCO', VIEW = 'FRONT', FILE_NAME='front.mp4'):
        
        self.MODE = MODE
        self.VIEW = VIEW
        self.FILE_NAME = FILE_NAME

        if MODE is "COCO":
            self.protoFile = "pose/coco/pose_deploy_linevec.prototxt"
            self.weightsFile = "pose/coco/pose_iter_440000.caffemodel"
            self.nPoints = 18
            self.POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

        elif MODE is "MPI" :
            self.protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
            self.weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
            self.nPoints = 15
            self.POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]



        self.need = []
        if (VIEW == 'side'):
            self.need = {1: 'N', 5: 'LS', 11 : 'LH', 12 : 'LK' ,13 : 'LA' }
        else:
            self.need = {1 : 'N',2 : 'RS' ,3: 'RE' ,4 : 'RW' ,5 : 'LS' ,6 : 'LE' ,7 : 'LW'} 



        self.inWidth = 368
        self.inHeight = 368
        self.threshold = 0.1

        self.maxY = 0
        self.minY = 1000000

        self.minDict = []
        self.maxDict = []

        self.maxFrame = None
        self.minFrame = None

    def put_in_dict(self, pointlist):
        dict = {}
        if self.MODE == 'COCO':
            for i in self.need.keys():
                dict[self.need[i]] = pointlist[i]

        if self.MODE == 'MPI':
            for i in self.need.keys():
                dict[self.need[i]] = pointlist[i]
        return dict

    
    def read_file(self):
        
        input_source = self.FILE_NAME
        cap = cv2.VideoCapture(input_source)
        hasFrame, frame = cap.read()

        #vid_writer = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))

        net = cv2.dnn.readNetFromCaffe(self.protoFile, self.weightsFile)
        count = 0
        while hasFrame:
            t = time.time()
            
            print(count)
            count +=1
            
            hasFrame, frame = cap.read()
            frameCopy = np.copy(frame)
            if not hasFrame:
                break


            frameWidth = frame.shape[1]
            frameHeight = frame.shape[0]

            inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (self.inWidth, self.inHeight),
                                      (0, 0, 0), swapRB=False, crop=False)
            net.setInput(inpBlob)
            output = net.forward()

            H = output.shape[2]
            W = output.shape[3]
            # Empty list to store the detected keypoints
            points = []
            isMax = False
            isMin = False
            for i in range(self.nPoints):

                # confidence map of corresponding body's part.
                probMap = output[0, i, :, :]

                # Find global maxima of the probMap.
                minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
                
                # Scale the point to fit on the original image
                x = (frameWidth * point[0]) / W
                y = (frameHeight * point[1]) / H

                if prob > self.threshold :
                    if(i in self.need.keys()): 
                        if (i != 1):
                            cv2.circle(frameCopy, (int(x), int(y)), 12, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
                       # cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

                        # Add the point to the list if the probability is greater than the threshold
                        points.append((int(x), int(y)))
                    else:
                        points.append(None)
                else :
                    points.append(None)
                # 11 is LS
                if i == 5:
                    if y > self.maxY:
                        isMax = True
                        self.maxY = y
                    elif y < self.minY:
                        self.minY = y
                        isMin = True

            if (isMax  == True):
                self.maxDict = self.put_in_dict(points)
                self.maxFrame = frameCopy
            if (isMin == True):
                self.minDict = self.put_in_dict(points)
                self.minFrame = frameCopy


            # # Draw Skeleton
            # for pair in POSE_PAIRS:
            #     partA = pair[0]
            #     partB = pair[1]

            #     if points[partA] and points[partB]:
            #         cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3, lineType=cv2.LINE_AA)
            #         cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            #         cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)


            # cv2.putText(frame, "time taken = {:.2f} sec".format(time.time() - t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
            # cv2.putText(frame, "OpenPose using OpenCV", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 0), 2, lineType=cv2.LINE_AA)
            # cv2.imshow('Output-Keypoints', frameCopy)
            #cv2.waitKey(1)
            # cv2.imshow('Output-Skeleton', frame)

        cv2.imwrite('OutputMax' + self.VIEW + '.png', self.maxFrame)
        cv2.imwrite('OutputMin'+ self.VIEW + '.png', self.minFrame)

        print(self.maxDict)
        print(self.minDict)
        #vid_writer.release()


# for pair in POSE_PAIRS:
#     partA = pair[0]
#     partB = pair[1]

#     if points[partA] and points[partB]:
#         cv2.line(neckMaxYImg, points[partA], points[partB], (0, 255, 255), 3, lineType=cv2.LINE_AA)
#         cv2.circle(neckMaxYImg, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
#         cv2.circle(neckMaxYImg, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
#         cv2.imwrite('muhjaypeg.jpg', neckMaxYImg)
