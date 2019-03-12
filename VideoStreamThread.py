from  threading import Thread
import cv2
from imageai.Detection import VideoObjectDetection
import os
global Global_Frame
import time
Path = os.getcwd()
VideoPath = os.path.join(Path,"VideoProcessing")
ModelPath = os.path.join(Path,"yolo.h5")
global BeginTime
#print(Path)
def returnGlobal_Frame():
    global Global_Frame
    return Global_Frame


def showCV(frame_number, output_array, output_count, returned_frame):
    #print(frame_number, output_array, output_count)
    global Global_Frame
    Global_Frame = returned_frame
    #print(returnGlobal_Frame())
    #print(Global_Frame)

    #cv2.imshow('frame', returned_frame)
    #cv2.waitKey(10)
class VideoThread(Thread):
    opencvCamera = None;
    ShouldClose = False
    Video_Detect = None
    OutPath = VideoPath
    #OutPath = r"C:\Users\JackXu\PycharmProjects\untitled\VideoProcessing"
    def __init__(self,CameraObj):
        Thread.__init__(self)
        self.opencvCamera = CameraObj




    def run(self):
        if (self.ShouldClose) == True:
            self.exit()
        else:
            self.Video_Detect = VideoObjectDetection()
            self.Video_Detect.setModelTypeAsYOLOv3()
            #BeginTime = time.time()
            self.Video_Detect.setModelPath(ModelPath)
            #EndTime = time.time()
            #print(" How long to set and load", EndTime - BeginTime)
            #self.Video_Detect.setModelPath(r"C:\Users\JackXu\PycharmProjects\untitled\yolo.h5")
            self.Video_Detect.loadModel("fastest")
            self.Video_Detect.detectObjectsFromVideo(camera_input= self.opencvCamera,return_detected_frame=True,
                                                     output_file_path=VideoPath,
                                                      frames_per_second=30,
                                                     minimum_percentage_probability=40,
                                                     per_frame_function=showCV, save_detected_video=False)
            self.ShouldClose = True








