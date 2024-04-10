import cv2
import os

def add_value_if_not_exists(value, array):
    if value not in array:  # Check if the value is not present in the array
        array.append(value)  # If not present, add the value to the array
    return array
        
def face_recognizer(data_path):
    data_path = './data'  # Cambia a la ruta donde hayas almacenado Data
    imagePaths = os.listdir(data_path)
    print('imagePaths=', imagePaths)
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('modeloLBPHFace.xml')
    cap = cv2.VideoCapture('./utils/pablo/Pablo.mp4')
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_found = False
    personas = []
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        

        for (x, y, w, h) in faces:
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
			
            cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
            # LBPHFace
            if result[1] < 70:
                personas = add_value_if_not_exists(imagePaths[result[0]], personas)
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1,
                            cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                face_found = True
                return personas
            else:
                cv2.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        
        k = cv2.waitKey(1)
        if k == 27:
            break

    if not face_found:
        # Si no se encontró ningún rostro conocido
        return False

    cap.release()
    cv2.destroyAllWindows()

print(face_recognizer('./data'),"   cara reconocida")