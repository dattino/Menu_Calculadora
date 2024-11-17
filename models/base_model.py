from abc import ABC, abstractmethod
from typing import List

from helpers.file_helpers import write_json_file, read_json_file


class Base(ABC):
    lista: List['Base'] = []
    filename = None

    @classmethod
    def __verificar_filename(cls):
        if (cls.filename is None) or (not cls.filename.endswith('.json')):
            raise Exception(
                '"Se debe definir un atributo filename en cada clase hija"'
            )

    @abstractmethod
    def parse_to_dict(self) -> dict:
        pass

    @classmethod
    def guardar(cls):
        cls.__verificar_filename()
        write_json_file(cls.filename, [item.parse_to_dict()
                        for item in cls.lista])

    @classmethod
    @abstractmethod
    def parse_from_dict(cls, item: dict) -> 'Base':
        pass

    @classmethod
    def leer(cls):
        cls.__verificar_filename()
        item_list: list[dict] = read_json_file(cls.filename)
        cls.lista = [cls.parse_from_dict(item) for item in item_list]
