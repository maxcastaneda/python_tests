lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"letra {numero_letra} es: {letra}")

# iterar lista de listas
for a,b in [[1,2],[3,4],[5,6]]:
    print(a,b)

#iterar diccionarios
dic={"a":1,"b":2,"c":3}
for item in dic: #itera llaves
    print(item)
for item in dic.values(): #itera valores
    print(item)
for item in dic.items(): #itera items
    print(item)    
for a,b in dic.items(): #itera items
    print(a,b)        

#rangos
for i in range(10):
    print(i)
for i in range(10,16,2):
    print(i)    
lista=list(range(2500,2586))
#print(lista)
mi_lista=list(range(3,3001,3))
#print(mi_lista)
suma_cuadrados=0
for i in range(1,16):
    suma_cuadrados = suma_cuadrados + i**2

#enumerador
lista=['a','b','c','d','e']
for indice,item in enumerate(lista):
    print(indice,item)
for item in enumerate(lista):
    print(item[0],item[1])  

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for item in enumerate(lista_nombres):
    indice = item[0]
    nombre = item[1]
    print(f'{nombre} se encuentra en el índice {indice}')

lista_indices = list(enumerate("Python"))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for item in enumerate(lista_nombres):
    if(item[1][0]=="M"):
        print(item[0])