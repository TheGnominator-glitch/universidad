# Python-Oracle conexion

Esto es una demostracion de la conexion de Python con el DB de Oracle

# INSTRUCCIONES DE USO


## Requerimientos

Python 3.x

Oracle Database XE (Oracle Express Edition)

oracledb libreria

## Installacion:

Installar el connector en cmd

`pip install oracledb`


## Como preparer el DB

Correr el siguiente codigo en Oracle SQL Developer

```
CREATE USER universidad IDENTIFIED BY pass123;
GRANT CONNECT, RESOURCE TO universidad;
ALTER USER universidad QUOTA UNLIMITED ON USERS;

CREATE TABLE universidad.estudiantes (
    codigo VARCHAR2(20) PRIMARY KEY,
    nombre VARCHAR2(120) NOT NULL,
    programa VARCHAR2(120) NOT NULL
);
```

## Como correr

1. Modificar la seccion de "config" en el archivo con sus propios credenciales de Oracle (Usuario, clave, etc...)
2. Correr el archivo desde cmd

## Que hace?

1. Insertar estudiantes en un DB
2. Muestra los estudiantes en la tabla