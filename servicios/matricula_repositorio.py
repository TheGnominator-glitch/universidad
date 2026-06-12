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

    def guardar_calificacion(self, estudiante_id, curso_codigo, actividad, nota):
        sql_find = "SELECT id FROM TBL_MATRICULAS WHERE estudiante_id = :1 AND curso_codigo = :2"
        sql_insert = "INSERT INTO TBL_CALIFICACIONES (matricula_id, actividad, nota) VALUES (:1, :2, :3)"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql_find, (estudiante_id, curso_codigo))
        fila = cursor.fetchone()
        if fila:
            cursor.execute(sql_insert, (fila[0], actividad, nota))
            conexion.commit()
            print("Calificacion guardada")
        cursor.close()
        conexion.close()

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