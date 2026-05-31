import oracledb

class Estudiante:
    def __init__(self, codigo, nombre, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.programa = programa

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

config = {
    "user": "universidad",
    "password": "pass123",
    "dsn": "localhost:1521/XEPDB1"
}

repo = EstudianteRepositorioOracle(config)
#repo.guardar(Estudiante("2026-001", "Laura Gomez", "Systems Engineering"))

estudiante = repo.buscar_por_codigo("2026-001")
print("Found:", estudiante.nombre, estudiante.programa)