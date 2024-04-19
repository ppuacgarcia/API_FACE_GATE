import cv2
import numpy as np
import urllib.request
import imageio
import os
from utils.getframes import MakeFrames
# Definir una lista para almacenar los cuadros del video

class VideoCamera:
    
    def save_video(username):
        try:
            frames = []
            dataPath = './videos' #Cambia a la ruta donde hayas almacenado Data
            personPath = dataPath + '/' + username
            if not os.path.exists(personPath):
                print('Carpeta creada: ',personPath)
                os.makedirs(personPath)
            url = 'http://192.168.195.19/cam-hi.jpg'
            win_name = 'ESP32 CAMERA'
            cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)
            
            # Leer y mostrar los frames del video
            while True:
                img_response = urllib.request.urlopen(url)  
                img_np = np.array(bytearray(img_response.read()), dtype=np.uint8)
                img = cv2.imdecode(img_np, -1)  
                img = cv2.rotate(img, cv2.ROTATE_180) 
                # Convertir de BGR a RGB
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # Agregar la imagen a la lista de cuadros 

                cv2.imshow(win_name, img) 
                # Agregar la imagen a la lista de cuadros
                frames.append(img)
                MAX_FRAMES = 50
                print(len(frames))
                if len(frames) > MAX_FRAMES:
                    break
                # Esperar hasta que se presione ESC para terminar el programa
                
                tecla = cv2.waitKey(5) & 0xFF
                if tecla == 27:
                    break

            cv2.destroyAllWindows()
            output_file = personPath+'/video_salida.mp4'
            imageio.mimsave(output_file, frames, fps=20)
            frames = MakeFrames
            frames.makeFrames(username, "./data", output_file)
        except Exception as e:
            print(e)
            