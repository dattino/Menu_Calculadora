import os

lista_historial = []


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
    print('2. Promedio')
    print('3. Comprobar Año bisiesto')
    print('4. Comprobar el Mayor de 3 n°')
    print('5. Area de un círculo')
    print('6. Historial')
    print('0. Exit')


def volver_menu():
    input('\nPresione "Enter" para volver al menú...')
    return limpiar_consola()


def historial(valor_almacenar):
    if ((type(valor_almacenar) != None) & (valor_almacenar != len(lista_historial))):
        lista_historial.append(valor_almacenar)
    elif ((type(valor_almacenar) != None) & (valor_almacenar == len(lista_historial))):
        lista_historial.append('Ingreso a "Ver el historial"')
        n = 1
        posicion = 1
        while posicion != -1:
            posicion = len(lista_historial) - n
            print(lista_historial[posicion])
            n = n + 1
    return volver_menu()


def calculadora_simple():
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
    return (f'Ingreso a "Calculadora Simple" {resultado}')


def sumatoria_promedio():
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
    return (f'Ingreso a "Calcular un promedio" {resultado}')


def anio_bisiesto():
    limpiar_consola()
    resultado = ''
    anio = int(input('Ingrese un año: '))
    bisiesto = 'Año Bisiesto' if ((anio % 4) == 0) & (
        (anio % 100) != 0) | ((anio % 400) == 0) else 'No Bisiesto'
    resultado = (f'El año {anio} es {bisiesto}')
    print(resultado)
    return (f'Ingreso a "Comprobar Año bisiesto" {resultado}')


def mayor_de_tres():
    limpiar_consola()
    resultado = ''
    num_a = int(input('Ingrese un número '))
    num_b = int(input('Ingrese un segundo número '))
    num_c = int(input('Ingrese un tercer número '))
    if num_a > num_b & num_a > num_c:
        resultado = (f'El primer número ingresado es el mayor de los tres {
                     (num_a), (num_b), (num_c)}')
    elif num_a < num_b & num_b > num_c:
        resultado = (f'El segudo número ingresado es el mayor de los tres {
                     (num_a), (num_b), (num_c)}')
    elif num_a < num_c & num_c > num_b:
        resultado = (f'El tercer número ingresado es el mayor de los tres {
                     (num_a), (num_b), (num_c)}')
    print(resultado)
    return (f'Ingreso a "Comprobar el Mayor de 3 n°" {resultado}')


def area_circulo():
    limpiar_consola()
    resultado = ''
    r = float(input('Ingrese el radio del circulo '))
    Pi = 3.14159
    area = round(Pi * r**2, 2)
    resultado = (f'Para un circulo de radio {r} su área es {str(area)}')
    print(resultado)
    return (f'Ingreso a "Area de un círculo" {resultado}')


def main():
    while True:
        vista_menu()
        eleccion = input('Elige una opción (0-5): ')
        match eleccion:
            case '1':
                historial(calculadora_simple())
            case '2':
                historial(sumatoria_promedio())
            case'3':
                historial(anio_bisiesto())
            case '4':
                historial(mayor_de_tres())
            case '5':
                historial(area_circulo())
            case '6':
                historial(len(lista_historial))
            case '0':
                print('Saliendo de la aplicacion. \nNos vemos...')
                break
            case _:
                print('\n Opción no válida, porfavor intente de nuevo.')


if __name__ == "__main__":
    main()
