# declaracion 
mi_tuple = (1,2,3,4)
otro_tuple= 5,6,7,8
print(type(mi_tuple))
print(mi_tuple)
print(otro_tuple)

# acceder a los valores del tuple
print(mi_tuple[0])

# los tuples son inmutables
# mi_tuple[0] = 5 # esto falla

# puedo hacer casting entre tuples y listas:
mi_lista = list(mi_tuple)
mi_lista[0] = 5 # esto no falla
print(mi_tuple)
print(mi_lista)

# puedo hacer asignacion a multiples variables usando tuples, listas o diccionarios
# esto funciona solo si las variables son del mismo numero que el total de elementos del  tuple
tuple = (1,2,3)
x,y,z = tuple
print(x,y,z)