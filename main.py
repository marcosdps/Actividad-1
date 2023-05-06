from clase import Email

import csv

def leerDatos(archi):
    reader = csv.reader(archi, delimiter= ",")
    for fila in reader:
        if fila[0].find("@") != -1:
            agregoObjetoEnLista(fila[0])
        else:
            print("ERROR EN EL EMAIL")

def agregoObjetoEnLista(correo):
    emailNuevo = Email("","","","")
    emailNuevo.tengoCorreo(correo)
    lista.append(emailNuevo)
    
def cuentoDominios():
    dom = input("Ingrese un dominio a buscar: ")
    cantidad = 0
    for i in range(len(lista)):
        cantidad += lista[i].domCoincide(dom)
    print(f"Hay {cantidad} emails con dominio coincidente al ingresado")
        
if __name__ == '__main__':
    lista = []
    unEmail = Email("","","","")           #lo que esta dentro de las comillas representa el valor con el que se van a inicializar los atributos del objeto, estos parametros se los lleva al init
    otroEmail = Email("","","","")
    #punto 1----------
    unEmail.crearCuenta()
    #punto 2----------
    unEmail.modificarContra()
    #punto 3----------
    nuevoCorreo = input('correo electronico: ')
    otroEmail.tengoCorreo(nuevoCorreo)
    #print('Dominio devuelto: ', unEmail.getDominio())
    unEmail.mostrarDatos()
    otroEmail.mostrarDatos()
    #punto 4----------
    with open ("listaEmails.csv") as archi:
        leerDatos(archi)
        print("cantidad de objetos en lista: ", len(lista))
        for i in range(len(lista)):
            lista[i].mostrarDatos()
    cuentoDominios()