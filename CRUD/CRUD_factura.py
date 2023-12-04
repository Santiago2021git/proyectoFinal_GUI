from MODELO import Factura
from CONTROLLER import CONTROLLER


def agregar_factura_a_cliente(clientes):
    factura_mi_cliente = crear_factura(CONTROLLER.crear_factura())
    cliente = CONTROLLER.buscar_cliente()
    clientes[cliente]._factura_cliente.append(factura_mi_cliente)
    CONTROLLER.llamdo_interfaz_factura()


def crear_factura(fecha):
    precio_factura = 0
    factura_mi_cliente = Factura.Factura(fecha)
    eleccion2 = 0
    while eleccion2 != 4:
        
        eleccion2 = CONTROLLER.elegir_productos_factura()
        
        if eleccion2 == 1:
            mi_antibiotico = CONTROLLER.buscar_antibioto()
            precio_factura = precio_factura + mi_antibiotico._precio
            factura_mi_cliente._antibiotico.append(mi_antibiotico)

        if eleccion2 == 2:
            mi_pesticida = CONTROLLER.buscar_plagas()
            precio_factura = precio_factura + mi_pesticida._valor_del_producto
            factura_mi_cliente._plaga.append(mi_pesticida)

        if eleccion2 == 3:
            mi_fertilizante = CONTROLLER.buscar_fertilizante()
            precio_factura = precio_factura + mi_fertilizante._valor_del_producto
            factura_mi_cliente._fertilizante.append(mi_fertilizante)

    factura_mi_cliente._valor_de_la_compra = precio_factura
    return factura_mi_cliente

