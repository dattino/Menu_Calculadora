from config import constants

from .base_model import Base


class Historial(Base):
    filename = constants.HISTORIAL_PATH

    def __init__(self, nombre: str, operacion: str, editado: bool = False) -> None:
        self.__nombre = nombre
        self.operacion = operacion
        self.editado = editado

    @property
    def nombre(self):
        return self.__nombre.title()

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise Exception('Nombre inválido')
        self.__nombre = nuevo_nombre

    @property
    def __dict__(self):
        return {
            'nombre': self.__nombre,
            'operacion': self.operacion,
            'editado': self.editado,
        }
