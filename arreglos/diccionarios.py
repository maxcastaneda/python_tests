print("\n")

#declarar 
diccionario = { 'nombre' : 'Carlos', 'edad' : 22, 'direccion' : 'Colombia' }
print(type(diccionario))
print(diccionario)

# acceder a los valores del diccionario
print(diccionario['nombre'])
cliente = { 'nombre':'juan', 'apellido' : 'fuentes' , 'peso' : 88, 'altura' : 1.80 }
consulta= cliente['apellido']
print(consulta)

# para agregar elementos a un diccionarios 
# esto se referencian con la clave nueva aun que no exista
dic = {'c1':'aa', 'c2':'bb'}
dic['c3'] = 'cc'
print(dic)


print("\n")