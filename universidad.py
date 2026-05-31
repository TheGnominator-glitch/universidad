from dataclasses import dataclass
import oracledb

@dataclass
class Estudiante:
    codigo: str
    nombre: str
    programa: str

class EstudianteRepositorioOracle:
    def __init__(self, config):
        self.config = config

    def guardar(self, estudiante):
        sql = "INSERT INTO estudiantes (codigo, nombre, programa) VALUES (:1, :2, :3)"
        conexion = oracledb.connect(**self.config)
        cursor = conexion.cursor()
        cursor.execute(sql, (estudiante.codigo, estudiante.nombre, estudiante.programa))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Student saved:", estudiante.nombre)

    def buscar_por_codigo(self, codigo):
        sql = "SELECT codigo, nombre, programa FROM estudiantes WHERE codigo = :1"
        conexion = oracledb.connect(**self.config)
        cursor = conexion.cursor()
        cursor.execute(sql, (codigo,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()
        if fila:
            return Estudiante(fila[0], fila[1], fila[2])
        return None

    def mostrar_todos(self):
        sql = "SELECT codigo, nombre, programa FROM estudiantes"
        conexion = oracledb.connect(**self.config)
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        print("Students")
        for fila in filas:
            print("Code:", fila[0], "Name:", fila[1], "Program:", fila[2])

config = {
    "user": "universidad",
    "password": "pass123",
    "dsn": "localhost:1521/XEPDB1"
}

repo = EstudianteRepositorioOracle(config)

# Insert students
repo.guardar(Estudiante("2026-001", "Laura Gomez", "Systems Engineering"))
repo.guardar(Estudiante("2026-002", "Y", "Business"))
repo.guardar(Estudiante("2026-003", "Z", "Math"))

# Search by code
estudiante = repo.buscar_por_codigo("2026-001")
print("\nFound:", estudiante.nombre, estudiante.programa)

# Show all
repo.mostrar_todos()
