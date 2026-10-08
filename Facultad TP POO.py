class Alumno:
    def __init__(self, nombre, apellido, legajo, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.carrera = carrera
        self.materias = []

    def inscribirse(self, materia):
        self.materias.append(materia)

    def abandonar(self, materia):
        if materia in self.materias:
            self.materias.remove(materia)


class Materia:
    def __init__(self, nombre, codigo, docente, cupo):
        self.nombre = nombre
        self.codigo = codigo
        self.docente = docente
        self.cupo = cupo
        self.alumnos = []

    def tiene_cupo(self):
        return len(self.alumnos) < self.cupo

    def agregar_alumno(self, alumno):
        if self.tiene_cupo():
            self.alumnos.append(alumno)
            return True
        return False

    def quitar_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            return True
        return False


class Universidad:
    def __init__(self):
        self.alumnos = []
        self.materias = []

    def buscar_alumno(self, legajo):
        for alumno in self.alumnos:
            if alumno.legajo == legajo:
                return alumno
        return None

    def buscar_materia(self, codigo):
        for materia in self.materias:
            if materia.codigo == codigo:
                return materia
        return None

    def registrar_alumno(self):
        print("\n--- REGISTRO DE ALUMNO ---")

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        legajo = input("Numero de legajo: ")
        carrera = input("Carrera: ")

        if not legajo.isdigit():
            print("Error: el legajo debe contener solamente numeros.")
            return

        if self.buscar_alumno(legajo) is not None:
            print("Error: ya existe un alumno con ese legajo.")
            return

        alumno = Alumno(nombre, apellido, legajo, carrera)
        self.alumnos.append(alumno)

        print("Alumno registrado correctamente.")

    def registrar_materia(self):
        print("\n--- REGISTRO DE MATERIA ---")

        nombre = input("Nombre de la materia: ")
        codigo = input("Codigo: ")
        docente = input("Docente: ")
        cupo = input("Cantidad maxima de alumnos: ")

        if self.buscar_materia(codigo) is not None:
            print("Error: ya existe una materia con ese codigo.")
            return

        if not cupo.isdigit():
            print("Error: el cupo debe ser un numero.")
            return

        cupo = int(cupo)

        if cupo <= 0:
            print("Error: el cupo debe ser mayor que cero.")
            return

        materia = Materia(nombre, codigo, docente, cupo)
        self.materias.append(materia)

        print("Materia registrada correctamente.")

    def realizar_inscripcion(self):
        print("\n--- INSCRIPCION ---")

        legajo = input("Legajo del alumno: ")

        if not legajo.isdigit():
            print("Error: el legajo debe contener solamente numeros.")
            return

        alumno = self.buscar_alumno(legajo)

        if alumno is None:
            print("Error: no se encontro el alumno.")
            return

        codigo = input("Codigo de la materia: ")
        materia = self.buscar_materia(codigo)

        if materia is None:
            print("Error: no se encontro la materia.")
            return

        if materia in alumno.materias:
            print("Error: el alumno ya esta inscripto.")
            return

        if materia.agregar_alumno(alumno):
            alumno.inscribirse(materia)
            print("Inscripcion realizada correctamente.")
        else:
            print("Error: la materia no tiene cupos disponibles.")

    def cancelar_inscripcion(self):
        print("\n--- BAJA DE MATERIA ---")

        legajo = input("Legajo del alumno: ")

        if not legajo.isdigit():
            print("Error: el legajo debe contener solamente numeros.")
            return

        alumno = self.buscar_alumno(legajo)

        if alumno is None:
            print("Error: no se encontro el alumno.")
            return

        codigo = input("Codigo de la materia: ")
        materia = self.buscar_materia(codigo)

        if materia is None:
            print("Error: no se encontro la materia.")
            return

        if materia.quitar_alumno(alumno):
            alumno.abandonar(materia)
            print("El alumno fue dado de baja correctamente.")
        else:
            print("Error: el alumno no estaba inscripto en esa materia.")

    def listar_materias(self):
        print("\n========== MATERIAS ==========")

        if not self.materias:
            print("No hay materias registradas.")
            return

        for materia in self.materias:
            cantidad = len(materia.alumnos)
            libres = materia.cupo - cantidad

            print("\nMateria:", materia.nombre)
            print("Codigo:", materia.codigo)
            print("Docente:", materia.docente)
            print("Cupo total:", materia.cupo)
            print("Alumnos inscriptos:", cantidad)
            print("Cupos libres:", libres)

    def listar_alumnos(self):
        print("\n========== ALUMNOS ==========")

        if not self.alumnos:
            print("No hay alumnos registrados.")
            return

        for alumno in self.alumnos:
            print("\nNombre:", alumno.nombre)
            print("Apellido:", alumno.apellido)
            print("Legajo:", alumno.legajo)
            print("Carrera:", alumno.carrera)

            if len(alumno.materias) == 0:
                print("Materias inscriptas: Ninguna")
            else:
                print("Materias inscriptas:")

                for materia in alumno.materias:
                    print("-", materia.nombre, "| Codigo:", materia.codigo)


def mostrar_opciones():
    print("\n========== SISTEMA ACADEMICO ==========")
    print("1. Registrar alumno")
    print("2. Registrar materia")
    print("3. Inscribir alumno")
    print("4. Cancelar inscripcion")
    print("5. Mostrar materias")
    print("6. Mostrar alumnos")
    print("7. Salir")


def main():
    universidad = Universidad()

    while True:
        mostrar_opciones()

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            universidad.registrar_alumno()

        elif opcion == "2":
            universidad.registrar_materia()

        elif opcion == "3":
            universidad.realizar_inscripcion()

        elif opcion == "4":
            universidad.cancelar_inscripcion()

        elif opcion == "5":
            universidad.listar_materias()

        elif opcion == "6":
            universidad.listar_alumnos()

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opcion incorrecta.")


main()