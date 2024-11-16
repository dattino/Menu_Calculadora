from typing import List


from helpers.file_helpers import write_json_file, read_json_file
from config import constants


class Historial:
    todo: List['Historial'] = []

    def __init__(self, nombre: str, operacion: str, editado: bool = False) -> None:
        self.nombre = nombre
        self.operacion = operacion
        self.editado = editado

    @classmethod
    def guardar(cls):
        write_json_file(constants.HISTORIAL_PATH, [historial.__dict__ for historial in cls.todo])

    @classmethod
    def leer(cls):
        for historial_dict in read_json_file(constants.HISTORIAL_PATH):
            historial_obj = Historial(
                nombre = historial_dict['nombre'], operacion = historial_dict['operacion'], editado = historial_dict['editado'])
            cls.todo.append(historial_obj)
