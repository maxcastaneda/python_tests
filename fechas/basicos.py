import datetime
#from datetime import datetime

mi_hora = datetime.time(17,35,45)
print(mi_hora)
print(mi_hora.minute)

mi_dia = datetime.date(2025,2,25)
print(mi_dia)
print(mi_dia.ctime())
print(mi_dia.year)
print(mi_dia.today())

mi_fecha = datetime.datetime(2025,2,25,17,35,45)
print(mi_fecha)
mi_fecha = mi_fecha.replace(year=2026)
print(mi_fecha)

nacimiento = datetime.date(1978,12,12)
edad = datetime.date.today() - nacimiento
print(edad.days)


#Ejercicio 1
mi_fecha = datetime.date(1999,2,3)

#Ejercicio 2
hoy = datetime.date.today()

#Ejercicio 3
hoy = datetime.datetime.today()
print(hoy.minute)