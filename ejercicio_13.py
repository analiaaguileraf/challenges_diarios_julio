# challenge ---> Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo.


class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto

    def consultar_saldo(self):
        return self.saldo

cuenta = CuentaBancaria(200) 
print(f"Saldo inicial: {cuenta.consultar_saldo()}")  

cuenta.depositar(100)
print(f"Saldo después de depositar 100: {cuenta.consultar_saldo()}")  

cuenta.depositar(50)
print(f"Saldo después de depositar 50: {cuenta.consultar_saldo()}")  
