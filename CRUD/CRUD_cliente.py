from MODELO import Cliente
from CONTROLLER import CONTROLLER as C


registros_clientes = []


def crear_cliente(nombre, cedula):
    mi_cliente = Cliente.Cliente(nombre, cedula)
    registros_clientes.append(mi_cliente)
    C.llamar_interfaz_clientes()


def eliminar_cliente(cedula):
    tamaño = len(registros_clientes)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_clientes[eliminador]._cedula
        if cedula == eliminar:
            del registros_clientes[eliminador]
            break
        
        eliminador += 1
    C.llamar_interfaz_clientes()

def buscar_cliente(cedula):
    tamaño = len(registros_clientes)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_clientes[buscador]._cedula
        if cedula == buscar:
            nombreb = registros_clientes[buscador]._nombre
            cedulab = registros_clientes[buscador]._cedula
            numero_de_facturasb = len(registros_clientes[buscador]._factura_cliente)
            C.retorno_encontrados_cliente(nombreb, cedulab, numero_de_facturasb)
            break

        buscador += 1

    if buscador == tamaño:
        C.retorno_no_encontrados_cliente

    return buscador

