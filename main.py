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
        print("\n------Students-----")
        print("1. Register student")
        print("2. Search for student")
        print("3. List all students")
        print("4. Delete student")
        print("5. Back")
        option = input("Select option: ")

        if option == "1":
            try:
                identificacion = input("ID: ")
                nombre = input("Name: ")
                email = input("Email: ")
                codigo = input("Code: ")
                programa = input("Program: ")
                estudiante = Estudiante(identificacion, nombre, email, codigo, programa)
                gestor_estudiantes.registrar(estudiante)
                est_repo.guardar(estudiante)
            except ValueError as e:
                print("Error:", e)

        elif option == "2":
            try:
                identificacion = input("Enter student ID: ")
                estudiante = gestor_estudiantes.buscar_por_id(identificacion)
                if estudiante:
                    estudiante.mostrar_info()
                else:
                    print("Student not found")
            except Exception as e:
                print("Error:", e)

        elif option == "3":
            try:
                gestor_estudiantes.listar_todos()
            except Exception as e:
                print("Error:", e)

        elif option == "4":
            try:
                identificacion = input("Enter student ID to delete: ")
                gestor_estudiantes.eliminar(identificacion)
                est_repo.eliminar(identificacion)
            except Exception as e:
                print("Error:", e)

        elif option == "5":
            break
        else:
            print("Invalid option")

def menu_cursos():
    while True:
        print("\n----Courses-----")
        print("1. Register course")
        print("2. Assign teacher to course")
        print("3. List all courses")
        print("4. Delete course")
        print("5. Back")
        option = input("Select option: ")

        if option == "1":
            try:
                codigo = input("Code: ")
                nombre = input("Name: ")
                creditos = int(input("Credits: "))
                cupo = int(input("Max capacity: "))
                curso = Curso(codigo, nombre, creditos, cupo)
                gestor_cursos.registrar_curso(curso)
                cur_repo.guardar(curso)
            except ValueError as e:
                print("Error:", e)

        elif option == "2":
            try:
                codigo_curso = input("Course code: ")
                curso = gestor_cursos.buscar_curso(codigo_curso)
                if curso:
                    identificacion = input("Teacher ID: ")
                    nombre = input("Teacher name: ")
                    email = input("Teacher email: ")
                    especialidad = input("Specialty: ")
                    titulo = input("Title: ")
                    docente = Docente(identificacion, nombre, email, especialidad, titulo)
                    curso.asignar_docente(docente)
                    print("Teacher assigned successfully")
                else:
                    print("Course not found")
            except ValueError as e:
                print("Error:", e)

        elif option == "3":
            try:
                gestor_cursos.listar_cursos()
            except Exception as e:
                print("Error:", e)

        elif option == "4":
            try:
                codigo = input("Enter course code to delete: ")
                cur_repo.eliminar(codigo)
            except Exception as e:
                print("Error:", e)

        elif option == "5":
            break
        else:
            print("Invalid option")

def menu_matriculas():
    while True:
        print("\n----Enrollment-----")
        print("1. Enroll student in course")
        print("2. Add grade")
        print("3. List all enrollments")
        print("4. Back")
        option = input("Select option: ")

        if option == "1":
            try:
                identificacion = input("Student ID: ")
                codigo_curso = input("Course code: ")
                estudiante = gestor_estudiantes.buscar_por_id(identificacion)
                curso = gestor_cursos.buscar_curso(codigo_curso)
                if estudiante and curso:
                    gestor_cursos.matricular(estudiante, curso)
                    matricula = gestor_cursos.buscar_matricula(identificacion, codigo_curso)
                    mat_repo.guardar(matricula)
                else:
                    print("Student or course not found")
            except Exception as e:
                print("Error:", e)

        elif option == "2":
            identificacion = input("Student ID: ")
            codigo_curso = input("Course code: ")
            matricula = gestor_cursos.buscar_matricula(identificacion, codigo_curso)
            if matricula:
                try:
                    actividad = input("Activity name: ")
                    nota = float(input("Grade: "))
                    matricula.agregar_calificacion(actividad, nota)
                    print("Grade added, average:", matricula.promedio())
                except ValueError as e:
                    print("Error:", e)
            else:
                print("Enrollment not found")

        elif option == "3":
            gestor_cursos.listar_matriculas()

        elif option == "4":
            break
        else:
            print("Invalid option")

def menu_reportes():
    while True:
        print("\n----Reports---")
        print("1. List all students")
        print("2. List all courses")
        print("3. List all enrollments")
        print("4. Back")
        option = input("Select option: ")

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
            print("Invalid option")

while True:
    print("\n------SGA------")
    print("1. Students")
    print("2. Courses")
    print("3. Enrollments")
    print("4. Reports")
    print("5. Exit")
    option = input("Select option: ")

    if option == "1":
        menu_estudiantes()
    elif option == "2":
        menu_cursos()
    elif option == "3":
        menu_matriculas()
    elif option == "4":
        menu_reportes()
    elif option == "5":
        print("Exiting system")
        break
    else:
        print("Invalid option")