import re
from datetime import datetime

# ================= USUARIOS =================

class Usuario:

    contador_id = 1

    def __init__(self, nombre, apellido, fecha_nacimiento, email, telefono, curp):

        self.id = Usuario.contador_id
        Usuario.contador_id += 1

        self._nombre = ""
        self._apellido = ""
        self._fecha_nacimiento = ""
        self._email = ""
        self._telefono = ""
        self._curp = ""

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.telefono = telefono
        self.curp = curp

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        valor = valor.strip()

        if valor == "":
            raise ValueError("Nombre vacío")

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", valor):
            raise ValueError("El nombre solo puede contener letras")

        self._nombre = valor.title()

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):

        valor = valor.strip()

        if valor == "":
            raise ValueError("Apellido vacío")

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", valor):
            raise ValueError("El apellido solo puede contener letras")

        self._apellido = valor.title()

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):

        try:
            fecha = datetime.strptime(valor, "%d-%m-%Y")

        except ValueError:
            raise ValueError("Fecha inválida")

        hoy = datetime.now()

        edad = hoy.year - fecha.year

        if (hoy.month, hoy.day) < (fecha.month, fecha.day):
            edad -= 1

        if edad < 15:
            raise ValueError("Debe ser mayor de 15 años")

        self._fecha_nacimiento = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):

        valor = valor.strip().lower()

        patron = r"^[^@ ]+@[^@]+\.[a-zA-Z]+$"

        if not re.match(patron, valor):
            raise ValueError("Email inválido")

        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        valor = valor.replace("-", "").replace(" ", "")

        if not valor.isdigit():
            raise ValueError("Teléfono inválido")

        if len(valor) != 10:
            raise ValueError("El teléfono debe contener 10 dígitos")

        self._telefono = valor

    @property
    def curp(self):
        return self._curp

    @curp.setter
    def curp(self, valor):

        valor = valor.strip()

        if valor != valor.upper():
            raise ValueError("La CURP debe escribirse en mayúsculas")

        patron = r"^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d$"

        if not re.match(patron, valor):
            raise ValueError("CURP inválida")

        self._curp = valor

    def __str__(self):

        return f"""
ID: {self.id}
Nombre: {self.nombre} {self.apellido}
Fecha de nacimiento: {self.fecha_nacimiento}
Email: {self.email}
Teléfono: {self.telefono}
CURP: {self.curp}
"""


usuarios = []

def registrar_usuario():

    print("\n===== REGISTRAR USUARIO =====")

    # ---------- NOMBRE ----------
    while True:

        try:

            nombre = input("Nombre: ").strip()

            if nombre == "":
                raise ValueError("Nombre vacío")

            if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", nombre):
                raise ValueError("El nombre solo debe contener letras")

            break

        except ValueError as e:

            print("ERROR:", e)

    # ---------- APELLIDO ----------
    while True:

        try:

            apellido = input("Apellido: ").strip()

            if apellido == "":
                raise ValueError("Apellido vacío")

            if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", apellido):
                raise ValueError("El apellido solo debe contener letras")

            break

        except ValueError as e:

            print("ERROR:", e)

    # ---------- FECHA ----------
    while True:

        try:

            fecha = input("Fecha nacimiento (DDMMAAAA): ").strip()

            fecha = fecha.replace(" ", "")

            if not fecha.isdigit() or len(fecha) != 8:
                raise ValueError("Debes escribir 8 números")

            fecha = fecha[:2] + "-" + fecha[2:4] + "-" + fecha[4:]

            fecha_convertida = datetime.strptime(fecha, "%d-%m-%Y")

            hoy = datetime.now()

            edad = hoy.year - fecha_convertida.year

            if (hoy.month, hoy.day) < (fecha_convertida.month, fecha_convertida.day):
                edad -= 1

            if edad < 15:
                raise ValueError("Debe ser mayor de 15 años")

            break

        except ValueError as e:

            print("ERROR:", e)

    # ---------- EMAIL ----------
    while True:

        try:

            email = input("Email: ").lower().strip()

            patron = r"^[^@]+@[^@]+\.[a-zA-Z]+$"

            if not re.match(patron, email):
                raise ValueError("Email inválido")

            repetido = False

            for u in usuarios:

                if u.email == email:
                    repetido = True
                    break

            if repetido:
                raise ValueError("Correo ya registrado")

            break

        except ValueError as e:

            print("ERROR:", e)

    # ---------- TELEFONO ----------
    while True:

        try:

            telefono = input("Teléfono (10 dígitos): ").strip()

            telefono = telefono.replace("-", "").replace(" ", "")

            if not telefono.isdigit():
                raise ValueError("El teléfono solo debe contener números")

            if len(telefono) != 10:
                raise ValueError("El teléfono debe tener exactamente 10 dígitos")

            repetido = False

            for u in usuarios:

                if u.telefono == telefono:
                    repetido = True
                    break

            if repetido:
                raise ValueError("Teléfono ya registrado")

            break

        except ValueError as e:

            print("ERROR:", e)

    # ---------- CURP ----------
    while True:

        try:

            curp = input("CURP (solo mayúsculas): ").strip()

            if curp != curp.upper():
                raise ValueError("La CURP debe escribirse en mayúsculas")

            patron = r"^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d$"

            if not re.match(patron, curp):
                raise ValueError("CURP inválida")

            repetido = False

            for u in usuarios:

                if u.curp == curp:
                    repetido = True
                    break

            if repetido:
                raise ValueError("CURP ya registrada")

            break

        except ValueError as e:

            print("ERROR:", e)

    # ---------- CREAR USUARIO ----------
    try:

        nuevo = Usuario(
            nombre,
            apellido,
            fecha,
            email,
            telefono,
            curp
        )

        usuarios.append(nuevo)

        print("\nUsuario registrado correctamente")

    except ValueError as e:

        print("ERROR:", e)


# ================= CLASES =================

clases = []

instructores = ["Milena", "Debanhi", "Franco", "Katia", "Nahomi", "Jesus"]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


class ClaseGym:

    def __init__(self, ID, nombre, disciplina, cupo, dia, hora, duracion, instructor):

        self.ID = ID
        self.nombre = nombre
        self.disciplina = disciplina
        self.cupo = cupo
        self.dia = dia
        self.hora = hora
        self.duracion = duracion
        self.instructor = instructor

    @property
    def cupo(self):
        return self._cupo

    @cupo.setter
    def cupo(self, cupo):

        if cupo > 0:
            self._cupo = cupo

        else:
            raise ValueError("Cupo inválido")

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, hora):

        try:

            datetime.strptime(hora, "%H:%M")
            self._hora = hora

        except ValueError:

            raise ValueError("Hora inválida")

    def __str__(self):

        return f"""
ID: {self.ID}
Nombre: {self.nombre}
Disciplina: {self.disciplina}
Cupo: {self.cupo}
Horario: {self.dia} {self.hora}
Duración: {self.duracion} min
Instructor: {self.instructor}
"""


def generar_id():

    if len(clases) == 0:
        return 1

    return clases[-1].ID + 1


def buscar_clase(ID):

    for clase in clases:

        if clase.ID == ID:
            return clase

    return None


def verificar_traslape(dia, hora):

    for clase in clases:

        if clase.dia == dia and clase.hora == hora:
            return True

    return False


def agregar_clase():

    print("\nAGREGAR CLASE")

    nombre = input("Nombre: ")
    disciplina = input("Disciplina: ")

    while True:

        try:

            cupo = int(input("Cupo: "))

            if cupo > 0:
                break

            print("ERROR: Cupo inválido")

        except ValueError:

            print("ERROR: Ingresa un número válido")

    while True:

        dia = input("Día: ").capitalize()

        if dia in dias:
            break

        print("ERROR: Día inválido")

    while True:

        hora = input("Hora (HH:MM): ")

        try:

            datetime.strptime(hora, "%H:%M")

            if verificar_traslape(dia, hora):

                print("ERROR: Horario ocupado")

            else:
                break

        except ValueError:

            print("ERROR: Hora inválida")

    while True:

        try:

            duracion = int(input("Duración: "))

            if duracion > 0:
                break

            print("ERROR: Duración inválida")

        except ValueError:

            print("ERROR: Ingresa un número válido")

    print("\nINSTRUCTORES")

    for instructor in instructores:
        print("-", instructor)

    while True:

        instructor = input("Instructor: ").capitalize()

        if instructor in instructores:
            break

        print("ERROR: Instructor inválido")

    nueva = ClaseGym(generar_id(), nombre, disciplina, cupo, dia, hora, duracion, instructor)

    clases.append(nueva)

    print("Clase agregada")


def mostrar_clases():

    if len(clases) == 0:

        print("No hay clases")
        return

    for clase in clases:
        print(clase)


def modificar_clase(inscripciones):

    while True:

        try:

            ID = int(input("ID: "))

            clase = buscar_clase(ID)

            if clase != None:
                break

            print("Clase no encontrada")

        except ValueError:

            print("ID inválido")

    while True:

        try:

            nuevo_cupo = int(input("Nuevo cupo: "))

            inscritos = 0

            for i in inscripciones:

                if i.clase == clase and i.estado == "Activa":
                    inscritos += 1

            if nuevo_cupo < inscritos:

                print("Hay más inscritos que el nuevo cupo")

            elif nuevo_cupo > 0:
                break

            else:
                print("Cupo inválido")

        except ValueError:

            print("Ingresa un número válido")

    clase.cupo = nuevo_cupo

    print("Clase modificada")


def eliminar_clase(inscripciones):

    while True:

        try:

            ID = int(input("ID: "))

            clase = buscar_clase(ID)

            if clase != None:
                break

            print("Clase no encontrada")

        except ValueError:

            print("ID inválido")

    inscritos = []

    for i in inscripciones:

        if i.clase == clase and i.estado == "Activa":

            inscritos.append(i.usuario)

    if len(inscritos) > 0:

        print("\nLa clase tiene inscripciones activas:\n")

        for usuario in inscritos:
            print("-", usuario.nombre)

        print("\nNo se puede eliminar")
        return

    clases.remove(clase)

    print("Clase eliminada")

# ================= INSCRIPCIONES =================

inscripciones = []


class Inscripcion:

    def __init__(self, usuario, clase):

        self.usuario = usuario
        self.clase = clase
        self.estado = "Activa"

    def __str__(self):

        return f"""
Usuario: {self.usuario.nombre}
Clase: {self.clase.nombre}
Estado: {self.estado}
"""


def inscribir_usuario():

    print("\n===== INSCRIPCIÓN A CLASE =====")

    if len(usuarios) == 0:

        print("No hay usuarios registrados")
        return

    if len(clases) == 0:

        print("No hay clases disponibles")
        return

    print("\nUSUARIOS")

    for usuario in usuarios:

        print(f"{usuario.id} - {usuario.nombre}")

    while True:

        try:

            id_usuario = int(input("\nID usuario: "))

            usuario_encontrado = None

            for usuario in usuarios:

                if usuario.id == id_usuario:

                    usuario_encontrado = usuario
                    break

            if usuario_encontrado != None:
                break

            print("Usuario no existe")

        except ValueError:

            print("ID inválido")

    print("\nCLASES DISPONIBLES")

    for clase in clases:

        inscritos = 0

        for inscripcion in inscripciones:

            if inscripcion.clase == clase and inscripcion.estado == "Activa":

                inscritos += 1

        disponibles = clase.cupo - inscritos

        print(f"""
ID: {clase.ID}
Clase: {clase.nombre}
Instructor: {clase.instructor}
Horario: {clase.dia} {clase.hora}
Disponibles: {disponibles}
""")

    while True:

        try:

            id_clase = int(input("ID clase: "))

            clase_encontrada = buscar_clase(id_clase)

            if clase_encontrada != None:
                break

            print("Clase no encontrada")

        except ValueError:

            print("ID inválido")

    for inscripcion in inscripciones:

        if inscripcion.usuario == usuario_encontrado and inscripcion.clase == clase_encontrada and inscripcion.estado == "Activa":

            print("Ya está inscrito")
            return

    inscritos = 0

    for inscripcion in inscripciones:

        if inscripcion.clase == clase_encontrada and inscripcion.estado == "Activa":

            inscritos += 1

    if inscritos >= clase_encontrada.cupo:

        print("Clase llena")
        return

    for inscripcion in inscripciones:

        if inscripcion.usuario == usuario_encontrado and inscripcion.clase.dia == clase_encontrada.dia and inscripcion.clase.hora == clase_encontrada.hora and inscripcion.estado == "Activa":

            print("Conflicto de horario")
            return

    nueva = Inscripcion(usuario_encontrado, clase_encontrada)

    inscripciones.append(nueva)

    print("\nInscripción exitosa")


def mostrar_inscripciones():

    print("\n===== INSCRIPCIONES =====")

    if len(inscripciones) == 0:

        print("No hay inscripciones")
        return

    for inscripcion in inscripciones:

        print(inscripcion)

# ================= PAGOS =================
pagos = []
class Pago:

    COSTO_MEMBRESIA = 650

    def __init__(
        self,
        usuario,
        monto,
        metodo,
        periodo,
        fecha_obj,
        abono=0,
        adeudo=0
    ):

        self.usuario = usuario
        self.monto = monto
        self.metodo = metodo
        self.periodo = periodo
        self.fecha = fecha_obj
        self.abono = abono
        self.adeudo = adeudo

    def __str__(self):

        texto = f"""
Usuario: {self.usuario.nombre}
Monto: {self.monto}
Método: {self.metodo}
Periodo: {self.periodo}
Fecha: {self.fecha}
"""
        
        if self.abono > 0:
            texto += f"\nABONO EXTRA: ${self.abono:.2f}"

        if self.adeudo > 0:
            texto += f"\nADEUDO: ${self.adeudo:.2f}"

        return texto

def buscar_usuario_por_id(ID):

    for usuario in usuarios:

        if usuario.id == ID:
            return usuario

    return None


def pago_duplicado(usuario, periodo):

    for pago in pagos:

        if (
            pago.usuario == usuario
            and pago.periodo.lower() == periodo.lower()
        ):

            return True

    return False


def registrar_pago():

    print("\n===== REGISTRAR PAGO =====")

    if len(usuarios) == 0:

        print("No hay usuarios registrados")
        return

    print("\nUSUARIOS")

    for usuario in usuarios:

        print(f"{usuario.id} - {usuario.nombre}")

    try:

        id_usuario = int(input("\nID usuario: "))

    except:

        print("ID inválido")
        return

    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:

        print("Usuario no encontrado")
        return

    try:

        monto = float(input("Monto pagado: "))

    except:

        print("Monto inválido")
        return

    abono = 0
    adeudo = 0

    if monto > Pago.COSTO_MEMBRESIA:
        abono = monto - Pago.COSTO_MEMBRESIA

    elif monto < Pago.COSTO_MEMBRESIA:
        adeudo = Pago.COSTO_MEMBRESIA - monto

    if abono > 0:
       print(f"Pagó ${abono:.2f} más de la mensualidad.")

    if adeudo > 0:
     print(f"Tiene un adeudo de ${adeudo:.2f}")

    metodo = input(
        "Método (efectivo/tarjeta/transferencia): "
    ).lower()

    if metodo not in [
        "efectivo",
        "tarjeta",
        "transferencia"
    ]:

        print("Método inválido")
        return

    periodo = input("Periodo (Ejemplo: Mayo 2026): ")

    if pago_duplicado(usuario, periodo):

        print("Ese periodo ya está pagado")
        return

    fecha = input("Fecha (dd/mm/yyyy): ")

    try:

        fecha_obj = datetime.strptime(
            fecha,
            "%d/%m/%Y"
        )

        if fecha_obj > datetime.now():

            print("No se permiten fechas futuras")
            return

    except:

        print("Fecha inválida")
        return

    nuevo_pago = Pago(
        usuario,
        monto,
        metodo,
        periodo,
        fecha,
        abono,
        adeudo
    )

    pagos.append(nuevo_pago)

    usuario.membresia_activa = True

    print("\nPago registrado correctamente")


def mostrar_pagos():

    print("\n===== PAGOS =====")

    if len(pagos) == 0:

        print("No hay pagos")
        return

    for pago in pagos:

        print(pago)


# ================= MENÚ PAGOS =================

def menu_pagos():

    while True:

        print("\n===== PAGOS =====")
        print("1. Registrar pago")
        print("2. Mostrar pagos")
        print("3. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            registrar_pago()

        elif opcion == "2":

            mostrar_pagos()

        elif opcion == "3":

            break

        else:

            print("Opción inválida")

# ================= ASISTENCIAS =================

asistencias = []

class Asistencia:

    def __init__(self, usuario, clase, fecha):

        self.usuario = usuario
        self.clase = clase
        self.fecha = fecha

    def __str__(self):

        return f"""
Usuario: {self.usuario.nombre}
Clase: {self.clase.nombre}
Fecha: {self.fecha}
"""
    
def usuario_tiene_pago(usuario):

    for pago in pagos:

        if pago.usuario == usuario:
            return True

    return False

def registrar_asistencia():

    print("\n===== REGISTRO DE ASISTENCIA =====")

    if len(usuarios) == 0:

        print("No hay usuarios")
        return

    for usuario in usuarios:

        print(f"{usuario.id} - {usuario.nombre}")

    try:

        id_usuario = int(input("ID usuario: "))

    except ValueError:

        print("ID inválido")
        return

    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:

        print("Usuario no encontrado")
        return

    if not usuario_tiene_pago(usuario):

        print("El usuario no tiene pagos registrados")
        return

    clases_usuario = []

    for inscripcion in inscripciones:

        if (
            inscripcion.usuario == usuario
            and inscripcion.estado == "Activa"
        ):

            clases_usuario.append(inscripcion.clase)

    if len(clases_usuario) == 0:

        print("El usuario no está inscrito en ninguna clase")
        return

    print("\nCLASES INSCRITAS")

    for clase in clases_usuario:

        print(
            f"{clase.ID} - {clase.nombre}"
        )

    try:

        id_clase = int(input("ID clase: "))

    except ValueError:

        print("ID inválido")
        return

    clase_seleccionada = None

    for clase in clases_usuario:

        if clase.ID == id_clase:

            clase_seleccionada = clase
            break

    if clase_seleccionada is None:

        print("El usuario no está inscrito en esa clase")
        return

    fecha = datetime.now().strftime("%d/%m/%Y")

    for asistencia in asistencias:

        if (
            asistencia.usuario == usuario
            and asistencia.clase == clase_seleccionada
            and asistencia.fecha == fecha
        ):

            print("La asistencia ya fue registrada hoy")
            return

    nueva = Asistencia(
        usuario,
        clase_seleccionada,
        fecha
    )

    asistencias.append(nueva)

    print("Asistencia registrada")

def mostrar_asistencias():

    print("\n===== ASISTENCIAS =====")

    if len(asistencias) == 0:

        print("No hay asistencias")
        return

    for asistencia in asistencias:

        print(asistencia)

def menu_asistencias():

    while True:

        print("\n===== ASISTENCIAS =====")
        print("1. Registrar asistencia")
        print("2. Mostrar asistencias")
        print("3. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            registrar_asistencia()

        elif opcion == "2":

            mostrar_asistencias()

        elif opcion == "3":

            break

        else:

            print("Opción inválida")

# ================= REPORTES =================

def reporte_usuario():

    print("\n===== REPORTE DE USUARIO =====")

    try:

        id_usuario = int(input("ID usuario: "))

    except ValueError:

        print("ID inválido")
        return

    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:

        print("Usuario no encontrado")
        return

    print(usuario)

    print("\n--- PAGOS ---")

    tiene_pago = False

    for pago in pagos:

        if pago.usuario == usuario:

            print(pago)
            tiene_pago = True

    if not tiene_pago:

        print("Sin pagos registrados")

    print("\n--- CLASES INSCRITAS ---")

    tiene_clases = False

    for inscripcion in inscripciones:

        if (
            inscripcion.usuario == usuario
            and inscripcion.estado == "Activa"
        ):

            print(
                f"{inscripcion.clase.nombre}"
            )

            tiene_clases = True

    if not tiene_clases:

        print("Sin clases")

    print("\n--- ASISTENCIAS ---")

    contador = 0

    for asistencia in asistencias:

        if asistencia.usuario == usuario:

            print(
                f"{asistencia.clase.nombre} - {asistencia.fecha}"
            )

            contador += 1

    if contador == 0:

        print("Sin asistencias")

    print(f"\nTotal asistencias: {contador}")

def reporte_general():

    print("\n===== REPORTE GENERAL =====")

    print(f"Usuarios: {len(usuarios)}")
    print(f"Clases: {len(clases)}")
    print(f"Inscripciones: {len(inscripciones)}")
    print(f"Pagos: {len(pagos)}")
    print(f"Asistencias: {len(asistencias)}")

    # Resumen de inventario en el reporte general
    if len(inventario) > 0:

        print(f"Artículos en inventario: {len(inventario)}")

        stock_bajo = [a for a in inventario if a.cantidad <= a.stock_minimo]

        if len(stock_bajo) > 0:

            print(f"  ⚠ Artículos con stock bajo: {len(stock_bajo)}")

            for articulo in stock_bajo:

                print(f"    - {articulo.nombre} (cantidad: {articulo.cantidad}, mínimo: {articulo.stock_minimo})")

def menu_reportes():

    while True:

        print("\n===== REPORTES =====")
        print("1. Reporte de usuario")
        print("2. Reporte general")
        print("3. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            reporte_usuario()

        elif opcion == "2":

            reporte_general()

        elif opcion == "3":

            break

        else:

            print("Opción inválida")


# ================= INVENTARIO =================

inventario = []

categorias_inventario = [
    "Equipamiento",
    "Suplementos",
    "Ropa",
    "Limpieza",
    "Papelería",
    "Otro"
]


class ArticuloInventario:

    contador_id = 1

    def __init__(self, nombre, categoria, cantidad, precio_unitario, stock_minimo, descripcion=""):

        self.id = ArticuloInventario.contador_id
        ArticuloInventario.contador_id += 1

        self._nombre = ""
        self._categoria = ""
        self._cantidad = 0
        self._precio_unitario = 0.0
        self._stock_minimo = 0

        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.stock_minimo = stock_minimo
        self.descripcion = descripcion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if valor.strip() == "":
            raise ValueError("Nombre vacío")

        self._nombre = valor.strip()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):

        if valor not in categorias_inventario:
            raise ValueError("Categoría inválida")

        self._categoria = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):

        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")

        self._cantidad = valor

    @property
    def precio_unitario(self):
        return self._precio_unitario

    @precio_unitario.setter
    def precio_unitario(self, valor):

        if valor < 0:
            raise ValueError("El precio no puede ser negativo")

        self._precio_unitario = valor

    @property
    def stock_minimo(self):
        return self._stock_minimo

    @stock_minimo.setter
    def stock_minimo(self, valor):

        if valor < 0:
            raise ValueError("El stock mínimo no puede ser negativo")

        self._stock_minimo = valor

    def __str__(self):

        alerta = " ⚠ STOCK BAJO" if self.cantidad <= self.stock_minimo else ""

        return f"""
ID: {self.id}
Nombre: {self.nombre}{alerta}
Categoría: {self.categoria}
Cantidad: {self.cantidad}
Precio unitario: ${self.precio_unitario:.2f}
Stock mínimo: {self.stock_minimo}
Descripción: {self.descripcion if self.descripcion else "Sin descripción"}
"""


def buscar_articulo(ID):

    for articulo in inventario:

        if articulo.id == ID:
            return articulo

    return None


def agregar_articulo():

    print("\n===== AGREGAR ARTÍCULO =====")

    nombre = input("Nombre del artículo: ").strip()

    if nombre == "":

        print("Nombre vacío")
        return

    # Verificar nombre duplicado
    for articulo in inventario:

        if articulo.nombre.lower() == nombre.lower():

            print("Ya existe un artículo con ese nombre")
            return

    print("\nCATEGORÍAS")

    for i, cat in enumerate(categorias_inventario, 1):
        print(f"{i}. {cat}")

    while True:

        try:

            opcion_cat = int(input("Elige categoría (número): "))

            if 1 <= opcion_cat <= len(categorias_inventario):

                categoria = categorias_inventario[opcion_cat - 1]
                break

            print("Opción inválida")

        except ValueError:

            print("Ingresa un número válido")

    while True:

        try:

            cantidad = int(input("Cantidad inicial: "))

            if cantidad >= 0:
                break

            print("La cantidad no puede ser negativa")

        except ValueError:

            print("Ingresa un número válido")

    while True:

        try:

            precio = float(input("Precio unitario ($): "))

            if precio >= 0:
                break

            print("El precio no puede ser negativo")

        except ValueError:

            print("Ingresa un número válido")

    while True:

        try:

            stock_minimo = int(input("Stock mínimo (alerta si baja de este número): "))

            if stock_minimo >= 0:
                break

            print("El stock mínimo no puede ser negativo")

        except ValueError:

            print("Ingresa un número válido")

    descripcion = input("Descripción (opcional, Enter para omitir): ").strip()

    try:

        nuevo = ArticuloInventario(
            nombre,
            categoria,
            cantidad,
            precio,
            stock_minimo,
            descripcion
        )

        inventario.append(nuevo)

        print("Artículo agregado al inventario")

    except ValueError as e:

        print("ERROR:", e)


def mostrar_inventario():

    print("\n===== INVENTARIO =====")

    if len(inventario) == 0:

        print("No hay artículos en el inventario")
        return

    # Mostrar alertas de stock bajo primero
    stock_bajo = [a for a in inventario if a.cantidad <= a.stock_minimo]

    if len(stock_bajo) > 0:

        print(f"\n⚠ ARTÍCULOS CON STOCK BAJO ({len(stock_bajo)}):")

        for articulo in stock_bajo:

            print(f"  - {articulo.nombre}: {articulo.cantidad} unidades (mínimo: {articulo.stock_minimo})")

    print("\nTODOS LOS ARTÍCULOS:")

    for articulo in inventario:

        print(articulo)


def editar_articulo():

    print("\n===== EDITAR ARTÍCULO =====")

    if len(inventario) == 0:

        print("No hay artículos en el inventario")
        return

    for articulo in inventario:

        print(f"{articulo.id} - {articulo.nombre} (cantidad: {articulo.cantidad})")

    while True:

        try:

            ID = int(input("\nID del artículo a editar: "))

            articulo = buscar_articulo(ID)

            if articulo is not None:
                break

            print("Artículo no encontrado")

        except ValueError:

            print("ID inválido")

    print(articulo)

    print("¿Qué deseas editar?")
    print("1. Nombre")
    print("2. Categoría")
    print("3. Cantidad")
    print("4. Precio unitario")
    print("5. Stock mínimo")
    print("6. Descripción")
    print("7. Cancelar")

    opcion = input("Opción: ")

    if opcion == "1":

        nuevo_nombre = input("Nuevo nombre: ").strip()

        if nuevo_nombre == "":

            print("Nombre vacío")
            return

        for a in inventario:

            if a.nombre.lower() == nuevo_nombre.lower() and a.id != articulo.id:

                print("Ya existe un artículo con ese nombre")
                return

        try:

            articulo.nombre = nuevo_nombre
            print("Nombre actualizado")

        except ValueError as e:

            print("ERROR:", e)

    elif opcion == "2":

        print("\nCATEGORÍAS")

        for i, cat in enumerate(categorias_inventario, 1):
            print(f"{i}. {cat}")

        while True:

            try:

                opcion_cat = int(input("Nueva categoría (número): "))

                if 1 <= opcion_cat <= len(categorias_inventario):

                    articulo.categoria = categorias_inventario[opcion_cat - 1]
                    print("Categoría actualizada")
                    break

                print("Opción inválida")

            except ValueError:

                print("Ingresa un número válido")

    elif opcion == "3":

        while True:

            try:

                nueva_cantidad = int(input("Nueva cantidad: "))

                if nueva_cantidad >= 0:

                    articulo.cantidad = nueva_cantidad
                    print("Cantidad actualizada")

                    if nueva_cantidad <= articulo.stock_minimo:
                        print(f"⚠ Advertencia: la cantidad está por debajo del stock mínimo ({articulo.stock_minimo})")

                    break

                print("La cantidad no puede ser negativa")

            except ValueError:

                print("Ingresa un número válido")

    elif opcion == "4":

        while True:

            try:

                nuevo_precio = float(input("Nuevo precio unitario ($): "))

                if nuevo_precio >= 0:

                    articulo.precio_unitario = nuevo_precio
                    print("Precio actualizado")
                    break

                print("El precio no puede ser negativo")

            except ValueError:

                print("Ingresa un número válido")

    elif opcion == "5":

        while True:

            try:

                nuevo_minimo = int(input("Nuevo stock mínimo: "))

                if nuevo_minimo >= 0:

                    articulo.stock_minimo = nuevo_minimo
                    print("Stock mínimo actualizado")
                    break

                print("El stock mínimo no puede ser negativo")

            except ValueError:

                print("Ingresa un número válido")

    elif opcion == "6":

        nueva_desc = input("Nueva descripción (Enter para dejar vacía): ").strip()
        articulo.descripcion = nueva_desc
        print("Descripción actualizada")

    elif opcion == "7":

        print("Edición cancelada")

    else:

        print("Opción inválida")


def eliminar_articulo():

    print("\n===== ELIMINAR ARTÍCULO =====")

    if len(inventario) == 0:

        print("No hay artículos en el inventario")
        return

    for articulo in inventario:

        print(f"{articulo.id} - {articulo.nombre}")

    while True:

        try:

            ID = int(input("\nID del artículo a eliminar: "))

            articulo = buscar_articulo(ID)

            if articulo is not None:
                break

            print("Artículo no encontrado")

        except ValueError:

            print("ID inválido")

    print(f"\n¿Eliminar '{articulo.nombre}'? (s/n): ", end="")

    confirmacion = input().strip().lower()

    if confirmacion == "s":

        inventario.remove(articulo)
        print("Artículo eliminado")

    else:

        print("Eliminación cancelada")
def menu_inventario():

    while True:

        print("\n===== INVENTARIO =====")
        print("1. Agregar artículo")
        print("2. Mostrar inventario")
        print("3. Editar artículo")
        print("4. Eliminar artículo")
        print("5. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            agregar_articulo()

        elif opcion == "2":

            mostrar_inventario()

        elif opcion == "3":

            editar_articulo()

        elif opcion == "4":

            eliminar_articulo()

        elif opcion == "5":

            break

        else:

            print("Opción inválida")


# ================= MENÚ USUARIOS =================

def menu_usuarios():

    while True:

        print("\n===== USUARIOS =====")
        print("1. Registrar usuario")
        print("2. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            registrar_usuario()

        elif opcion == "2":

            break

        else:

            print("Opción inválida")


# ================= MENÚ CLASES =================

def menu_clases():

    while True:

        print("\n===== GESTIONAR CLASES =====")
        print("1. Agregar clase")
        print("2. Mostrar clases")
        print("3. Modificar clase")
        print("4. Eliminar clase")
        print("5. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            agregar_clase()

        elif opcion == "2":

            mostrar_clases()

        elif opcion == "3":

            modificar_clase(inscripciones)

        elif opcion == "4":

            eliminar_clase(inscripciones)

        elif opcion == "5":

            break

        else:

            print("Opción inválida")


# ================= MENÚ INSCRIPCIONES =================

def menu_inscripciones():

    while True:

        print("\n===== INSCRIPCIONES =====")
        print("1. Inscribir usuario")
        print("2. Mostrar inscripciones")
        print("3. Volver")

        opcion = input("Opción: ")

        if opcion == "1":

            inscribir_usuario()

        elif opcion == "2":

            mostrar_inscripciones()

        elif opcion == "3":

            break

        else:

            print("Opción inválida")


# ================= MENÚ PRINCIPAL =================

while True:

    print("\n========== GYM ==========")
    print("1. Usuarios")
    print("2. Gestionar clases")
    print("3. Inscripciones")
    print("4. Pagos")
    print("5. Asistencias")
    print("6. Reportes")
    print("7. Inventario")
    print("8. Salir")

    opcion = input("Opción: ")

    if opcion == "1":

        menu_usuarios()

    elif opcion == "2":

        menu_clases()

    elif opcion == "3":

        menu_inscripciones()

    elif opcion == "4":

        menu_pagos()

    elif opcion == "5":

        menu_asistencias()

    elif opcion == "6":

        menu_reportes()

    elif opcion == "7":

        menu_inventario()

    elif opcion == "8":

        print("Programa finalizado")
        break

    else:

        print("Opción inválida")