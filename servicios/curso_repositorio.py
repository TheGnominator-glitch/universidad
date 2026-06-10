from database.conexion import obtener_conexion
from modelos.curso import Curso

class CursoRepositorio:
    def guardar(self, curso):
        sql = "INSERT INTO TBL_CURSOS VALUES (:1, :2, :3, :4, :5)"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        docente_id = curso.get_docente().get_identificacion() if curso.get_docente() else None
        cursor.execute(sql, (curso.get_codigo(), curso.get_nombre(), curso.get_creditos(), curso.get_cupo_maximo(), docente_id))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Course saved:", curso.get_nombre())

    def buscar_por_codigo(self, codigo):
        sql = "SELECT * FROM TBL_CURSOS WHERE codigo = :1"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (codigo,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()
        if fila:
            return Curso(fila[0], fila[1], fila[2], fila[3])
        return None

    def listar_todos(self):
        sql = "SELECT * FROM TBL_CURSOS ORDER BY nombre"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        cursos = []
        for fila in filas:
            cursos.append(Curso(fila[0], fila[1], fila[2], fila[3]))
        return cursos

    def eliminar(self, codigo):
        sql = "DELETE FROM TBL_CURSOS WHERE codigo = :1"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (codigo,))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Course deleted:", codigo)
