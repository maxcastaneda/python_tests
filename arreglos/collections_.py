from collections import Counter, deque, defaultdict

serie = Counter([1,1,1,1,1,2,2,3,3,3,5,5])

print(serie.most_common()) # elementos unicos incluyendo cuantas veces aparecen
print(serie.total())
print(list(serie)) # elementos unicos

mi_dic = {'uno':'verde','dos':'rojo','tres':'azul','cuatro':'verde'}
print(mi_dic['cuatro'])
mi_ddic = defaultdict(lambda: 'nada')
mi_ddic['uno'] = 'verde'
print(mi_ddic['dos'])
print(dict(mi_ddic))


lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.append("Bogotá")
lista_ciudades.appendleft("Buenos Aires")
print(lista_ciudades)

