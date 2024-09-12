__author__= "Leider Alexis Yela Gomez"
__license__= "GPL"
__version__= "1.0.0"
__email__= "leider.yela@campusucc.edu.co"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
    __cuentaAhorros=CuentaAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        # total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        # return total
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorrros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        # Aqui inicia mi codigo
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)

    __method__ = "Ahorrar"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite pasar saldo de la cuenta corriente a la cuenta de ahorros"
    
    def Ahorrar(self):
        # verificar si hay suficientes fondos en la cuenta corriente
        if self.__cuentaCorriente.DarSaldo() >= self.__cuentaAhorros.DarSaldo():
            self.__cuentaCorriente.RetirarSaldo(self.__cuentaAhorros.DarSaldo())
            self.__cuentaAhorros.ConsignarSaldo(self.__cuentaAhorros.DarSaldo())
        else:
            print("No hay suficientesw fondos en la cuenta corriente para ahorrar")
        
    __method__ = "retirarAhorro"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que Permite retirar el ahorro de la cuenta"
    
    def retirarAhorro(self,monto):
        #verificar si hay suficientes fondos en la cuenta de ahorros
        if self.__cuentaAhorros.DarSaldo() >= monto:
            self.__cuentaAhorros.RetirarSaldo(monto)
    
    __method__ = "darSaldoCorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite retornar el saldo que hay en la cuenta corriente"
    
    def darSaldoCorriente(self):
        # Aqui inicia mi codigo
        return self.__cuentaCorriente.DarSaldo()
        
    __method__ = "retirarTodo"
    __parameter__ = "Monto"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que retirar el saldo total actual en todas las cuentas"
    
    def retirarTodo(self,monto):
        # Aqui inicia mi codigo
        saldo_total = sel.CalcularSaldoTotal()
        self.__cuentaCorriente.RetirarSaldo(self.__cuentaCorriente.DarSaldo())
        self.__cuentaAhorros.RetirarSaldo(self.__cuentaAhorros.DarSaldo())
        
    __method__ = "duplicarAhorro"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite duplicar el dinero que hay en la cuenta de ahorros"
    
    def duplicarAhorro(self):
        saldo_ahorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.ConsignarSaldo(saldo_ahorros)