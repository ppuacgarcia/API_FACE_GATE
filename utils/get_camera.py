import cv2
import urllib.request
import numpy as np 
import os
import imutils
def stream(username, save_frames):
    url = 'http://192.168.172.19/cam-hi.jpg'
    win_name = 'ESP32 CAMERA'
    cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)
    
    # Crear una carpeta para almacenar los frames si no existe
    if not os.path.exists('frames'):
        os.makedirs('frames')
    
    frame_count = 0  # Contador de frames para nombrar las imágenes
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    while True:
        frame_response = urllib.request.urlopen(url)
        frame_np = np.array(bytearray(frame_response.read()), dtype=np.uint8)
        frame = cv2.imdecode(frame_np, -1)
        frame =  imutils.resize(frame, width=640)
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aux_frame = frame.copy()
        
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = aux_frame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            # Guardar el frame como una imagen en la carpeta 'frames'
            if save_frames:
                cv2.imwrite(f'data/{username}/frame_{frame_count}.jpg', frame)
                frame_count += 1
        # solo se muestra si se quiere
        # cv2.imshow(win_name, frame)

        tecla = cv2.waitKey(5) & 0xFF
        if tecla == 27:
            break

    cv2.destroyAllWindows()