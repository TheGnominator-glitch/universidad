from database.conexion import obtener_conexion
from modelos.estudiante import Estudiante

class EstudianteRepositorio:
    def guardar(self, estudiante):
        sql = "INSERT INTO TBL_ESTUDIANTES VALUES (:1, :2, :3, :4, :5)"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (estudiante.get_identificacion(), estudiante.get_nombre(), estudiante.get_email(), estudiante.get_codigo(), estudiante.get_programa()))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Student saved:", estudiante.get_nombre())

    def buscar_por_id(self, identificacion):
        sql = "SELECT * FROM TBL_ESTUDIANTES WHERE id = :1"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (identificacion,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()
        if fila:
            return Estudiante(fila[0], fila[1], fila[2], fila[3], fila[4])
        return None

    def listar_todos(self):
        sql = "SELECT * FROM TBL_ESTUDIANTES ORDER BY nombre"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        estudiantes = []
        for fila in filas:
            estudiantes.append(Estudiante(fila[0], fila[1], fila[2], fila[3], fila[4]))
        return estudiantes

    def eliminar(self, identificacion):
        sql = "DELETE FROM TBL_ESTUDIANTES WHERE id = :1"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (identificacion,))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Student deleted:", identificacion)