__author__= "Leider Alexis Yela Gomez"
__license__= "GPL"
__version__= "1.0.0"
__email__= "leider.yela@campusucc.edu.co"

class Fecha:
    # Aquí inicia la declaracion de la clase
    
    '''#----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------#'''
    
    dia = 0
    mes = 0
    anio = 0
    
    __method__ = 'DarDia'
    __parameter__ = "ninguno"
    __returns__ = "Dia"
    __Description__ = "Metodo que regresa el dia"
    
    def DarDia(self):
        return self.dia
    
    __method__ = 'DarMes'
    __parameter__ = "ninguno"
    __returns__ = "Mes"
    __Description__ = "Metodo que regresa el Mes"
    
    def DarMes(self):
        return self.mes
    
    __method__ = 'DarAnio'
    __parameter__ = "ninguno"
    __returns__ = "Anio"
    __Description__ = "Metodo que regresa el año"
    
    def DarAnio(self):
        return self.anio
    
    __method__ = 'DarFecha'
    __parameter__ = "ninguno"
    __returns__ = "la fecha de la clase"
    __Description__ = "Metodo que regresa la fecha digitada por el usuario"
    
    def DarFecha(self):
        return self.dia+'/'+self.mes+'/'+self.anio