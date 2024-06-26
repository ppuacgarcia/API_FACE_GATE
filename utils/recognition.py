import cv2
import os
import urllib.request
import numpy as np
from django.http import JsonResponse
class Recognition:
    def face_recognizer(data_path):
        #Cambia a la ruta donde hayas almacenado Data
        imagePaths = os.listdir(data_path)
        print('imagePaths=',imagePaths)
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('modeloLBPHFace.xml')
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        # url de la camara
        url = 'http://192.168.227.19/cam-hi.jpg'
        while True:
            try:
                img_response = urllib.request.urlopen(url)
                img_np = np.array(bytearray(img_response.read()), dtype=np.uint8)
                frame = cv2.imdecode(img_np, -1)
                frame = cv2.flip(frame, 0)  # Invertir verticalmente la imagen
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = gray.copy()

                faces = faceClassif.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                    result = face_recognizer.predict(rostro)

                    cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
                    # LBPHFace
                    if result[1] < 85:
                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                        cv2.destroyAllWindows()
                        return JsonResponse({'message': 'Usuario reconocido'})
                        
                    else:
                        
                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                        
                    
                cv2.imshow('frame',frame)
                k = cv2.waitKey(1)
                if k == 27:
                    break
            except Exception as e:
                return JsonResponse({'message': 'Usuario reconocido'})  
        cv2.destroyAllWindows()
        return JsonResponse({'message': 'Usuario reconocido'})  
