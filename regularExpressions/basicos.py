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