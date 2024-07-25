from Conexion import Conexion
from logger_base import log
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exception_type, exception_val, exception_tb):
        log.debug('Se ejecuta método __exit__')
        if exception_val:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción, se hace rollback: {exception_val} {exception_type} {exception_tb}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la trasacción, se hace commit')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.info(f'Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario ORDER BY id_usuario')
        log.info(cursor.fetchall())


