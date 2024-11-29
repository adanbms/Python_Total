'''
--- Definición de la clase Pajaro ---
- Esta no tiene atributos ya que es una definición básica
- A cada varibale que genra una instancia de esta clase se le llama 'OBJETO'
- Podemos definir diferentes instancias de esta Clase, cada una de ellas vivirá en un espacio de memoria diferente
- El tipo de dato de los obejtos de esta clase será Pajaro
'''
class Pajaro:
    pass

mi_pajaro = Pajaro()
otro_pajaro = Pajaro()

#Son diferentes ya que utilizan diferentes espacios de memoria:
print(mi_pajaro) #<__main__.Pajaro object at 0x00000185B20FF8F0>
print(otro_pajaro) #<__main__.Pajaro object at 0x00000185B20FF920>

#Tipo de dato Pajaro
print(type(otro_pajaro)) #<class '__main__.Pajaro'>