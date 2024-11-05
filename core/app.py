from termcolor import colored


from core.crud_historial import *


def calcular_operaciones_simple(historial) -> str:
    try:
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
            case _:
                print(colored(
                    'Operación no válida, porfavor intente de nuevo.', 'light_red', attrs=['bold']))
                return calcular_operaciones_simple(historial)
        print(resultado)
        return agregar_historial(historial, 'Calculadora Simple', str(resultado))
    except ValueError:
        print(colored('Entrada errónea, porfavor ingrese un número.',
              'light_red', attrs=['bold']))
        calcular_operaciones_simple(historial)
    return


def calcular_sumatoria_promedio(historial) -> str:
    try:
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
                cantidad_de_numeros = len(lista_numero)
                promedio = suma / cantidad_de_numeros
                print()
                mensaje_sumatoria = (f'La sumatoria es: {round(suma, 2)}')
                mensaje_promedio = (f'Su promedio es: {round(promedio, 2)}')
                resultado = (
                    f'De {cantidad_de_numeros} n° {mensaje_sumatoria} Y {mensaje_promedio}')
        print(resultado)
        return agregar_historial(historial, 'Calcular promedio', str(resultado))
    except ValueError:
        print(colored('Entrada errónea, porfavor ingrese un número.',
              'light_red', attrs=['bold']))
        calcular_sumatoria_promedio(historial)
    return


def verificar_anio_bisiesto(historial) -> str:
    try:
        resultado = ''
        anio = int(input('Ingrese un año: '))
        bisiesto = 'Año Bisiesto' if ((anio % 4) == 0) & (
            (anio % 100) != 0) | ((anio % 400) == 0) else 'No Bisiesto'
        resultado = (f'El año {anio} es {bisiesto}')
        print(resultado)
        return agregar_historial(historial, 'Comprobar Año bisiesto', str(resultado))
    except ValueError:
        print(colored('Entrada errónea, porfavor ingrese un número.',
              'light_red', attrs=['bold']))
        verificar_anio_bisiesto(historial)
    return


def calcular_mayor_de_tres(historial) -> str:
    try:
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
    except ValueError:
        print(colored('Entrada errónea, porfavor ingrese un número.',
              'light_red', attrs=['bold']))
        calcular_mayor_de_tres(historial)
    return


def calcular_area_circulo(historial) -> str:
    limpiar_consola()
    try:
        resultado = ''
        r = float(input('Ingrese el radio del circulo '))
        Pi = 3.14159
        area = round(Pi * r**2, 2)
        resultado = (f'Para un circulo de radio {r} su área es {str(area)}')
        print(resultado)
        return agregar_historial(historial, 'Calcular área de un círculo', str(resultado))
    except ValueError:
        print(colored('Entrada errónea, porfavor ingrese un número.',
              'light_red', attrs=['bold']))
        calcular_area_circulo(historial)
    return
