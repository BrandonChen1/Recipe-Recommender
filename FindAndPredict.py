import os;

from imageai.Prediction import ImagePrediction
from googlesearch import search
import cv2
from matplotlib import pyplot as plt
import time

Path = os.getcwd();
PredictModelPath = os.path.join(Path,"inception.h5")
#print(PredictModelPath);

"""Initialization code """
global prediction
prediction = ImagePrediction()
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(PredictModelPath)
#prediction.loadModel()

AllowedWeb = [" site:allrecipes.com ", "OR site:foodnetwork.com ","OR site:bbc.com "]



def MakePrediction(filename):

    Exe2 = os.path.join(Path,"Img")
    global prediction
    BeginTime = time.time()
    prediction.loadModel()
    EndTime = time.time()
    print("How long to load model", EndTime - BeginTime)

    Predicto, Prob = prediction.predictImage(os.path.join(Exe2,filename ))
    return Predicto[0]


def FindOnGoogle(ObjectName):
    query = ObjectName + " recipe "
    for n in AllowedWeb:
        query += n
    return search(query,stop = 2)


#print(MakePrediction("tomato.jpeg"))
