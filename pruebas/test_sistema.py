import pytest
import sys
sys.path.insert(0, '..')

from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.calificacion import Calificacion
from modelos.matricula import Matricula
from modelos.curso import Curso

def test_estudiante_valido():
    est = Estudiante("EST001", "X", "X@email.com", "2026-001", "Systems")
    assert est.get_nombre() == "X"

def test_calificacion_invalida():
    with pytest.raises(ValueError):
        Calificacion("Parcial", 6.0)

def test_calificacion_valida():
    cal = Calificacion("Parcial", 4.0)
    assert cal.get_nota() == 4.0

def test_promedio_correcto():
    est = Estudiante("EST001", "X", "X@email.com", "2026-001", "Systems")
    cur = Curso("C001", "P", 3, 30)
    mat = Matricula(est, cur)
    mat.agregar_calificacion("Parcial", 4.0)
    mat.agregar_calificacion("Final", 5.0)
    assert mat.promedio() == 4.5

def test_mostrar_info_polimorfismo():
    est = Estudiante("EST001", "X", "X@email.com", "2026-001", "Systems")
    doc = Docente("DOC001", "Y", "Y@email.com", "POO", "Phd")
    assert est.get_codigo() != doc.get_especialidad()
