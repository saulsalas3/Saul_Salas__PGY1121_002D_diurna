from Cita import *
import numpy as np
import random as rn

arreglo_cita = np.array([])
ciclo = True
def ingresar_cita(arreglo_cita):
    cita = Cita()
    c = False
    while c == False:
        c = cita.setCodigo_atencion(input("Ingrese Codigo de atencion: "))
    c = False
    while c == False:
        c = cita.setNombre(input("Ingrese nombre: "))
    cita.fecha = input("Ingrese fecha de atencion: ")
    c = False
    while c == False:
        c = cita.setDescripcion(input("Ingrese descripcion de atencion: "))
    c = False
    while c == False:
        try:
            c = cita.setCosto(int(input("Ingrese costo de atencion: ")))
        except:
            print("Formato no valida, ingrese solo numeros")
    return np.append(arreglo_cita, cita)





def buscar_cita(arreglo_cita):
    codigo = input("Ingrese codigo de atencion: ")
    flag = True
    for cita in arreglo_cita:
        if codigo == cita.codigo_atencion:
            flag = True
            print("Datos de la cita")
            print(f"Codigo: {cita.codigo_atencion}")
            print(f"Nombre: {cita.nombre}")
            print(f"Fecha: {cita.fecha}")
            print(f"Descripcion: {cita.descripcion}")
            print(f"Costo: ${cita.costo}")
            if cita.costo >= 45000:
                print(f"Acceso a masaje facial gratis: Si")
            else:
                print("Acceso a masaje facial gratis: No")
            break
    if flag == False:
        print("Cita no existe")



def lista_boleta(arreglo_cita):
    codigo = input("Ingrese codigo de atencion: ")
    flag = True
    for cita in arreglo_cita:
        if codigo == cita.codigo_atencion:
            flag = True
            print("Boleta de la cita")
            print(f"Codigo:                         {cita.codigo_atencion}")
            print(f"Nombre:                         {cita.nombre}")
            print(f"Fecha:                          {cita.fecha}")
            print(f"Descripcion:                    {cita.descripcion}")
            print(f"Costo:                          {cita.costo}")
            if cita.costo >= 45000:
                print(f"Acceso a masaje facial gratis: Si")
            else:
                print("Acceso a masaje facial gratis:  No")
            propina = rn.randint(100, 1000)
            print(f"Propina:                        {propina}")
            total = cita.costo + propina
            print(f"Total                           {total}")
            break
    if flag == False:
        print("Cita no existe")


def salir():
    print("Vuelva pronto")
    print("Saúl Salas")
    print("Python 3.11")
    ciclo = False




while ciclo:
    print("Peluqueria: Mechas locas")
    print("1) Grabar cita")
    print("2) Buscar cita")
    print("3) Imprimir atencion")
    print("4) Salir")
    try:
        op = int(input("Seleccione una opcion (1-4): "))
        match op:
            case 1:
                arreglo_cita=ingresar_cita(arreglo_cita)
            case 2:
                buscar_cita(arreglo_cita)
            case 3:
                lista_boleta(arreglo_cita)
            case 4:
                ciclo = salir()
            case _:
                print("Opcion no valida, seleccione (1-4)")
    except:
        print("Opcion no valida, seleccione (1-4)")
