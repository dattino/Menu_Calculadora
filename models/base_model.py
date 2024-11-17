from helpers.file_helpers import write_json_file, read_json_file


class Base:
    lista: list = []
    filename = ''

    @classmethod
    def guardar(cls):
        write_json_file(cls.filename,
                        [historial.__dict__ for historial in cls.lista]
        )

    @classmethod
    def leer(cls):
        for historial_dict in read_json_file(cls.filename):
            historial_obj = cls(
                nombre=historial_dict['nombre'],
                operacion=historial_dict['operacion'],
                editado=historial_dict['editado']
            )
            cls.lista.append(historial_obj)
