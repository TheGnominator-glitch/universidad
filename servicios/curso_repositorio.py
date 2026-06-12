from database.conexion import obtener_conexion
from modelos.curso import Curso
from modelos.docente import Docente

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
        print("Curso guardado:", curso.get_nombre())
        
    def guardar_docente(self, docente):
        sql = "INSERT INTO TBL_DOCENTES VALUES (:1, :2, :3, :4, :5)"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (docente.get_identificacion(), docente.get_nombre(), docente.get_email(), docente.get_especialidad(), docente.get_titulo()))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Docente guardado")

    def actualizar_docente(self, curso):
        sql = "UPDATE TBL_CURSOS SET docente_id = :1 WHERE codigo = :2"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        docente_id = curso.get_docente().get_identificacion()
        cursor.execute(sql, (docente_id, curso.get_codigo()))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Docente actualizado")

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
        sql = "SELECT c.codigo, c.nombre, c.creditos, c.cupo_maximo, d.id, d.nombre, d.email, d.especialidad, d.titulo FROM TBL_CURSOS c LEFT JOIN TBL_DOCENTES d ON c.docente_id = d.id ORDER BY c.nombre"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        cursos = []
        for fila in filas:
            curso = Curso(fila[0], fila[1], fila[2], fila[3])
            if fila[4]:
                docente = Docente(fila[4], fila[5], fila[6], fila[7], fila[8])
                curso.asignar_docente(docente)
            cursos.append(curso)
        return cursos

    def eliminar(self, codigo):
        sql = "DELETE FROM TBL_CURSOS WHERE codigo = :1"
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql, (codigo,))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Curso eliminado:", codigo)