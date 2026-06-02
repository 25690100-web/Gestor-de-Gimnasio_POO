from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from rich.progress import track
from rich import print as rprint
import time

console = Console()

# ====== RICH INTEGRADO ======
console.print(Panel.fit("[bold cyan]SISTEMA DE GIMNASIO[/bold cyan]", border_style="green"))
for _ in track(range(50), description="Cargando sistema..."):
    time.sleep(0.01)

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

    console.print("[green]\n===== REGISTRAR USUARIO =====[/green]")

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

            console.print("[red]ERROR:[/red]", e)

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

            console.print("[red]ERROR:[/red]", e)

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

            console.print("[red]ERROR:[/red]", e)

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

            console.print("[red]ERROR:[/red]", e)

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

            console.print("[red]ERROR:[/red]", e)

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

            console.print("[red]ERROR:[/red]", e)

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

        console.print("[bright_green]\nUsuario registrado correctamente[/bright_green]")

    except ValueError as e:

        console.print("[red]ERROR:[/red]", e)


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

    console.print("[blue]\nAGREGAR CLASE[/blue]")

    nombre = input("Nombre: ")
    disciplina = input("Disciplina: ")

    while True:

        try:

            cupo = int(input("Cupo: "))

            if cupo > 0:
                break

            console.print("ERROR: Cupo inválido")

        except ValueError:

            console.print("[red]ERROR: Ingresa un número válido[/red]")

    while True:

        dia = input("Día: ").capitalize()

        if dia in dias:
            break

        console.print("[red]ERROR: Día inválido[/red]")

    while True:

        hora = input("Hora (HH:MM): ")

        try:

            datetime.strptime(hora, "%H:%M")

            if verificar_traslape(dia, hora):

                console.print("ERROR: Horario ocupado")

            else:
                break

        except ValueError:

            console.print("[red]ERROR: Hora inválida[/red]")

    while True:

        try:

            duracion = int(input("Duración: "))

            if duracion > 0:
                break

            console.print("[red]ERROR: Duración inválida[/red]")

        except ValueError:

            console.print("[red]ERROR: Ingresa un número válido[/red]")

    console.print("[blue]\nINSTRUCTORES[/blue]")

    for instructor in instructores:
        print("-", instructor)

    while True:

        instructor = input("Instructor: ").capitalize()

        if instructor in instructores:
            break

        console.print("[red]ERROR: Instructor inválido[/red]")

    nueva = ClaseGym(generar_id(), nombre, disciplina, cupo, dia, hora, duracion, instructor)

    clases.append(nueva)

    console.print("[bright_blue]Clase agregada[/bright_blue]")

def mostrar_clases():

    console.print(
        Panel.fit(
            "[bold blue]📚 GESTIÓN DE CLASES[/bold blue]",
            border_style="bright_blue"
        )
    )

    if len(clases) == 0:

        console.print(
            "[bold red]❌ No hay clases registradas[/bold red]"
        )
        return

    tabla = Table(
        title="[bold magenta]📚 CLASES DISPONIBLES[/bold magenta]",
        border_style="bright_magenta",
        header_style="bold white on dark_blue",
        show_lines=True
    )

    tabla.add_column(
        "🆔 ID",
        justify="center",
        style="bright_cyan"
    )

    tabla.add_column(
        "📖 Nombre",
        style="spring_green1"
    )

    tabla.add_column(
        "🏋️ Disciplina",
        style="yellow"
    )

    tabla.add_column(
        "👨‍🏫 Instructor",
        style="deep_sky_blue1"
    )

    tabla.add_column(
        "🕒 Horario",
        style="orange1"
    )

    tabla.add_column(
        "👥 Cupo",
        justify="center"
    )

    for clase in clases:

        cupo = str(clase.cupo)

        if clase.cupo <= 5:
            cupo = f"[bold red]{clase.cupo}[/bold red]"
        elif clase.cupo <= 10:
            cupo = f"[bold yellow]{clase.cupo}[/bold yellow]"
        else:
            cupo = f"[bold green]{clase.cupo}[/bold green]"

        tabla.add_row(
            str(clase.ID),
            clase.nombre,
            clase.disciplina,
            clase.instructor,
            f"{clase.dia} {clase.hora}",
            cupo
        )

    console.print(tabla)

def modificar_clase(inscripciones):

    while True:

        try:

            ID = int(input("ID: "))

            clase = buscar_clase(ID)

            if clase != None:
                break

            console.print("[bright_blue]Clase no encontrada[/bright_blue]")

        except ValueError:

            console.print("[bright_blue]ID inválido[/bright_blue]")

    while True:

        try:

            nuevo_cupo = int(input("Nuevo cupo: "))

            inscritos = 0

            for i in inscripciones:

                if i.clase == clase and i.estado == "Activa":
                    inscritos += 1

            if nuevo_cupo < inscritos:

                print("[bright_blue]Hay más inscritos que el nuevo cupo[/bright_blue]")

            elif nuevo_cupo > 0:
                break

            else:
                print("[bright_blue]Cupo inválido[bright_blue]")

        except ValueError:

            console.print("[bright_blue]Ingresa un número válido[/bright_blue]")

    clase.cupo = nuevo_cupo

    print("[bright_blue]Clase modificada[/bright_blue]")


def eliminar_clase(inscripciones):

    while True:

        try:

            ID = int(input("ID: "))

            clase = buscar_clase(ID)

            if clase != None:
                break

            console.print("[bright_blue]Clase no encontrada[/bright_blue]")

        except ValueError:

            console.print("[bright_blue]ID inválido[/bright_blue]")

    inscritos = []

    for i in inscripciones:

        if i.clase == clase and i.estado == "Activa":

            inscritos.append(i.usuario)

    if len(inscritos) > 0:

        console.print("[blue]\nLa clase tiene inscripciones activas:\n[/blue]")

        for usuario in inscritos:
            console.print("-", usuario.nombre)

        console.print("[blue]\nNo se puede eliminar[/blue]")
        return

    clases.remove(clase)

    console.print("[bright_blue]Clase eliminada[/bright_blue]")

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

    console.print("[violet]\n===== INSCRIPCIÓN A CLASE =====[/violet]")

    if len(usuarios) == 0:

        console.print("[magenta]No hay usuarios registrados[/magenta]")
        return

    if len(clases) == 0:

        console.print("[magenta]No hay clases disponibles[/magenta]")
        return

    console.print("[violet]\nUSUARIOS[/violet]")

    for usuario in usuarios:

        console.print(f"[purple]{usuario.id} - {usuario.nombre}[/purple]")

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

            print("[magenta]Usuario no existe[/magenta]")

        except ValueError:

            console.print("[magenta]ID inválido[/magenta]")

    console.print("[violet]\nCLASES DISPONIBLES[/violet]")

    for clase in clases:

        inscritos = 0

        for inscripcion in inscripciones:

            if inscripcion.clase == clase and inscripcion.estado == "Activa":

                inscritos += 1

        disponibles = clase.cupo - inscritos

        console.print(f"""[purple]
ID: {clase.ID}
Clase: {clase.nombre}
Instructor: {clase.instructor}
Horario: {clase.dia} {clase.hora}
Disponibles: {disponibles}
[/purple]""")

    while True:

        try:

            id_clase = int(input("ID clase: "))

            clase_encontrada = buscar_clase(id_clase)

            if clase_encontrada != None:
                break

            console.print("[magenta]Clase no encontrada[/magenta]")

        except ValueError:

            console.print("[magenta]ID inválido[/magenta]")

    for inscripcion in inscripciones:

        if inscripcion.usuario == usuario_encontrado and inscripcion.clase == clase_encontrada and inscripcion.estado == "Activa":

            console.print("[magenta]Ya está inscrito[/magenta]")
            return

    inscritos = 0

    for inscripcion in inscripciones:

        if inscripcion.clase == clase_encontrada and inscripcion.estado == "Activa":

            inscritos += 1

    if inscritos >= clase_encontrada.cupo:

        console.print("[magenta]Clase llena[/magenta]")
        return

    for inscripcion in inscripciones:

        if inscripcion.usuario == usuario_encontrado and inscripcion.clase.dia == clase_encontrada.dia and inscripcion.clase.hora == clase_encontrada.hora and inscripcion.estado == "Activa":

            console.print("[magenta]Conflicto de horario[/magenta]")
            return

    nueva = Inscripcion(usuario_encontrado, clase_encontrada)

    inscripciones.append(nueva)

    console.print("[violet]\nInscripción exitosa[/violet]")


def mostrar_inscripciones():

    console.print("[violet]\n===== INSCRIPCIONES =====[/violet]")

    if len(inscripciones) == 0:

        console.print("[magenta]No hay inscripciones[/magenta]")
        return

    for inscripcion in inscripciones:

        console.print(inscripcion)

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

    console.print("[yellow]\n===== REGISTRAR PAGO =====[/yellow]")

    if len(usuarios) == 0:

        print("[gold1]No hay usuarios registrados[/gold1]")
        return

    console.print("[yellow]\nUSUARIOS[/yellow]")

    for usuario in usuarios:

        console.print(f"[bright_yellow]{usuario.id} - {usuario.nombre}[/bright_yellow]")

    try:

        id_usuario = int(input("\nID usuario: "))

    except:

        console.print("[golden1]ID inválido[/golden1]")
        return

    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:

        console.print("[golden1]Usuario no encontrado[/golden1]")
        return

    try:

        monto = float(input("Monto pagado: "))

    except:

        console.print("[golden1]Monto inválido[/golden1]")
        return

    abono = 0
    adeudo = 0

    if monto > Pago.COSTO_MEMBRESIA:
        abono = monto - Pago.COSTO_MEMBRESIA

    elif monto < Pago.COSTO_MEMBRESIA:
        adeudo = Pago.COSTO_MEMBRESIA - monto

    if abono > 0:
       console.print(f"[bright_yellow]Pagó ${abono:.2f} más de la mensualidad.[/bright_yellow]")

    if adeudo > 0:
     console.print(f"[bright_yellow]Tiene un adeudo de ${adeudo:.2f}[/bright_yellow]")

    metodo = input(
        "Método (efectivo/tarjeta/transferencia): "
    ).lower()

    if metodo not in [
        "efectivo",
        "tarjeta",
        "transferencia"
    ]:

        console.print("[golden1]Método inválido[/golden1]")
        return

    periodo = input("Periodo (Ejemplo: Mayo 2026): ")

    if pago_duplicado(usuario, periodo):

        console.print("[golden1]Ese periodo ya está pagado[golden1]")
        return

    fecha = input("Fecha (dd/mm/yyyy): ")

    try:

        fecha_obj = datetime.strptime(
            fecha,
            "%d/%m/%Y"
        )

        if fecha_obj > datetime.now():

            console.print("[golden1]No se permiten fechas futuras[/golden1]")
            return

    except:

        print("[golden1]Fecha inválida[/golden1]")
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

    console.print("[yellow]\nPago registrado correctamente[/yellow]")

def mostrar_pagos():

    if len(pagos) == 0:

        console.print(
            "[bold red]No hay pagos registrados[/bold red]"
        )
        return

    console.print(
        Panel.fit(
            "[bold green]GESTIÓN DE PAGOS[/bold green]",
            border_style="green"
        )
    )

    tabla = Table(
        title="[bold yellow]💳 PAGOS REGISTRADOS[/bold yellow]",
        border_style="bright_green",
        header_style="bold white",
        show_lines=True
    )

    tabla.add_column(
        "Usuario",
        style="cyan"
    )

    tabla.add_column(
        "Monto",
        justify="right",
        style="bold green"
    )

    tabla.add_column(
        "Método",
        style="yellow"
    )

    tabla.add_column(
        "Periodo",
        style="magenta"
    )

    for pago in pagos:

        tabla.add_row(
            pago.usuario.nombre,
            f"${pago.monto:.2f}",
            pago.metodo,
            pago.periodo
        )

    console.print(tabla)


# ================= MENÚ PAGOS =================
def menu_pagos():

    while True:

        console.print(
            Panel.fit(
                "[bold yellow]MENÚ PAGOS[/bold yellow]",
                border_style="yellow"
            )
        )

        console.print("[yellow]1. Registrar pago[/yellow]")
        console.print("[yellow]2. Mostrar pagos[/yellow]")
        console.print("[yellow]3. Volver[/yellow]")

        opcion = input("Opción: ")

        if opcion == "1":

            registrar_pago()

        elif opcion == "2":

            mostrar_pagos()

        elif opcion == "3":

            break

        else:

            console.print(
                "[bold red]Opción inválida[/bold red]"
            )

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

    console.print("[orange3]\n===== REGISTRO DE ASISTENCIA =====[/orange3]")

    if len(usuarios) == 0:

        print("[white]No hay usuarios[/white]")
        return

    for usuario in usuarios:

        console.print(f"[bright_red]{usuario.id} - {usuario.nombre}[/bright_red]")

    try:

        id_usuario = int(input("ID usuario: "))

    except ValueError:

        console.print("[white]ID inválido[/white]")
        return

    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:

        console.print("[white]Usuario no encontrado[/white]")
        return

    if not usuario_tiene_pago(usuario):

        console.print("[white]El usuario no tiene pagos registrados[/white]")
        return

    clases_usuario = []

    for inscripcion in inscripciones:

        if (
            inscripcion.usuario == usuario
            and inscripcion.estado == "Activa"
        ):

            clases_usuario.append(inscripcion.clase)

    if len(clases_usuario) == 0:

        console.print("[white]El usuario no está inscrito en ninguna clase[/white]")
        return

    console.print("[green3]\nCLASES INSCRITAS[/green3]")

    for clase in clases_usuario:

        console.print(
            f"[bright_red]{clase.ID} - {clase.nombre}[bright_red]"
        )

    try:

        id_clase = int(input("ID clase: "))

    except ValueError:

        console.print("[white]ID inválido[/white]")
        return

    clase_seleccionada = None

    for clase in clases_usuario:

        if clase.ID == id_clase:

            clase_seleccionada = clase
            break

    if clase_seleccionada is None:

        console.print("[white]El usuario no está inscrito en esa clase[/white]")
        return

    fecha = datetime.now().strftime("%d/%m/%Y")

    for asistencia in asistencias:

        if (
            asistencia.usuario == usuario
            and asistencia.clase == clase_seleccionada
            and asistencia.fecha == fecha
        ):

            console.print("[white]La asistencia ya fue registrada hoy[/white]")
            return

    nueva = Asistencia(
        usuario,
        clase_seleccionada,
        fecha
    )

    asistencias.append(nueva)

    console.print("[white]Asistencia registrada[/white]")

def mostrar_asistencias():

    console.print(
        Panel.fit(
            "[bold cyan]✅ CONTROL DE ASISTENCIAS[/bold cyan]",
            border_style="cyan"
        )
    )

    if len(asistencias) == 0:

        console.print(
            "[bold red]❌ No hay asistencias registradas[/bold red]"
        )
        return

    tabla = Table(
        title="[bold green]📋 ASISTENCIAS REGISTRADAS[/bold green]",
        border_style="bright_cyan",
        header_style="bold white on dark_blue",
        show_lines=True
    )

    tabla.add_column(
        "👤 Usuario",
        style="spring_green1"
    )

    tabla.add_column(
        "🏋️ Clase",
        style="yellow"
    )

    tabla.add_column(
        "📅 Fecha",
        style="deep_sky_blue1"
    )

    for asistencia in asistencias:

        tabla.add_row(
            asistencia.usuario.nombre,
            asistencia.clase.nombre,
            str(asistencia.fecha)
        )

    console.print(tabla)

# ================= MENU ASISTENCIA =================
def menu_asistencias():

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]MENÚ ASISTENCIAS[/bold cyan]",
                border_style="cyan"
            )
        )

        console.print("[cyan]1. Registrar asistencia[/cyan]")
        console.print("[cyan]2. Mostrar asistencias[/cyan]")
        console.print("[cyan]3. Volver[/cyan]")

        opcion = input("Opción: ")

        if opcion == "1":

            registrar_asistencia()

        elif opcion == "2":

            mostrar_asistencias()

        elif opcion == "3":

            break

        else:

            console.print(
                "[bold red]Opción inválida[/bold red]"
            )

# ================= REPORTES =================

def reporte_usuario():

    console.print("[orange3]\n===== REPORTE DE USUARIO =====[/orange3]")

    try:

        id_usuario = int(input("ID usuario: "))

    except ValueError:

        print("ID inválido")
        return

    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:

        console.print("[white]Usuario no encontrado[/white]")
        return

    print(usuario)

    console.print("[orange3]\n--- PAGOS ---[/orange3]")

    tiene_pago = False

    for pago in pagos:

        if pago.usuario == usuario:

            print(pago)
            tiene_pago = True

    if not tiene_pago:

        console.print("[white]Sin pagos registrados[/white]")

    console.print("[orange3]\n--- CLASES INSCRITAS ---[/orange3]")

    tiene_clases = False

    for inscripcion in inscripciones:

        if (
            inscripcion.usuario == usuario
            and inscripcion.estado == "Activa"
        ):

            console.print(
                f"[bright_red]{inscripcion.clase.nombre}[/bright_red]"
            )

            tiene_clases = True

    if not tiene_clases:

        console.print("[white]Sin clases[white]")

    console.print("[orange3]\n--- ASISTENCIAS ---[/orange3]")

    contador = 0

    for asistencia in asistencias:

        if asistencia.usuario == usuario:

            console.print(
                f"[bright_red]{asistencia.clase.nombre} - {asistencia.fecha}[/bright_red]"
            )

            contador += 1

    if contador == 0:

        console.print("[white]Sin asistencias[/white]")

    console.print(f"[bright_red]\nTotal asistencias: {contador}[/bright_red]")

def reporte_general():

    console.print("[orange3]\n===== REPORTE GENERAL =====[/orange3]")

    print(f"Usuarios: {len(usuarios)}")
    print(f"Clases: {len(clases)}")
    print(f"Inscripciones: {len(inscripciones)}")
    print(f"Pagos: {len(pagos)}")
    print(f"Asistencias: {len(asistencias)}")

    # Resumen de inventario en el reporte general
    if len(inventario) > 0:

        console.print(f"[bright_red]Artículos en inventario: {len(inventario)}[/bright_red]")

        stock_bajo = [a for a in inventario if a.cantidad <= a.stock_minimo]

        if len(stock_bajo) > 0:

            console.print(f"[bright_red]  ⚠ Artículos con stock bajo: {len(stock_bajo)}[/bright_red]")

            for articulo in stock_bajo:

                console.print(f"[bright_red]    - {articulo.nombre} (cantidad: {articulo.cantidad}, mínimo: {articulo.stock_minimo})[/bright_red]")

# ================= MENU REPORTES =================
def menu_reportes():

    while True:

        tree = Tree("🏋️ GIMNASIO")

        usuarios = tree.add("👤 Usuarios")
        usuarios.add("Reporte de usuarios")

        clases = tree.add("📚 Clases")
        clases.add("Reporte de clases")

        pagos = tree.add("💳 Pagos")
        pagos.add("Pagos realizados")

        asistencias = tree.add("✅ Asistencias")
        asistencias.add("Control de asistencia")

        rama_inventario = tree.add("📦 Inventario")
        rama_inventario.add("Stock actual")
        rama_inventario.add("Stock bajo")

        console.print(tree)

        console.print(
            Panel.fit(
                "[bold cyan]MENÚ REPORTES[/bold cyan]",
                border_style="cyan"
            )
        )

        console.print("[cyan]1. Reporte de usuario[/cyan]")
        console.print("[cyan]2. Reporte general[/cyan]")
        console.print("[cyan]3. Volver[/cyan]")

        opcion = input("Opción: ")

        if opcion == "1":

            reporte_usuario()

        elif opcion == "2":

            reporte_general()

        elif opcion == "3":

            break

        else:

            console.print(
                "[bold red]Opción inválida[/bold red]"
            )

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

    console.print("[pink1]\n===== AGREGAR ARTÍCULO =====[/pink1]")

    nombre = input("Nombre del artículo: ").strip()

    if nombre == "":

        console.print("[hot_pink]Nombre vacío[/hot_pink]")
        return

    # Verificar nombre duplicado
    for articulo in inventario:

        if articulo.nombre.lower() == nombre.lower():

            console.print("[hot_pink]Ya existe un artículo con ese nombre[/hot_pink]")
            return

    print("[pink1]\nCATEGORÍAS[/`pink1]")

    for i, cat in enumerate(categorias_inventario, 1):
        console.print(f"{i}. {cat}")

    while True:

        try:

            opcion_cat = int(input("Elige categoría (número): "))

            if 1 <= opcion_cat <= len(categorias_inventario):

                categoria = categorias_inventario[opcion_cat - 1]
                break

            console.print("[hot_pink]Opción inválida[/hot_pink]")

        except ValueError:

            console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

    while True:

        try:

            cantidad = int(input("Cantidad inicial: "))

            if cantidad >= 0:
                break

            console.print("[hot_pink]La cantidad no puede ser negativa[/hot_pink]")

        except ValueError:

            console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

    while True:

        try:

            precio = float(input("Precio unitario ($): "))

            if precio >= 0:
                break

            console.print("[hot_pink]El precio no puede ser negativo[/hot_pink]")

        except ValueError:

            console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

    while True:

        try:

            stock_minimo = int(input("Stock mínimo (alerta si baja de este número): "))

            if stock_minimo >= 0:
                break

            console.print("[hot_pink]El stock mínimo no puede ser negativo[/hot_pink]")

        except ValueError:

            console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

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

        console.print("[hot_pink]Artículo agregado al inventario[hot_pink]")

    except ValueError as e:

        print("ERROR:", e)
from rich.table import Table
from rich.panel import Panel

def mostrar_inventario():

    console.print(
        Panel.fit(
            "[bold red]INVENTARIO DEL GIMNASIO[/bold red]",
            border_style="red"
        )
    )

    if len(inventario) == 0:

        console.print(
            "[bold yellow]No hay artículos en el inventario[/bold yellow]"
        )
        return

    stock_bajo = [
        a for a in inventario
        if a.cantidad <= a.stock_minimo
    ]

    if len(stock_bajo) > 0:

        console.print(
            f"[bold red]⚠ ARTÍCULOS CON STOCK BAJO ({len(stock_bajo)})[/bold red]"
        )

        for articulo in stock_bajo:

            console.print(
                f"[yellow]- {articulo.nombre}: "
                f"{articulo.cantidad} unidades "
                f"(mínimo: {articulo.stock_minimo})[/yellow]"
            )

    tabla = Table(
        title="📦 Inventario",
        show_header=True,
        header_style="bold cyan"
    )

    tabla.add_column("ID", justify="center")
    tabla.add_column("Artículo", style="green")
    tabla.add_column("Categoría", style="yellow")
    tabla.add_column("Cantidad", justify="center")
    tabla.add_column("Stock mínimo", justify="center")

    for articulo in inventario:

        cantidad = str(articulo.cantidad)

        if articulo.cantidad <= articulo.stock_minimo:
            cantidad = f"[bold red]{articulo.cantidad}[/bold red]"

        tabla.add_row(
            str(articulo.id),
            articulo.nombre,
            articulo.categoria,
            cantidad,
            str(articulo.stock_minimo)
        )

    console.print(tabla)

def editar_articulo():

    console.print("[pink1]\n===== EDITAR ARTÍCULO =====[/pink1]")

    if len(inventario) == 0:

        console.print("[hot_pink]No hay artículos en el inventario[/hot_pink]")
        return

    for articulo in inventario:

        console.print(f"[purple]{articulo.id} - {articulo.nombre} (cantidad: {articulo.cantidad})[/purple]")

    while True:

        try:

            ID = int(input("\nID del artículo a editar: "))

            articulo = buscar_articulo(ID)

            if articulo is not None:
                break

            console.print("[hot_pink]Artículo no encontrado[/hot_pink]")

        except ValueError:

            console.print("[hot_pink]ID inválido[/hot_pink]")

    print(articulo)

    console.print("[purple]¿Qué deseas editar?[/purple]")
    console.print("[purple]1. Nombre[/purple]")
    console.print("[purple]2. Categoría[/purple]")
    console.print("[purple]3. Cantidad[/purple]")
    console.print("[purple]4. Precio unitario[/purple]")
    console.print("[purple]5. Stock mínimo[/purple]")
    console.print("[purple]6. Descripción[/purple]")
    console.print("[purple]7. Cancelar[/purple]")

    opcion = input("Opción: ")

    if opcion == "1":

        nuevo_nombre = input("Nuevo nombre: ").strip()

        if nuevo_nombre == "":

            console.print("Nombre vacío")
            return

        for a in inventario:

            if a.nombre.lower() == nuevo_nombre.lower() and a.id != articulo.id:

                console.print("[hot_pink]Ya existe un artículo con ese nombre[/hot_pink]")
                return

        try:

            articulo.nombre = nuevo_nombre
            console.print("[hot_pink]Nombre actualizado[/hot_pink]")

        except ValueError as e:

            console.print("[red]ERROR:[/red]", e)

    elif opcion == "2":

        console.print("[pink1]\nCATEGORÍAS[/pink1]")

        for i, cat in enumerate(categorias_inventario, 1):
            console.print(f"[purple]{i}. {cat}[/purple]")

        while True:

            try:

                opcion_cat = int(input("Nueva categoría (número): "))

                if 1 <= opcion_cat <= len(categorias_inventario):

                    articulo.categoria = categorias_inventario[opcion_cat - 1]
                    console.print("[hot_pink]Categoría actualizada[/hot_pink]")
                    break

                console.print("[hot_pink]Opción inválida[/hot_pink]")

            except ValueError:

                console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

    elif opcion == "3":

        while True:

            try:

                nueva_cantidad = int(input("Nueva cantidad: "))

                if nueva_cantidad >= 0:

                    articulo.cantidad = nueva_cantidad
                    console.print("[hot_pink]Cantidad actualizada[/hot_pink]")

                    if nueva_cantidad <= articulo.stock_minimo:
                        console.print(f"⚠ Advertencia: la cantidad está por debajo del stock mínimo ({articulo.stock_minimo})")

                    break

                console.print("[hot_pink]La cantidad no puede ser negativa[/hot_pink]")

            except ValueError:

                console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

    elif opcion == "4":

        while True:

            try:

                nuevo_precio = float(input("Nuevo precio unitario ($): "))

                if nuevo_precio >= 0:

                    articulo.precio_unitario = nuevo_precio
                    console.print("[hot_pink]Precio actualizado[/hot_pink]")
                    break

                console.print("[hot_pink]El precio no puede ser negativo[/hot_pink]")

            except ValueError:

                console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

    elif opcion == "5":

        while True:

            try:

                nuevo_minimo = int(input("Nuevo stock mínimo: "))

                if nuevo_minimo >= 0:

                    articulo.stock_minimo = nuevo_minimo
                    print("[hot_pink]Stock mínimo actualizado[/hot_pink]")
                    break

                console.print("[hot_pink]El stock mínimo no puede ser negativo[hot_pink]")

            except ValueError:

                console.print("[hot_pink]Ingresa un número válido[/hot_pink]")

    elif opcion == "6":

        nueva_desc = input("Nueva descripción (Enter para dejar vacía): ").strip()
        articulo.descripcion = nueva_desc
        console.print("[hot_pink]Descripción actualizada[/hot_pink]")

    elif opcion == "7":

        console.print("[hot_pink]Edición cancelada[/hot_pink]")

    else:

        console.print("[hot_pink]Opción inválida[/hot_pink]")


def eliminar_articulo():

    console.print("[pink1]\n===== ELIMINAR ARTÍCULO =====[/pink1]")

    if len(inventario) == 0:

        console.print("[hot_pink]No hay artículos en el inventario[hot_pink]")
        return

    for articulo in inventario:

        console.print(f"[purple]{articulo.id} - {articulo.nombre}[/purple]")

    while True:

        try:

            ID = int(input("\nID del artículo a eliminar: "))

            articulo = buscar_articulo(ID)

            if articulo is not None:
                break

            console.print("[hot_pink]Artículo no encontrado[hot_pink]")

        except ValueError:

            console.print("[hot_pink]ID inválido[hot_pink]")

    console.print(f"\n¿Eliminar '{articulo.nombre}'? (s/n): ", end="")

    confirmacion = input().strip().lower()

    if confirmacion == "s":

        inventario.remove(articulo)
        console.print("[hot_pink]Artículo eliminado[hot_pink]")

    else:

        console.print("[hot_pink]Eliminación cancelada[/hot_pink]")
def menu_inventario():

# ================= MENÚ INVENTARIO =================
    while True:
        console.print(
    Panel.fit(
        "[pink1]MENÚ INVENTARIO[/pink1]",
        border_style="pink1"
    )
)
        console.print("[magenta]1. Agregar artículo[/magenta]")
        console.print("[magenta]2. Mostrar inventario[/magenta]")
        console.print("[magenta]3. Editar artículo[/magenta]")
        console.print("[magenta]4. Eliminar artículo[/magenta]")
        console.print("[magenta]5. Volver[/magenta]")

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
        console.print(
    Panel.fit(
        "[bold green]MENÚ USUARIOS[/bold green]",
        border_style="green"
    )
)
        console.print("[spring_green1]1. Registrar usuarios[/spring_green1]")
        console.print("[spring_green1]2. Volver[/spring_green1]")

        opcion = input("Opción: ")

        if opcion == "1":

            registrar_usuario()

        elif opcion == "2":

            break

        else:

            print("[bright_green]Opción inválida[/bright_pink]")


# ================= MENÚ CLASES =================

def menu_clases():

    while True:
        console.print(
    Panel.fit(
        "[blue]MENÚ INSCRIPCIONES[/blue]",
        border_style="blue"
        )
    ) 
        console.print("[cyan]1. Agregar clase[/cyan]")
        console.print("[cyan]2. Mostrar clases[/cyan]")
        console.print("[cyan]3. Modificar clase[/cyan]")
        console.print("[cyan]4. Eliminar clase[/cyan]")
        console.print("[cyan]5. Volver[/cyan]")

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

        console.print(
            Panel.fit(
                "[violet]MENÚ INSCRIPCIONES[/violet]",
                border_style="violet"
            )
        )

        console.print("[purple]1. Inscribir usuario[/purple]")
        console.print("[purple]2. Mostrar inscripciones[/purple]")
        console.print("[purple]3. Volver[/purple]")

        opcion = input("Opción: ")

        if opcion == "1":
            inscribir_usuario()

        elif opcion == "2":
            mostrar_inscripciones()

        elif opcion == "3":
            break

        else:
            print("Opción inválida")

console.print(
    Panel.fit(
        "[bold cyan]SISTEMA DE GESTIÓN DE GIMNASIO[/bold cyan]",
        border_style="green"
    )
)

for _ in track(
    range(100),
    description="Cargando sistema..."
):
    time.sleep(0.01)

# ================= MENÚ PRINCIPAL =================

while True:
    console.print(
    Panel.fit(
        "[bold yellow]GYM[/bold yellow]",
        border_style="bright_blue"
    )
)

    console.print("[green]1.[/green] Usuarios")
    console.print("[blue]2.[/blue] Gestionar clases")
    console.print("[violet]3.[/violet] Inscripciones")
    console.print("[yellow]4.[/yellow] Pagos")
    console.print("[orange3]5.[/orange3] Asistencias")
    console.print("[orange3]6.[/orange3] Reportes")
    console.print("[pink1]7.[/pink1] Inventario")
    console.print("[black]8.[/black] Salir")

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