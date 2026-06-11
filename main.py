from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.curso import Curso
from servicios.gestor_estudiantes import GestorEstudiantes
from servicios.gestor_cursos import GestorCursos
from servicios.estudiante_repositorio import EstudianteRepositorio
from servicios.curso_repositorio import CursoRepositorio
from servicios.matricula_repositorio import MatriculaRepositorio

gestor_estudiantes = GestorEstudiantes()
gestor_cursos = GestorCursos()
est_repo = EstudianteRepositorio()
cur_repo = CursoRepositorio()
mat_repo = MatriculaRepositorio()

def menu_estudiantes():
    while True:
        print("\n------Estudiantes-----")
        print("1. Registrar estudiante")
        print("2. Buscar estudiante")
        print("3. Listar estudiantes")
        print("4. Eliminar estudiante")
        print("5. Atras")
        option = input("Elegir opcion: ")

        if option == "1":
            try:
                identificacion = input("ID: ")
                nombre = input("Nombre: ")
                email = input("Email: ")
                codigo = input("Codigo: ")
                programa = input("Programa: ")
                estudiante = Estudiante(identificacion, nombre, email, codigo, programa)
                gestor_estudiantes.registrar(estudiante)
                est_repo.guardar(estudiante)
            except ValueError as e:
                print("Error:", e)

        elif option == "2":
            try:
                identificacion = input("Ingresar ID del estudiante: ")
                estudiante = gestor_estudiantes.buscar_por_id(identificacion)
                if estudiante:
                    estudiante.mostrar_info()
                else:
                    print("Estudiante no se encuentra")
            except Exception as e:
                print("Error:", e)

        elif option == "3":
            try:
                gestor_estudiantes.listar_todos()
            except Exception as e:
                print("Error:", e)

        elif option == "4":
            try:
                identificacion = input("Ingresar ID del estudiante para borrar: ")
                gestor_estudiantes.eliminar(identificacion)
                est_repo.eliminar(identificacion)
            except Exception as e:
                print("Error:", e)

        elif option == "5":
            break
        else:
            print("Opcion no valida")

def menu_cursos():
    while True:
        print("\n----Cursos-----")
        print("1. Registrar curso")
        print("2. Asignar docente a curso")
        print("3. Listar cursos")
        print("4. Eliminar curso")
        print("5. Atras")
        option = input("Elegir opcion: ")

        if option == "1":
            try:
                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                creditos = int(input("Creditos: "))
                cupo = int(input("Cupo maximo: "))
                curso = Curso(codigo, nombre, creditos, cupo)
                gestor_cursos.registrar_curso(curso)
                cur_repo.guardar(curso)
            except ValueError as e:
                print("Error:", e)

        elif option == "2":
            try:
                codigo_curso = input("Codigo del curso: ")
                curso = gestor_cursos.buscar_curso(codigo_curso)
                if curso:
                    identificacion = input("ID: ")
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    especialidad = input("Especialidad: ")
                    titulo = input("Titulo: ")
                    docente = Docente(identificacion, nombre, email, especialidad, titulo)
                    curso.asignar_docente(docente)
                    print("Docente asignado")
                else:
                    print("Curso no se encuentra")
            except ValueError as e:
                print("Error:", e)

        elif option == "3":
            try:
                gestor_cursos.listar_cursos()
            except Exception as e:
                print("Error:", e)

        elif option == "4":
            try:
                codigo = input("Ingresar codigo para eliminar curso: ")
                cur_repo.eliminar(codigo)
            except Exception as e:
                print("Error:", e)

        elif option == "5":
            break
        else:
            print("Opcion no valida")

def menu_matriculas():
    while True:
        print("\n----Matriculas-----")
        print("1. Matricular estudiante en curso")
        print("2. Agregar calificacion")
        print("3. Listar matriculas")
        print("4. Atras")
        option = input("Elegir opcion: ")

        if option == "1":
            try:
                identificacion = input("ID del estudiante: ")
                codigo_curso = input("Codigo del curso: ")
                estudiante = gestor_estudiantes.buscar_por_id(identificacion)
                curso = gestor_cursos.buscar_curso(codigo_curso)
                if estudiante and curso:
                    gestor_cursos.matricular(estudiante, curso)
                    matricula = gestor_cursos.buscar_matricula(identificacion, codigo_curso)
                    mat_repo.guardar(matricula)
                else:
                    print("Estudiante o curso no encontrado")
            except Exception as e:
                print("Error:", e)

        elif option == "2":
            identificacion = input("ID del estudiante: ")
            codigo_curso = input("Codigo del curso: ")
            matricula = gestor_cursos.buscar_matricula(identificacion, codigo_curso)
            if matricula:
                try:
                    actividad = input("Nombre de la actividad: ")
                    nota = float(input("Calificacion: "))
                    matricula.agregar_calificacion(actividad, nota)
                    print("Calificacion agregada, promedio:", matricula.promedio())
                except ValueError as e:
                    print("Error:", e)
            else:
                print("Matricula no encontrada")

        elif option == "3":
            gestor_cursos.listar_matriculas()

        elif option == "4":
            break
        else:
            print("Opcion no valida")

def menu_reportes():
    while True:
        print("\n----Reportes---")
        print("1. Listar estudiantes")
        print("2. Listar cursos")
        print("3. Listar matriculas")
        print("4. Atras")
        option = input("Elegir opcion: ")

        if option == "1":
            try:
                estudiantes = est_repo.listar_todos()
                for e in estudiantes:
                    e.mostrar_info()
            except Exception as e:
                print("Error:", e)
        elif option == "2":
            try:
                cursos = cur_repo.listar_todos()
                for c in cursos:
                    c.mostrar_info()
            except Exception as e:
                print("Error:", e)
        elif option == "3":
            try:
                gestor_cursos.listar_matriculas()
            except Exception as e:
                print("Error:", e)
        elif option == "4":
            break
        else:
            print("Opcion no valida")

while True:
    print("\n------SGA------")
    print("1. Estudiantes")
    print("2. Cursos")
    print("3. Matriculas")
    print("4. Reportes")
    print("5. Salir")
    option = input("Elegir opcion: ")

    if option == "1":
        menu_estudiantes()
    elif option == "2":
        menu_cursos()
    elif option == "3":
        menu_matriculas()
    elif option == "4":
        menu_reportes()
    elif option == "5":
        break
    else:
        print("Opcion no valida")