import os


def limpiar_consola():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def vista_menu():
    print('\n--- Menú Calculadora ---')
    print('1. Calculadora Simple')
    print('2. Calcular promedio')
    print('3. Calcular área de un círculo')
    print('4. Comprobar el Mayor de 3 n°')
    print('5. Comprobar Año bisiesto')
    print('6. Historial')
    print('0. Salir')


def vista_menu_historial():
    print('\n--- Menú Historial ---')
    print('1. Ver Historial')
    print('2. Editar Historial')
    print('3. Borar Entrada del Historial')
    print('0. Volver')


def volver_menu():
    input('\nPresione "Enter" para continuar...')
    return limpiar_consola()


def agregar_historial(historial, nombre_aplicacion: str, resultado_almacenar: str):
    funcion = nombre_aplicacion
    descripcion = resultado_almacenar
    entrada = {
        'nombre': funcion,
        'operación': descripcion,
        'editado': False,
    }
    historial.append(entrada)
    print(f'Entrada {funcion} agregada al historial')
    return volver_menu()


def ver_historial(historial):
    limpiar_consola()
    if not historial:
        print('Historial no disponible.')
        return

    for index, entrada in enumerate(historial, start=1):
        fue_editado = '✔️' if entrada['editado'] else '❌'
        print(f'{index}. {entrada['nombre']} - Editado: {fue_editado}')
        print(f'   Operación: {entrada['operación']}')
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


def calculadora_simple(historial):
    limpiar_consola()
    num_1 = int(input('Ingrese un número '))
    operacion = input('Ingrese una operacion matemética (+, -, *, /) ')
    num_2 = int(input('Ingrese un segundo número '))
    resultado = ''
    match  operacion:
        case '+':
            resultado = (f'{num_1} + {num_2} = {num_1 + num_2}')
        case '-':
            resultado = (f'{num_1} - {num_2} = {num_1 - num_2}')
        case '*':
            resultado = (f'{num_1} x {num_2} = {num_1 * num_2}')
        case '/':
            if num_2 == 0:
                resultado = (
                    f'\n¡Error matemático! \n¡¡¡No se puede dividir por cero!!!')
            else:
                resultado = (f'{num_1} / {num_2} = {num_1 / num_2}')
    print(resultado)
    return agregar_historial(historial, 'Calculadora Simple', str(resultado))


def sumatoria_promedio(historial):
    limpiar_consola()
    n = 1
    lista_numero = []
    resultado = ''
    while n != 0:
        n = float(input('Ingresa un número o 0 (cero) para terminar: '))
        if (n != 0):
            lista_numero.append(n)
            resultado = (lista_numero)
        else:
            suma = sum(lista_numero)
            promedio = suma / len(lista_numero)
            print()
            sumatoria = (f'La sumatoria es: {round(suma, 2)}')
            promedio = (f'Su promedio es: {round(promedio, 2)}')
            resultado = (f'{sumatoria} y {promedio}')
    print(resultado)
    return agregar_historial(historial, 'Calcular promedio', str(resultado))


def anio_bisiesto(historial):
    limpiar_consola()
    resultado = ''
    anio = int(input('Ingrese un año: '))
    bisiesto = 'Año Bisiesto' if ((anio % 4) == 0) & (
        (anio % 100) != 0) | ((anio % 400) == 0) else 'No Bisiesto'
    resultado = (f'El año {anio} es {bisiesto}')
    print(resultado)
    return agregar_historial(historial, 'Comprobar Año bisiesto', str(resultado))


def mayor_de_tres(historial):
    limpiar_consola()
    resultado = ''
    num_a = int(input('Ingrese un número '))
    num_b = int(input('Ingrese un segundo número '))
    num_c = int(input('Ingrese un tercer número '))
    if num_a > num_b & num_a > num_c:
        mensaje = 'El primer número ingresado es el mayor de los tres '
        resultado = (f'{(mensaje), (num_a), (num_b), (num_c)}')
    elif num_a < num_b & num_b > num_c:
        mensaje = 'El segudo número ingresado es el mayor de los tres '
        resultado = (f'{(mensaje), (num_a), (num_b), (num_c)}')
    elif num_a < num_c & num_c > num_b:
        mensaje = 'El tercer número ingresado es el mayor de los tres '
        resultado = (f'{(mensaje), (num_a), (num_b), (num_c)}')
    print(resultado)
    return agregar_historial(historial, 'Comprobar el Mayor de 3 n°', str(resultado))


def area_circulo(historial):
    limpiar_consola()
    resultado = ''
    r = float(input('Ingrese el radio del circulo '))
    Pi = 3.14159
    area = round(Pi * r**2, 2)
    resultado = (f'Para un circulo de radio {r} su área es {str(area)}')
    print(resultado)
    return agregar_historial(historial, 'Calcular área de un círculo', str(resultado))

def controlador_historial(historial):
    while True:
        vista_menu_historial()
        eleccion = input('Elige una opción (0-3): ')
        match eleccion:
            case '1':
                ver_historial(historial)
            case '2':
                editar_historial(historial)
            case'3':
                borrar_historial(historial)
            case '0':
                print('Saliendo de la aplicacion... \n  ¡Nos vemos!')
                break
            case _:
                print('\n_Opción no válida, porfavor intente de nuevo.')


def main(historial = []):
    if (len(historial) > 0):
        lista_historial = historial
    else:
        lista_historial = []
    while True:
        vista_menu()
        eleccion = input('Elige una opción (0-5): ')
        match eleccion:
            case '1':
                calculadora_simple(lista_historial)
            case '2':
                sumatoria_promedio(lista_historial)
            case'3':
                area_circulo(lista_historial)
            case '4':
                mayor_de_tres(lista_historial)
            case '5':
                anio_bisiesto(lista_historial)
            case '6':
                controlador_historial(lista_historial)
            case '0':
                print('Saliendo de la aplicacion... \n  ¡Nos vemos!')
                break
            case _:
                print('\n_Opción no válida, porfavor intente de nuevo.')


if __name__ == "__main__":
    main()
