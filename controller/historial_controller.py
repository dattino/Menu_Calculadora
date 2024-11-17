from termcolor import colored


from models.historial_model import Historial
from helpers.utils import limpiar_consola, volver_menu
from helpers.menu import ver_menu_historial


class HistorialController:
    @classmethod
    def inicio(cls):
        if not Historial.lista:
            Historial.leer()
        while True:
            limpiar_consola()
            ver_menu_historial()
            eleccion = input(
                colored('\nElige una opción (0-3): ', 'yellow'))
            match eleccion:
                case '1':
                    limpiar_consola()
                    cls.consultar()
                    volver_menu()
                case '2':
                    limpiar_consola()
                    cls.consultar()
                    cls.editar()
                    volver_menu()
                case'3':
                    limpiar_consola()
                    cls.consultar()
                    cls.borrar()
                    volver_menu()
                case '0':
                    limpiar_consola()
                    break
                case _:
                    limpiar_consola()
                    print(
                        colored(
                            '\nOpción no válida, porfavor intente de nuevo.', 'light_red')
                    )
                    volver_menu()

    @classmethod
    def agregar(cls, nombre: str, operacion: str) -> list:
        nombre = nombre
        operacion = operacion
        registro = Historial(nombre, operacion)
        Historial.lista.append(registro)
        Historial.guardar()
        print(
            colored(f'Entrada {nombre} agregada al historial', 'green')
        )
        return

    @classmethod
    def consultar(cls) -> list:
        if not Historial.lista:
            print(
                colored('Historial no disponible', 'light_red')
            )
            return
        else:
            print(
                colored('\n--- Historial ---\n', 'light_blue', attrs=['bold'])
            )
            for index, entrada in enumerate(Historial.lista, start=1):
                estado_editado = '✔️' if entrada.editado else '❌'
                print(
                    colored(
                        f'{index}. {
                            entrada.nombre} - Editado: {estado_editado}', 'dark_grey'
                    )
                )
                print(
                    colored(f'   Operacion: {entrada.operacion}', 'grey')
                )

    @classmethod
    def editar(cls):
        if (Historial.lista):
            try:
                index = int(
                    input('\nIngrece el índice a editar o 0 para salir: ')) - 1
                if (index < -1 or index >= len(Historial.lista)):
                    print(colored('Indice no disponible.', 'light_magenta'))
                    return HistorialController.editar()
                elif (index > -1 or index >= len(Historial.lista)):
                    entrada = Historial.lista[index]
                    entrada.nombre = input(
                        f'Ingrese el nuevo nombre (actual: {entrada.nombre}): ') or entrada.nombre
                    entrada.operacion = input(
                        f'Ingrese la nueva operación (actual: {entrada.operacion}): ') or entrada.operacion
                    entrada.editado = True
                    Historial.guardar()
                    print(
                        colored(
                            f'"{entrada.nombre}" actualizada correctamente.', 'light_green')
                    )
                    return
                elif (index == -1):
                    return
            except ValueError:
                mensaje_error = 'Entrada errónea, porfavor ingrese un número.'
                print(
                    colored(mensaje_error, 'light_red', attrs=['bold'])
                )
                return HistorialController.editar()

    @classmethod
    def borrar(cls):
        if (len(Historial.lista) > 0):
            try:
                index = int(
                    input('\nIngrece el índice a editar o 0 para salir: ')) - 1
                if (index < -1 or index >= len(Historial.lista)):
                    print(
                        colored('Indice no disponible.', 'light_magenta')
                    )
                    return HistorialController.borrar()
                elif (index == -1):
                    return
                else:
                    borrar_entrada = Historial.lista.pop(index)
                    Historial.guardar()
                    print(
                        colored(
                            f'Entrada "{borrar_entrada.nombre}" borrada correctamente.', on_color='on_red'
                        )
                    )
                    return
            except ValueError:
                print(
                    colored('Entrada errónea, porfavor ingrese un número.',
                            'light_red', attrs=['bold']
                            )
                )
            return HistorialController.borrar()

    @classmethod
    def ver(cls):
        if not Historial.lista:
            Historial.leer()
