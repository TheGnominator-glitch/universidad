# SGA: Sistema de Gestion Academica

Sistema de gestion academica desarrollado en Python con conexion a Oracle, aplicando POO.

## Requerimientos

Python 3.x

Oracle Database XE (Oracle Express Edition)

oracledb libreria

## Instalacion

Instalar las desde cmd:

```
pip install oracledb
pip install pytest
pip install pylint
```

## Como preparar el DB

Correr el archivo `sga_universidad.sql` en Oracle SQL Developer. Esto crea todas las tablas necesarias.

Tambien crear el usuario de Oracle:

```
CREATE USER universidad IDENTIFIED BY pass123;
GRANT CONNECT, RESOURCE TO universidad;
ALTER USER universidad QUOTA UNLIMITED ON USERS;
```

## Como correr

1. Modificar `conexion.py` con sus credenciales de Oracle (Usuario, clave, etc...)
2. Correr `main.py` desde cmd

## Que hace?

1. Registrar y gestionar estudiantes
2. Registrar y gestionar cursos
3. Matricular estudiantes en cursos
4. Agregar calificaciones y calcular promedios
5. Generar reportes desde la base de datos

## Correr las pruebas

```
pytest pruebas/ -v
```

## Calidad de codigo

```
pylint modelos/ servicios
```
