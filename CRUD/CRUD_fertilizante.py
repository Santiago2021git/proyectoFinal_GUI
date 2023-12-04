from MODELO import Fertilizantes
from CONTROLLER import CONTROLLER


registros_fertilizantes = []


def crear_fertilizante(registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto,
     fecha_de_ultima_aplicacion):
    mi_fertilizante = Fertilizantes.Fertilizante(registro_ica, nombre_del_producto, frecuencia_de_aplicacion,
                                   valor_del_producto, fecha_de_ultima_aplicacion)
    registros_fertilizantes.append(mi_fertilizante)
    CONTROLLER.retorno_fertilizante()


def eliminar_fertilizante(producto):
    producto = producto.upper()
    tamaño = len(registros_fertilizantes)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_fertilizantes[eliminador]._nombre_del_producto.upper()
        if producto == eliminar:
            del registros_fertilizantes[eliminador]
            break

        eliminador += 1
    CONTROLLER.retorno_fertilizante()


def buscar_producto(producto):
    producto = producto.upper()
    tamaño = len(registros_fertilizantes)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_fertilizantes[buscador]._nombre_del_producto.upper()
        if producto == buscar:
            registob = registros_fertilizantes[buscador]._registro_ica
            nombreb = registros_fertilizantes[buscador]._nombre_del_producto
            frecuenciab = registros_fertilizantes[buscador]._frecuencia_de_aplicacion
            preciob = registros_fertilizantes[buscador]._valor_del_producto
            aplicacionb = registros_fertilizantes[buscador]._fecha_de_ultima_aplicacion
            CONTROLLER.retorno_fertilizante_encontrado(registob, nombreb, frecuenciab, preciob, aplicacionb)
            break

        buscador += 1

    if buscador == tamaño:
        CONTROLLER.retorno_fertilizante_no_encontrado()

    return registros_fertilizantes[buscador]

