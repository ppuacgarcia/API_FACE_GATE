import cv2
import os
import numpy as np
class Training:
	def training(data_path):
		
		peopleList = os.listdir(data_path)
		print('Lista de personas: ', peopleList)

		labels = []
		facesData = []
		label = 0

		for nameDir in peopleList:
			personPath = data_path + '/' + nameDir
			print('Leyendo las imágenes')

			for fileName in os.listdir(personPath):
				print('Rostros: ', nameDir + '/' + fileName)
				labels.append(label)
				facesData.append(cv2.imread(personPath+'/'+fileName,0))
				
			label = label + 1
		face_recognizer = cv2.face.LBPHFaceRecognizer_create()
		face_recognizer.train(facesData, np.array(labels))
		face_recognizer.write('modeloLBPHFace.xml')
		print("Modelo almacenado...")