import oracledb

CONFIG_BD = {
    "user": "universidad",
    "password": "pass123",
    "dsn": "localhost:1521/XEPDB1"
}

def obtener_conexion():
    try:
        return oracledb.connect(**CONFIG_BD)
    except oracledb.Error as e:
        raise ConnectionError("Could not connect to database: " + str(e))