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
    print('2. Promedio')
    print('3. Comprobar Año bisiesto')
    print('4. Comprobar el Mayor de 3 n°')
    print('5. Area de un círculo')
    print('0. Exit')


def volver_menu():
    input('\nPresione "Enter" para volver al menú...')
    return limpiar_consola()


def calculadora_simple():
    limpiar_consola()
    num_1 = int(input('Ingrese un número '))
    num_2 = int(input('Ingrese un segundo número '))
    operacion = input('Ingrese una operacion matemética (+, -, *, /) ')
    match  operacion:
        case '+':
            print(f'{num_1} + {num_2} = {num_1 + num_2}')
        case '-':
            print(f'{num_1} - {num_2} = {num_1 - num_2}')
        case '*':
            print(f'{num_1} x {num_2} = {num_1 * num_2}')
        case '/':
            if num_2 == 0:
                print('\n¡Error matemático! \n¡¡¡No se puede dividir por cero!!!')
            else:
                print(f'{num_1} / {num_2} = {num_1 / num_2}')
    return volver_menu()


def sumatoria_promedio():
    limpiar_consola()
    n = 1
    lista_numero = []
    while n != 0:
        n = float(input('Ingresa un número o 0 (cero) para terminar: '))
        if (n != 0):
            lista_numero.append(n)
            print(lista_numero)
        else:
            suma = sum(lista_numero)
            promedio = suma / len(lista_numero)
            print()
            print(f'La sumatoria es: {round(suma, 2)}')
            print(f'Su promedio es: {round(promedio, 2)}')
    return volver_menu()


def anio_bisiesto():
    limpiar_consola()
    anio = int(input('Ingrese un año: '))
    bisiesto = 'Año Bisiesto' if ((anio % 4) == 0) & (
        (anio % 100) != 0) | ((anio % 400) == 0) else 'No Bisiesto'
    print(f'\nEl año {anio} es {bisiesto}')
    return volver_menu()


def mayor_de_tres():
    limpiar_consola()
    num_a = int(input('Ingrese un número '))
    num_b = int(input('Ingrese un segundo número '))
    num_c = int(input('Ingrese un tercer número '))
    if num_a > num_b & num_a > num_c:
        print(f'El primer número ingresado es el mayor de los tres')
    elif num_a < num_b & num_b > num_c:
        print(f'El segudo número ingresado es el mayor de los tres')
    elif num_a < num_c & num_c > num_b:
        print(f'El tercer número ingresado es el mayor de los tres')
    return volver_menu()


def area_circulo():
    limpiar_consola()
    r = float(input('Ingrese el radio del circulo '))
    PI = 3.14159
    area = round(PI * r**2, 2)
    print(f'Para un circulo de radio {r} su área es {area}')
    return volver_menu()


def main():
    while True:
        vista_menu()
        eleccion = input('Elige una opción (0-5): ')
        match eleccion:
            case '1':
                calculadora_simple()
            case '2':
                sumatoria_promedio()
            case'3':
                anio_bisiesto()
            case '4':
                mayor_de_tres()
            case '5':
                area_circulo()
            case '0':
                print('Saliendo de la aplicacion. \nNos vemos...')
                break
            case _:
                print('\n Opción no válida, porfavor intente de nuevo.')


if __name__ == "__main__":
    main()
