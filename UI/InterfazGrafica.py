from CRUD import CRUD_cliente
from CRUD import CRUD_fertilizante
from CRUD import CRUD_antibiotico
from CRUD import CRUD_control_de_plagas
from CONTROLLER import CONTROLLER


def opciones():
    print("seleccione la opcion que corresponda al area al que desea ingresar:")
    print("1.REGISTRO DE CLIENTES")
    print("2.REGISTRO DE ANTIBIOTICOS")
    print("3.REGISTRO DE PESTICIDAS")
    print("4.REGISTRO DE FERTILIZANTES")
    print("5.FACTURACION")
    print("6.SALIR")
    opcion = int(input("su eleccion es la opcion: "))
    return opcion


def escoger_opciones():
    opcion = opciones()
    if opcion == 1:
        print_options_cliente()

    if opcion == 2:
        print_options_antibiotico()

    if opcion == 3:
        print_options_plagas()

    if opcion == 4:
        print_options_fertilizante()

    if opcion == 5:
        print_options_factura()

    if opcion == 6:
        pass


def print_options_cliente():
    print("REGISTROS DE CLIENTES ")
    print('*' * 50)
    print("[C]rear cliente")
    print("[L]istar clientes")
    print("[E]liminar cliente")
    print("[S]alir")
    run_cliente()
    

def run_cliente():
    command = input()
    command = command.upper()

    if command == 'C':
        ingreso_de_datos_cliente()
    elif command == 'L':
        imprimir_clientes(CRUD_cliente.registros_clientes)
    elif command == 'E':
        ingreso_datos_eliminar_cliente()
    elif command == 'S':
        escoger_opciones()
    else:
        print("comando invalido")
        run_cliente()


def ingreso_de_datos_cliente():
    nombre = (str(input("Ingrese el nombre del cliente: ")))
    cedula = (int(input("Ingrese la cedula del cliente: ")))
    CONTROLLER.crear_cliente(nombre, cedula)


def ingreso_datos_eliminar_cliente():
    cedula = int(input("ingrese la cedula del cliente que desea eliminar: "))
    CONTROLLER.eliminar_cliente(cedula)


def imprimir_clientes(registros_clientes):
    contador = 0
    tamaño = len(registros_clientes)
    while contador <= tamaño - 1:
        print('*' * 50)
        print("nombre del cliente: ", CRUD_cliente.registros_clientes[contador]._nombre)
        print("cedula: ", CRUD_cliente.registros_clientes[contador]._cedula)

        contador += 1
    print_options_cliente()

def print_options_factura():
    print("REGISTROS DE FACTURAS ")
    print('*' * 50)
    print("[C]rear factura")
    print("[L]istar facturas")
    print("[S]alir")
    run_factura()


def run_factura():
    command = input()
    command = command.upper()

    if command == 'C':
        CONTROLLER.agregar_factura(CRUD_cliente.registros_clientes)
    elif command == 'L':
        imprimir(CRUD_cliente.registros_clientes)
    elif command == 'S':
        escoger_opciones()
    else:
        print("comando invalido")
        run_factura()


def imprimir(registros_clientes):
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
    print_options_factura()


def ingreso_busqueda():
    cedula = int(input("ingrese la cedula del cliente que desea buscar: "))
    return cedula


def impresion_encontrado(a, b, c):
    print (f"nombre:{a}")
    print (f"cedula:{b}")
    print (f"numero de facturas:{c}")
    

def impresion_no_encontrados():
    print("el cliente que esta buscando no esta registrado")


def elegir_productos_factura():
    print("    ")
    print("1.agregar antibiotico")
    print("2.agregar pesticida")
    print("3.agregarproducto de control fertilizante")
    print("4.Salir")
    eleccion = (int(input("Ingrese la opcion: ")))
    return eleccion


def ingreso_de_datos_factura():
    fecha = (str(input("Ingrese la fecha de la factura: ")))
    return fecha


def print_options_antibiotico():
    print("REGISTROS DE ANTIBIOTICO ")
    print('*' * 50)
    print("[C]rear antibiotico")
    print("[L]istar antibiotico")
    print("[E]liminar antibiotico")
    print("[S]alir")
    run_antibiotico()

def run_antibiotico():
    command = input()
    command = command.upper()

    if command == 'C':
        ingreso_de_datos_antibiotico()
    elif command == 'L':
        imprimir_antibiotico(CRUD_antibiotico.registros_antibiotico)
    elif command == 'E':
        ingreso_datos_eliminar_antibiotico()
    elif command == 'S':
        escoger_opciones()
    else:
        print("comando invalido")
        run_antibiotico()


def ingreso_de_datos_antibiotico():
    nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
    dosis = (str(input("Ingrese la dosis del producto: ")))
    precio = (int(input("Ingrese ingrese el precio: ")))
    CONTROLLER.crear_antibiotico(nombre_del_producto, dosis, precio)


def imprimir_antibiotico(registros_antibiotico):
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
    print_options_antibiotico()


def ingreso_datos_eliminar_antibiotico():
    producto = (str(input("ingrese el nombre del producto que desea eliminar: ")))
    CONTROLLER.eliminar_antibiotico(producto)


def ingreso_datos_busqueda_antibiotico():
    producto = str(input("ingrese el nombre del producto que desea buscar: "))
    return producto


def impresion_antibiotico_encontrado(a, b, c, d):
    print('*' * 50)
    print(f"Nombre del antibiotico: {a}")
    print(f"Dosis Recomendada: {b}")
    print(f"Tipo de animal: {c}")
    print(f"Precio: {d}")
    print('*' * 50)


def impresion_antibiotico_no_encontrado():
    print("el producto que esta buscando no existe en el inventario")


def print_options_fertilizante():
    print("REGISTROS DE FERTILIZANTES ")
    print('*' * 50)
    print("[C]rear fertilizante")
    print("[L]istar fertilizante")
    print("[E]liminar fertilizante")
    print("[S]alir")
    run_fertilizante()

def run_fertilizante():
    command = input()
    command = command.upper()

    if command == 'C':
        ingreso_de_datos_fertilizante()
    elif command == 'L':
        imprimir_fertilizante(CRUD_fertilizante.registros_fertilizantes)
    elif command == 'E':
        ingreso_datos_eliminar_fertilizante()
    elif command == 'S':
        escoger_opciones()
    else:
        print("comando invalido")
        run_fertilizante()


def ingreso_de_datos_fertilizante():
    registro_ica = (str(input("Ingrese el registro ICA del producto: ")))
    nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
    frecuencia_de_aplicacion = (str(input("Ingrese la frecuencia de aplicacion del producto: ")))
    valor_del_producto = (int(input("Ingrese ingrese el precio: ")))
    fecha_de_ultima_aplicacion = (str(input("Ingrese la fecha de ultima aplicacion del producto: ")))
    CONTROLLER.crear_fertilizante(registro_ica, nombre_del_producto, frecuencia_de_aplicacion,
                                  valor_del_producto, fecha_de_ultima_aplicacion)


def imprimir_fertilizante(registros_fertilizantes):
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
    print_options_fertilizante()


def ingreso_datos_eliminar_fertilizante():
    producto = (str(input("ingrese el nombre del producto que desea eliminar: ")))
    CONTROLLER.eliminar_fertilizante(producto)


def ingreso_datos_busqueda_fertilizante():
    producto = str(input("ingrese el nombre del producto que desea buscar: "))
    return producto


def impresion_fertilizante_encontrado(a, b, c, d, e):
    print('*' * 50)
    print(f"Registro ICA: {a}")
    print(f"Nombre del fertilizante: {b}")
    print(f"Frecuencia de aplicacion: {c}")
    print(f"Precio: {d}")
    print(f"Fecha de ultima aplicacion: {e}")
    print('*' * 50)


def impresion_fertilizante_no_encontrado():
    print("el producto que esta buscando no existe en el inventario")


def print_options_plagas():
    print("REGISTROS DE PRODUCTOS DE CONTROL DE PLAGAS ")
    print('*' * 50)
    print("[C]rear peticida")
    print("[L]istar pesticidas")
    print("[E]liminar psticida")
    print("[S]alir")
    run_plagas()


def run_plagas():
    command = input()
    command = command.upper()

    if command == 'C':
        ingreso_de_datos_plagas()
    elif command == 'L':
        imprimir_plagas(CRUD_control_de_plagas.registros_pesticidas)
    elif command == 'E':
        ingreso_datos_eliminar_plaga()
    elif command == 'S':
        escoger_opciones()
    else:
        print("comando invalido")
        run_plagas()


def ingreso_de_datos_plagas():
    registro_ica = (str(input("Ingrese el registro ICA del producto: ")))
    nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
    frecuencia_de_aplicacion = (str(input("Ingrese la frecuencia de aplicacion del producto: ")))
    valor_del_producto = (int(input("Ingrese ingrese el precio: ")))
    periodo_de_carencia = (str(input("Ingrese la fecha de ultima aplicacion del producto: ")))
    CONTROLLER.crear_plagas(registro_ica, nombre_del_producto, frecuencia_de_aplicacion
                                 , valor_del_producto, periodo_de_carencia)


def imprimir_plagas(registros_pesticidas):
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
    print_options_plagas()


def ingreso_datos_eliminar_plaga():
    producto = (str(input("ingrese el nombre del producto que desea eliminar: ")))
    CONTROLLER.eliminar_plagas(producto)


def ingreso_datos_busqueda_plaga():
    producto = str(input("ingrese el nombre del producto que desea buscar: "))
    return producto


def impresion_plaga_encontrado(a, b, c, d, e):
    print('*' * 50)
    print(f"Registro ICA: {a}")
    print(f"Nombre del fertilizante: {b}")
    print(f"Frecuencia de aplicacion: {c}")
    print(f"Precio: {d}")
    print(f"Periodo de carencia: {e}")
    print('*' * 50)


def impresion_plaga_no_encontrado():
    print("el producto que esta buscando no existe en el inventario")