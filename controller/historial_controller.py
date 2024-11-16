from termcolor import colored


from models.historial_model import Historial
from helpers.utils import limpiar_consola, volver_menu
from helpers.menu import ver_menu_historial


class HistorialController:

    @classmethod
    def inicio(cls):
        Historial.leer()
        limpiar_consola()
        while True:
            ver_menu_historial()
            eleccion = input(colored('\nElige una opción (0-3): ', 'yellow'))
            match eleccion:
                case '1':
                    cls.consultar()
                case '2':
                    cls.consultar()
                    cls.editar()
                case'3':
                    cls.consultar()
                    cls.borrar()
                case '0':
                    break
                case _:
                    print(
                        colored('\n_Opción no válida, porfavor intente de nuevo.', 'light_red'))
                    
    @classmethod
    def listar(cls):
        Historial.leer()
        return Historial.todo
        




    @classmethod
    def agregar(cls, nombre: str, operacion: str, editado: bool = False) -> list:
        funcion = nombre
        descripcion = operacion
        estado = editado
        registro_nuevo = Historial(funcion, descripcion, estado)
        Historial.todo.append(registro_nuevo)
        Historial.guardar
        print(colored(f'Entrada {funcion} agregada al historial', 'green'))
        return volver_menu()

    @classmethod
    def consultar(cls) -> list:
        limpiar_consola()
        if not Historial.todo:
            print(colored('Historial no disponible', 'light_red'))
            return volver_menu()
        else:
            print(colored('\n--- Historial ---\n',
                  'light_blue', attrs=['bold']))
            for index, entrada in enumerate(Historial.todo, start=1):
                estado_editado = '✔️' if entrada.editado else '❌'
                print(colored(f'{index}. {
                      entrada.nombre} - Editado: {estado_editado}', 'dark_grey'))
                print(colored(f'   Operacion: {entrada.operacion}', 'grey'))
            return volver_menu()

    @classmethod
    def editar(cls):
        if (Historial.todo):
            try:
                index = int(
                    input('Ingrece el índice a editar o 0 para salir: ')) - 1
                if (index < 0 or index >= len(Historial.todo)):
                    print(colored('Indice no disponible.', 'light_magenta'))
                    return volver_menu()
                entrada = Historial.todo[index]
                entrada.nombre = input(
                    f'Ingrese el nuevo nombre (actual: {entrada.nombre}): ') or entrada.nombre
                entrada.operacion = input(
                    f'Ingrese la nueva operación (actual: {entrada.operacion}): ') or entrada.operacion
                entrada.editado = True
                Historial.guardar
                print(
                    colored(f'"{entrada.nombre}" actualizada correctamente.', 'light_green'))
                return volver_menu()
            except ValueError:
                print(colored('Entrada errónea, porfavor ingrese un número.',
                              'light_red', attrs=['bold']))
            return volver_menu()

    @classmethod
    def borrar(cls):
        if (len(Historial.todo) > 0):
            try:
                index = int(
                    input('Ingrece el índice a editar o 0 para salir: ')) - 1
                if (index < 0 or index >= len(Historial.todo)):
                    print(colored('Indice no disponible.', 'light_magenta'))
                    return volver_menu()
                borrar_entrada = Historial.todo.pop(index)
                Historial.guardar
                print(colored(f'Entrada "{
                    borrar_entrada.nombre}" borrada correctamente.', on_color='on_red'))
                return volver_menu()
            except ValueError:
                print(colored('Entrada errónea, porfavor ingrese un número.',
                              'light_red', attrs=['bold']))
            return volver_menu()
