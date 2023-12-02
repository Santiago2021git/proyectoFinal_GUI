from MODELO import Antibiotico
from CONTROLLER import CONTROLLER

registros_antibiotico = []


def crear_antibiotico(nombre_del_producto, dosis, precio):
    mi_antibiotico = Antibiotico.Antibiotico(nombre_del_producto, dosis, precio)
    registros_antibiotico.append(mi_antibiotico)
    CONTROLLER.retorno_interfaz_antibiotico()


def eliminar_antibiotico(producto):
    producto = producto.upper()
    tamaño = len(registros_antibiotico)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_antibiotico[eliminador]._nombre_del_producto.upper()
        if producto == eliminar:
            del registros_antibiotico[eliminador]
            break

        eliminador += 1
    CONTROLLER.retorno_interfaz_antibiotico()


def buscar_producto(producto):
    producto = producto.upper()
    tamaño = len(registros_antibiotico)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_antibiotico[buscador]._nombre_del_producto.upper()
        if producto == buscar:
            nombreb = registros_antibiotico[buscador]._nombre_del_producto
            dosisb = registros_antibiotico[buscador]._dosis
            tipo_animalb = registros_antibiotico[buscador]._tipo_de_animal
            preciob = registros_antibiotico[buscador]._precio
            CONTROLLER.antibiotico_encontrado(nombreb, dosisb, tipo_animalb, preciob)
            break

        buscador += 1

    if buscador == tamaño:
        CONTROLLER.antibiotico_no_encontrado()

    return registros_antibiotico[buscador]

