import cv2
import os
import numpy as np
class Training:
	def training(data_path ,person_path):
		
		peopleList = os.listdir(data_path)
		print('Lista de personas: ', peopleList)

		labels = []
		facesData = []
		label = 0

		for nameDir in peopleList:
			
			print('Leyendo las imágenes')

			for fileName in os.listdir(person_path):
				print('Rostros: ', nameDir + '/' + fileName)
				labels.append(label)
				facesData.append(cv2.imread(person_path+'/'+fileName,0))
				
			label = label + 1
		face_recognizer = cv2.face.LBPHFaceRecognizer_create()
		face_recognizer.train(facesData, np.array(labels))
		face_recognizer.write('modeloLBPHFace.xml')
		print("Modelo almacenado...")