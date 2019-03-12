from flask import Flask,request,render_template,Response,jsonify, url_for
import os
from werkzeug.utils import secure_filename
from FindAndPredict import MakePrediction
from FindAndPredict import FindOnGoogle
from recipe_scrapers import scrape_me

import Sorting
import WegmanAPI
import time
#from RecordingThread import Global_Frame
app = Flask(__name__)
CurrentCwd = os.getcwd()
Save_Folder = os.path.join(CurrentCwd,"Img")
import cv2
from VideoStreamThread import VideoThread
import time
from VideoStreamThread import returnGlobal_Frame
def gen(camera):
    while True:
        img = returnGlobal_Frame()
        #print(img)
        ret,jpg = cv2.imencode('.jpg',img)
        frame = jpg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def default():
    if request.method == "GET":
        #print(MakePrediction("tomato.jpeg"))

        return render_template("Website.html")

@app.route('/Video')
def VideoCamera():
    camera = cv2.VideoCapture(0)

    ThreadedItem = VideoThread(camera)
    ThreadedItem.start()
    time.sleep(40)
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
# <Variable> in a URL
@app.route('/Recipes', methods = ['GET','POST'])
def AcceptImage():
    #Init = time.time()
    #print(MakePrediction("tomato.jpeg"))
    try:
        if(request.method == "POST"):
            #print("Here")
            f = request.files['fileupload']
            filename = f.filename
            f.save(os.path.join(Save_Folder,secure_filename(f.filename)))
            CheckVal = request.form.get("Check")

            ActualObject = MakePrediction(filename)
            ListOfLink = FindOnGoogle(ActualObject)
            ValidSite = []
            counter = 0
            max = 0

            for Link in ListOfLink:
                try:
                    if(counter == 3):
                        break
                    ListofItem = scrape_me(Link).ingredients()
                    Time = scrape_me(Link).total_time()
                    Title = scrape_me(Link).title()

                    if(len(ListofItem) != 0):
                        Ingredient, Price = WegmanAPI.FormatData(ListofItem)
                        InsideLinkObj =[]
                        InsideLinkObj.append(Link)
                        InsideLinkObj.append(Ingredient)
                        InsideLinkObj.append(round(float(Price), 2))
                        InsideLinkObj.append(Time)
                        InsideLinkObj.append(Title)
                        ValidSite.append(InsideLinkObj)
                        counter +=1
                except:
                    print("Stupid Error")
            ValidSite =  Sorting.SortProperly(ValidSite,CheckVal)
            print("Got past ValidSite")
            for i in ValidSite:
                print(i, max)
                if len(i[1]) > max:
                    max = len(i[1])
            print("ValidSite indexing")
            for i in ValidSite:
                if len(i[1]) < max:
                    for j in range((max - len(i[1]))):
                        i[1].append(' ')
            print("ValidSite afterward")
            return render_template("Recipes.html",ActualObject = ActualObject,ListOfLink= ValidSite,CheckV = CheckVal)

        else:
            return "GTFO GET"
    except:
      return render_template("ErrorPage.html")






if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = Save_Folder
    app.run(debug=True,threaded=True)


