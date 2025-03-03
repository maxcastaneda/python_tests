import re
texto = """
En una lejana galaxia, el joven padawan Kael entrenaba bajo la tutela del maestro Jedi Sol-Dar en un templo oculto entre los anillos de un planeta helado. 
Un día, mientras exploraba unas antiguas ruinas, descubrió un holocrón Sith que susurraba secretos oscuros. 
La tentación fue grande, pero recordó las enseñanzas de su maestro y decidió entregarlo al Consejo Jedi. 
Sin embargo, un cazarrecompensas mandaloriano, contratado por un señor Sith, lo emboscó en su camino. 
Kael luchó con valentía, usando la Fuerza para esquivar disparos y desarmar a su enemigo sin recurrir al odio. 
Finalmente, el holocrón fue sellado en el templo Jedi y Kael aprendió que la verdadera fuerza de un Jedi no está en su sable, sino en su voluntad. 
Desde ese día, juró proteger la paz sin dejarse seducir por el lado oscuro.
"""

patron = "padawan"
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())

patron = r"(Kael|Jedi)\s(\w+)"
busqueda = re.findall(patron, texto)
for match in busqueda:
    print(match)

# Ejercicio 1
"""
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, 
que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) 
y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).
Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", 
pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
"""
def verificar_email(email):
    pattern = "\w+@\w+\.com?[\.\w+]"
    if re.match(pattern, email):
        return "Ok"
    else:
        return "La dirección de email es incorrecta"
""""
print(verificar_email("aaaa"))
print(verificar_email("hola@yo.com.br"))
print(verificar_email("hola@yo.xom"))
print(verificar_email("usuario@host.com"))
print(verificar_email("hola@yo.com.mx"))
"""

# Ejercicio 2
"""
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". 
Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", 
debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
"""

def verificar_saludo(frase):
    pattern = r"^Hola.*"
    if re.match(pattern, frase):
        print ("Ok")
    else:
        print ("No has saludado")

verificar_saludo("Hola como estas")
verificar_saludo("fsdfdsfdsf")

# Ejercicio 3
"""
Práctica Módulo RE 3
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). 
Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. 
Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
"""

def verificar_cp(cp):
    pattern = r"^\w{2}\d{4}$"
    if re.match(pattern, cp):
        print ("Ok")
    else:
        print ("El código postal ingresado no es correcto")

verificar_cp("AA1234")
verificar_cp("AA12345")
verificar_cp("A1234")
verificar_cp("XX1122")