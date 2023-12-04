from UI import InterfazGrafica as IG
from CRUD import CRUD_cliente
from CRUD import CRUD_fertilizante
from CRUD import CRUD_antibiotico
from CRUD import CRUD_factura
from CRUD import CRUD_control_de_plagas


def retorno_interfaz():
    IG.escoger_opciones()


def llamar_interfaz_clientes():
    IG.print_options_cliente()


def retorno_encontrados_cliente(nombreb, cedulab, numero_de_facturasb):
    IG.impresion_encontrado(nombreb, cedulab, numero_de_facturasb)


def retorno_no_encontrados_cliente():
    IG.impresion_no_encontrados()


def crear_cliente(nombre, cedula):
    CRUD_cliente.crear_cliente(nombre, cedula)
    

def eliminar_cliente(cedula):
    CRUD_cliente.eliminar_cliente(cedula)


def buscar_cliente():
    cedula = IG.ingreso_busqueda()
    elcliente = CRUD_cliente.buscar_cliente(cedula)
    return elcliente


def crear_factura():
    fecha = IG.ingreso_de_datos_factura()
    return fecha


def elegir_productos_factura():
    opcion = IG.elegir_productos_factura()
    return opcion


def agregar_factura(clientes):
    CRUD_factura.agregar_factura_a_cliente(clientes)


def llamdo_interfaz_factura():
    IG.print_options_factura()


def crear_antibiotico(nombre, dosis, precio):
    CRUD_antibiotico.crear_antibiotico(nombre, dosis, precio)


def eliminar_antibiotico(producto):
    CRUD_antibiotico.eliminar_antibiotico(producto)


def buscar_antibioto():
    producto = IG.ingreso_datos_busqueda_antibiotico()
    elproducto = CRUD_antibiotico.buscar_producto(producto)
    return elproducto


def antibiotico_encontrado(nombreb, dosisb, tipo_animalb, preciob):
    IG.impresion_antibiotico_encontrado(nombreb, dosisb, tipo_animalb, preciob)


def antibiotico_no_encontrado():
    IG.impresion_antibiotico_no_encontrado()


def retorno_plagas():
    IG.print_options_plagas()


def crear_plagas(registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, periodo_de_carencia):
    CRUD_control_de_plagas.crear_pesticida(registro_ica, nombre_del_producto,
                                           frecuencia_de_aplicacion, valor_del_producto, periodo_de_carencia)


def eliminar_plagas(producto):
    CRUD_control_de_plagas.eliminar_pesticida(producto)


def buscar_plagas():
    producto = IG.ingreso_datos_busqueda_plaga()
    elproducto = CRUD_control_de_plagas.buscar_producto(producto)
    return elproducto


def retorno_plagas_encontrado(Registrob, Nombreb, Frecuenciab, Preciob, Periodob):
    IG.impresion_plaga_encontrado(Registrob, Nombreb, Frecuenciab, Preciob, Periodob)


def retorno_plagas_no_encontrado():
    IG.impresion_plaga_no_encontrado()


def retorno_fertilizante():
    IG.print_options_fertilizante()


def crear_fertilizante(registro_ica, nombre_del_producto, frecuencia_de_aplicacion,
                       valor_del_producto, fecha_de_ultima_aplicacion):
    CRUD_fertilizante.crear_fertilizante(registro_ica, nombre_del_producto, frecuencia_de_aplicacion,
                       valor_del_producto, fecha_de_ultima_aplicacion)


def eliminar_fertilizante(producto):
    CRUD_fertilizante.eliminar_fertilizante(producto)


def retorno_fertilizante_encontrado(registob, nombreb, frecuenciab, preciob, aplicacionb):
    IG.impresion_fertilizante_encontrado(registob, nombreb, frecuenciab, preciob, aplicacionb)


def retorno_fertilizante_no_encontrado():
    IG.impresion_fertilizante_no_encontrado()

def buscar_fertilizante():
    producto = IG.ingreso_datos_busqueda_fertilizante()
    elproducto = CRUD_fertilizante.buscar_producto(producto)
    return elproducto


def imprimir():
    registros_clientes = CRUD_cliente.registros_clientes
    contador = 0
    tamaño = len(registros_clientes)
    while contador <= tamaño - 1:
        print('*' * 50)
        print("nombre del cliente: ", registros_clientes[contador]._nombre)
        print("cedula: ", registros_clientes[contador]._cedula)

        contador_facturas = 0
        tamaño_facturas = len(registros_clientes[contador]._factura_cliente)
        while contador_facturas <= tamaño_facturas - 1:
            print('*' * 50)
            print("Datos de la Factura")
            print("fecha de la factura: ", registros_clientes[contador]._factura_cliente[contador_facturas]._fecha)
            print("valor de la compra: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                  ._valor_de_la_compra)

            contador_antibioticos = 0
            contador_fertilizantes = 0
            contador_pesticidas = 0
            tamaño_antibioticos = len(registros_clientes[contador]._factura_cliente[contador_facturas]._antibiotico)
            tamaño_fertilizanes = len(registros_clientes[contador]._factura_cliente[contador_facturas]._fertilizante)
            tamaño_pesticidas = len(registros_clientes[contador]._factura_cliente[contador_facturas]._plaga)

            while contador_antibioticos <= tamaño_antibioticos - 1:
                print('*' * 50)
                print("antibioticos")
                print("nombre del producto: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._nombre_del_producto)
                print("dosis(entre 400kg y 600kg): ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._dosis)
                print("tipo de animal: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._tipo_de_animal)
                print("precio: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._precio)

                contador_antibioticos += 1

            while contador_pesticidas <= tamaño_pesticidas - 1:
                print('*' * 50)
                print("productos de control : plagas")
                print("registro ica: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._registro_ica)
                print("nombre del producto: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._nombre_del_producto)
                print("frecuencia de aplicacion: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._frecuencia_de_aplicacion)
                print("valor del producto: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._valor_del_producto)
                print("periodo de carencia: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._periodo_de_carencia)

                contador_pesticidas += 1

            while contador_fertilizantes <= tamaño_fertilizanes - 1:
                print("           ")
                print("productos de control : fertilizantes")
                print("registro ica", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._registro_ica)
                print("nombre del producto", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._nombre_del_producto)
                print("frecuencia de aplicacion", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._frecuencia_de_aplicacion)
                print("valor del producto", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._valor_del_producto)
                print("fecha de ultima aplicacion: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._fecha_de_ultima_aplicacion)

                contador_fertilizantes += 1

            contador_facturas += 1

        contador += 1


def imprimir_clientes():
    registros_clientes = CRUD_cliente.registros_clientes
    contador = 0
    tamaño = len(registros_clientes)
    while contador <= tamaño - 1:
        mensaje_1 = ('*' * 50)
        mensaje_2 = ("nombre del cliente: ", registros_clientes[contador]._nombre)
        mensaje_3 = ("cedula: ", registros_clientes[contador]._cedula)

        contador += 1


def imprimir_antibiotico():
    registros_antibiotico = CRUD_antibiotico.registros_antibiotico
    tamaño = len(registros_antibiotico)
    contador = 0
    while contador <= tamaño - 1:
        print('*' * 50)
        print(f"Nombre del antibiotico: {registros_antibiotico[contador]._nombre_del_producto}")
        print(f"Dosis Recomendada: {registros_antibiotico[contador]._dosis}")
        print(f"Tipo de animal: {registros_antibiotico[contador]._tipo_de_animal}")
        print(f"Precio: {registros_antibiotico[contador]._precio}")
        print('*' * 50)

        contador += 1


def imprimir_fertilizante():
    registros_fertilizantes = CRUD_fertilizante.registros_fertilizantes
    tamaño = len(registros_fertilizantes)
    contador = 0
    while contador <= tamaño - 1:
        print('*' * 50)
        print(f"Registro ICA: {registros_fertilizantes[contador]._registro_ica}")
        print(f"Nombre del fertilizante: {registros_fertilizantes[contador]._nombre_del_producto}")
        print(f"Frecuencia de aplicacion: {registros_fertilizantes[contador]._frecuencia_de_aplicacion}")
        print(f"Precio: {registros_fertilizantes[contador]._valor_del_producto}")
        print(f"Fecha de ultima aplicacion: {registros_fertilizantes[contador]._fecha_de_ultima_aplicacion}")
        print('*' * 50)

        contador += 1


def imprimir_plagas():
    registros_pesticidas = CRUD_control_de_plagas.registros_pesticidas
    tamaño = len(registros_pesticidas)
    contador = 0
    while contador <= tamaño - 1:
        print('*' * 50)
        print(f"Registro ICA: {registros_pesticidas[contador]._registro_ica}")
        print(f"Nombre del fertilizante: {registros_pesticidas[contador]._nombre_del_producto}")
        print(f"Frecuencia de aplicacion: {registros_pesticidas[contador]._frecuencia_de_aplicacion}")
        print(f"Precio: {registros_pesticidas[contador]._valor_del_producto}")
        print(f"Periodo de carencia: {registros_pesticidas[contador]._periodo_de_carencia}")
        print('*' * 50)

        contador += 1

