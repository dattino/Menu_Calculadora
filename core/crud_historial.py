from helpers.utils import limpiar_consola
from helpers.menu import vista_menu_historial, volver_menu


from termcolor import colored


def controlador_historial(historial):
    while True:
        vista_menu_historial()
        eleccion = input(colored('\nElige una opción (0-3): ', 'yellow'))
        match eleccion:
            case '1':
                ver_historial(historial)
            case '2':
                editar_historial(historial)
            case'3':
                borrar_historial(historial)
            case '0':
                break
            case _:
                print(
                    colored('\n_Opción no válida, porfavor intente de nuevo.', 'light_red'))


def ver_historial(historial):
    limpiar_consola()

    print(colored('\n--- Historial ---\n', 'light_blue', attrs=['bold',]))
    for index, entrada in enumerate(historial, start=1):
        fue_editado = '✔️' if entrada['editado'] else '❌'
        print(f'{index}. {entrada['nombre']} - Editado: {fue_editado}')
        print(f'   Operación: {entrada['operación']}')
    return volver_menu()


def agregar_historial(historial, nombre_aplicacion: str, resultado_almacenar: str):
    funcion = nombre_aplicacion
    descripcion = resultado_almacenar
    entrada = {
        'nombre': funcion,
        'operación': descripcion,
        'editado': False,
    }
    historial.append(entrada)
    print(colored(f'Entrada {funcion} agregada al historial', 'green'))
    return volver_menu()


def editar_historial(historial):
    ver_historial(historial)

    try:
        index = int(input('>Ingrece el índice a editar: ')) - 1
        if index < 0 or index >= len(historial):
            print('Indice no disponible.')
            return volver_menu()

        entrada = historial[index]
        entrada['nombre'] = input(
            f'Ingrese el nuevo nombre (actual: {entrada['nombre']}): ') or entrada['nombre']
        entrada['operación'] = input(
            f'Ingrese la nueva operación (actual: {entrada['operación']}): ') or entrada['operación']
        entrada['editado'] = True

        print(f'TODO "{entrada["nombre"]}" actualizada correctamente.')
    except ValueError:
        print('Entrada errónea, porfavor ingrese un número.')
    return volver_menu()


def borrar_historial(historial):
    ver_historial(historial)

    try:
        index = int(input('Ingrese el índice a borrar: ')) - 1
        if index < 0 or index >= len(historial):
            print('Indice no disponible.')
            return volver_menu()

        borrar_entrada = historial.pop(index)
        print(f'Entrada "{borrar_entrada["nombre"]}" borrada correctamente.')
    except ValueError:
        print('Entrada errónea, porfavor ingrese un número.')
    return volver_menu()