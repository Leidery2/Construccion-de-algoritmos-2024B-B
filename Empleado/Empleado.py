__author__= "Leider Alexis Yela Gomez"
__license__= "GPL"
__version__= "1.0.0"
__email__= "leider.yela@campusucc.edu.co"

from Fecha import Fecha

class Empleado:
    # Aquí inicia la declaracion de la clase
    
    '''#----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------#'''
    
    nombre = ''
    apellido = ''
    salario = 0
    
    '''#----------------------------------------------------------------
    # 1 = Masculino, 2 = Femenino
    ----------------------------------------------------------------#'''
    
    sexo = 0
    
    '''#----------------------------------------------------------------
    # Asociación
    ----------------------------------------------------------------#'''
    
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()
    
    '''#----------------------------------------------------------------
    # Metodos 
    -----------------------------------------------------------------#'''
    # Este metodo retorna el nombre del empleado
    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre
    
    __method__ = "CambiarSalario"
    __parameter__ = "nuevoSalario"
    __returns__ = "Salario"
    __Description__ = " metodo que actualiza el salario del empleado"
    
    def CambiarSalario(self, nuevoSalario):    
        # Aqui va mi codigo
        self.salario = nuevoSalario
    
    __method__ = "DarSalario"
    __parameter__ = "Ninguno"
    __returns__ = "Salario"
    __Description__ = " metodo que Muestra el salario del empleado"
    # Retorna el salario del empleado
    def DarSalario(self):
        # Aqui va mi codigo
        return self.salario
    
    __method__ = "ConsultarFechaIngreso"
    __parameter__ = "Ninguno"
    __returns__ = "Fecha de ingreso"
    __Description__ = " metodo que muestra la fecha de ingreso del empleado"
    def ConsultarFechaIngreso(self):
        return self.fechaIngreso.DarFecha()
    
    __method__ = "CalcularSalarioAnual"
    __parameter__ = "Ninguno"
    __returns__ = "Salario anual"
    __Description__ = "Muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # Aqui va mi codigo
        # forma 1
        # total = self.salario*12
        # return total
        # forma 2
        return self.salario*12
    
    __method__ = "CalcularImpuestoSalarioAnual"
    __parameter__ = "Ninguno"
    __returns__ = "Impuesto del salario anual"
    __Description__ = "Muestra el impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # Aqui inicia mi codigo
        # Forma 1
        # salarioAnual=self.CalcularSalarioAnual()
        # impuestoAnual=salarioAnual*0.19
        # return impuestoAnual
        # Forma 2
        return self.CalcularSalarioAnual()*0.19
    
    __method__ = "CalcularImpuestoSalario"
    __parameter__ = "Ninguno"
    __returns__ = "Impuesto del salario"
    __Description__ = "Muestra el impuesto del salario del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # Aqui inicia mi codigo
        return self.DarSalario()*0.19