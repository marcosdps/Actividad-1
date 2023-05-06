#CLASE EMAIL
import re                                           #libreria que le añade el modulo al split para que podamos usarlo con multiples delimitadores

class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contra = ''

    #el __init__ que es el constructor, cuando se cree un objeto de la clase Email, va a inicializarse con esos valores que le llegan a los parametros formales
    def __init__(self, idCuenta, dominio, tipoDominio, contra):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contra = contra

    def ingresoDatos(self):
        """metodo para ingresar datos de email"""
        print('Ingrese los siguientes datos del Email: ')
        self.__idCuenta = input('ID: ')
        self.__dominio = input('Dominio: ')
        self.__tipoDominio = input('Tipo de dominio: ')
        self.__contra = input('Contraseña: ')


    def retornaEmail(self):
        """metodo que retorna el email completo"""
        #print('{}@{}.{}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio)) probando una forma de mostrar
        return self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDominio
    
    def getDominio(self):
        """metodo que devuelve el dominio ingresado"""
        return self.__dominio
    
    def crearCuenta(self):
        nombre = input("Ingrese el nombre de la persona: ")
        self.ingresoDatos()
        print(f"Estimado {nombre}, te enviaremos tus mensajes a la direccion {self.retornaEmail()}")

    def modificarContra(self):
        print("Sistema de modificacion de contraseña")
        contraActual = input("Ingrese contraseña actual: ")
        if contraActual == self.__contra:
            self.__contra = input("Ingrese la contraseña nueva: ")
        return self.__contra

    def agregoDatos(self, datos, contra, idcuenta):
        self.__contra = contra
        self.__dominio = datos[0]
        self.__idCuenta = idcuenta
        self.__tipoDominio = datos[1]

    def mostrarDatos(self):
        print("Idcuenta: ",self.__idCuenta, "; Dominio: ", self.__dominio, "; Tipo dominio: ", self.__tipoDominio, "; Contraseña: ", self.__contra)

    def tengoCorreo(self, correo):
        print("Para el correo ", correo)
        contra = input("Ingrese contraseña: ")
        datos = re.split('[@]',correo)           #Dentro de los corchetes, pongo los delimitadores que quiero que separe las palabras al encontrarlos, sin separacion ni nada, todos juntos
        idcuenta = datos[0]
        datos = re.split('[.]',datos[1-2])
        print(len(datos))                                   #me muestra la cantidad de elementos que tiene datos
        print(datos)
        #datosCompletos = (idcuenta,"@",datos[0],".", datos[1]) Una forma interesante de almacenar datos
        self.agregoDatos(datos, contra, idcuenta)   #ahora puedo almacenar los datos del correo en una instancia de clase Email

    def domCoincide(self, domIngresado):
        if self.__dominio == domIngresado:
            return 1
        else:
            return 0