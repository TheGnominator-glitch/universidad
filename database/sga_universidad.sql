-- SGA Universidad - Oracle Script

CREATE TABLE estudiantes (
    id VARCHAR2(20) PRIMARY KEY,
    nombre VARCHAR2(120) NOT NULL,
    email VARCHAR2(120) NOT NULL,
    codigo VARCHAR2(30) NOT NULL,
    programa VARCHAR2(120)
);

CREATE TABLE docentes (
    id VARCHAR2(20) PRIMARY KEY,
    nombre VARCHAR2(120) NOT NULL,
    email VARCHAR2(120) NOT NULL,
    especialidad VARCHAR2(120),
    titulo VARCHAR2(80)
);

CREATE TABLE cursos (
    codigo VARCHAR2(20) PRIMARY KEY,
    nombre VARCHAR2(120) NOT NULL,
    creditos INT DEFAULT 3,
    cupo_maximo INT DEFAULT 30,
    docente_id VARCHAR2(20),
    FOREIGN KEY (docente_id) REFERENCES docentes(id)
);

CREATE TABLE matriculas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    estudiante_id VARCHAR2(20) NOT NULL,
    curso_codigo VARCHAR2(20) NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_codigo) REFERENCES cursos(codigo),
    UNIQUE (estudiante_id, curso_codigo)
);

CREATE TABLE calificaciones (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    matricula_id INT NOT NULL,
    actividad VARCHAR2(80) NOT NULL,
    nota DECIMAL(3,1) NOT NULL,
    CONSTRAINT chk_nota CHECK (nota >= 0.0 AND nota <= 5.0),
    FOREIGN KEY (matricula_id) REFERENCES matriculas(id) ON DELETE CASCADE
);
