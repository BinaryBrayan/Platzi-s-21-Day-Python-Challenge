def get_student_average(students):
    averages={}#el diccionario final, el que pide la prueba
    prom_gen=0#promedio general de todos los estudiantes del salon
    prom_individual=0
    estudiantes=[]#lista que tiene name y average de cada estudiante
    
    for student in students:#se recorre cada estudiante del diccionario dado
        estudiante={}#se debe vaciar cada vez, sino todos los name y average los va a reemplazar
        #por el valor del ultimo student
        #se obtiene el promedio individual acumulado a partir de los grades de cada estudiante
        # y redondeando a 2 cifras decimales
        prom_individual+=(round(sum(student["grades"])/len(student["grades"]),2))
        #al diccionario estudiante se le agrega el nombre
        estudiante['name']=student['name']
        #luego se le agrega el promedio de sus notas, el average tambien redondeado a 2 cifras decimales
        estudiante['average']=round(sum(student["grades"])/len(student["grades"]),2)
        #print(estudiante)
        #a la lista estudiantes se le agrega el diccionario resultante estudiante, 
        # que tiene dos keys, name y average.
        estudiantes.append(estudiante)
    #print(estudiantes)
    #se obtiene el prom general de la suma de todos los promedios individuales, dividido en la longitud
    #del diccionario original pasado como parametro a la funcion
    prom_gen=round(prom_individual/len(students),2)
    #al dcit averages que es el final, primero se agrega el promedio de la clase como el primer par key:value
    averages['class_average']=prom_gen
    #luego al mismo dict final averages se agrega la lista estudiantes que es un dict con el par name:average
    averages['students']=estudiantes
    #se muestra el glorioso resultado
    return averages

if __name__ == '__main__':
    print(get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
]))
