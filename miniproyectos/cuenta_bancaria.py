class Persona:
    def __init__(self, nombre, apellido):        
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance=balance

    def __str__(self):
        return f"""
Nombre del cliente: {self.nombre} {self.apellido}
Numero de cuenta: {self.numero_cuenta}
Balance Total: ${self.balance}
        """
    
    def depositar(self, monto):
        self.balance += float(monto)
        return f"Su saldo es ${self.balance}"

    def retirar(self, monto):
        if float(monto) > self.balance:
            return "Fondos insuficientes!"
        else:
            self.balance -= float(monto)
            return f"Su saldo es ${self.balance}"

# test
cliente = Cliente("max","castaneda","12345",200.0)
print(cliente)

while True:
    print ("""
Menu del banco:
[1] Depositar
[2] Retirar
[3] Saldo
[4] Salir
    """)
    opcion = input("Que opcion quieres?")
    match opcion:
        case "1" :
            print(cliente.depositar(input("Monto a depositar: ")))
        case "2" :
            print(cliente.retirar(input("Monto a retirar: ")))
        case "3" :
            print(cliente)
        case "4" :
            print("Hasta luego!")
            break
        case _:
            print("Opcion no valida!")