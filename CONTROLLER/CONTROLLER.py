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


def retorno_interfaz_antibiotico():
    IG.print_options_antibiotico()


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

