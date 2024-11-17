from config import constants

from .historial_base_model import HistorialBase


class CalculadoraHistorial(HistorialBase):
    filename = constants.HISTORIAL_PATH

    def __init__(self, nombre: str, operacion: str, editado: bool = False) -> None:
        super().__init__(editado)
        self.__nombre = nombre
        self.operacion = operacion
        self.editado = editado

    @property
    def nombre(self):
        return self.__nombre.title()
    
    def __str__(self):
        estado_editado = '✔️' if self.editado else '❌'
        return f'{self.nombre}  |  Modificado: {estado_editado}\n   {self.operacion}'

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
    def parse_from_dict(cls, item: dict) -> 'CalculadoraHistorial':
        #return cls(nombre=item['nombre'], peracion=item['operacion'], editado=item['editado'])
        return cls(**item)