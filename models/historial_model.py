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

    def parse_to_dict(self) -> dict:
        return {
            'nombre': self.__nombre,
            'operacion': self.operacion,
            'editado': self.editado,
        }

    @classmethod
    def parse_from_dict(cls, item: dict) -> 'Historial':
        #return cls(nombre=item['nombre'], peracion=item['operacion'], editado=item['editado'])
        return cls(**item)