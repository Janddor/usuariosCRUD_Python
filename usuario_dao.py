from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario


class UsuarioDAO:
    '''
    DAO - DATA ACCES OBJECT para la tabla de usuario
    CRUD - Create, Read, Update, Delete para la tabla de usuario
    '''
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = [] #lista de usuarios
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2]) #objeto individual usuarios
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password) #tupla de valores que están como %s
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario._id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario._id_usuario,)#la comma es para que sea una tupla.
            cursor.execute(cls._ELIMINAR, valores)#solo tiene un parámetro posicional %s
            return cursor.rowcount

