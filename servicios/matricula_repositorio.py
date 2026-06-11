from database.conexion import obtener_conexion

class MatriculaRepositorio:
    def guardar(self, matricula):
        sql = "INSERT INTO TBL_MATRICULAS (estudiante_id, curso_codigo) VALUES (:1, :2)"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (matricula.get_estudiante().get_identificacion(), matricula.get_curso().get_codigo()))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Matricula guardado")

    def listar_todos(self):
        sql = "SELECT * FROM TBL_MATRICULAS"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas

    def eliminar(self, matricula_id):
        sql = "DELETE FROM TBL_MATRICULAS WHERE id = :1"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (matricula_id,))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Matricula eliminado", matricula_id)