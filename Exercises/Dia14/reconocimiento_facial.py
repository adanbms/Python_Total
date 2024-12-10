import cv2
import face_recognition as fr

'''Cargar imagenes de referencia para reconocimiento facial'''
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

'''Pasar imagenes a RGB'''
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGRA2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGRA2RGB)

'''Localizar Cara control'''
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings()[0]

#Mostrar rectangulo en donde esta la cara
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0,255,0),
              2)

'''Localizar Cara prueba'''
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings()[0]

#Mostrar rectangulo en donde esta la cara
cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0,255,0),
              2)

'''Realizar Comparación
Si la coincidencia entre caras tiene una distancia de 0.6 o una definida entonces dara True
'''
resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B, 0.6)#ultimo dato es tolerancia de comparación de caras
print(resultado) #True porque el a misma persona

distancia = fr.compare_distance([cara_codificada_A],cara_codificada_B)

'''Mostrar Resultado'''
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,255,0),
            2)


'''Mostrar imagenes'''
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

'''Mantener programa abierto'''
cv2.waitKey(0)