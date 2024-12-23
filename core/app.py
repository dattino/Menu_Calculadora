from termcolor import colored


from controller.historial_controller import HistorialController


def calcular_operaciones_simple() -> str:
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
                    'Operación no válida, porfavor intente de nuevo.', 'light_red', attrs=['bold'])
                )
                return calcular_operaciones_simple()
        print(resultado)
        nombre = 'Calculadora Simple'
        operacion = str(resultado)
        HistorialController.agregar(nombre, operacion)
        return 
    except ValueError:
        msj_error = 'Entrada errónea, porfavor ingrese un número.'
        print(colored(msj_error, 'red'))
    return calcular_operaciones_simple()


def calcular_sumatoria_promedio() -> str:
    try:
        n = 1
        lista_numero = []
        resultado = ''
        while n != 0:
            n = float(input('Ingresa un número o 0 (cero) para terminar: '))
            if (n != 0):
                lista_numero.append(n)
                resultado = (lista_numero)
            elif (len(lista_numero) > 0):
                suma = sum(lista_numero)
                cantidad_de_numeros = len(lista_numero)
                promedio = suma / cantidad_de_numeros
                print()
                mensaje_sumatoria = (f'La sumatoria es: {round(suma, 2)}')
                mensaje_promedio = (f'Su promedio es: {round(promedio, 2)}')
                resultado = (
                    f'De {cantidad_de_numeros} n° {mensaje_sumatoria} Y {mensaje_promedio}')
                print(resultado)
                nombre = 'Calcular promedio'
                operacion = str(resultado)
                HistorialController.agregar(nombre, operacion)
                return
    except ValueError:
        msj_error = 'Entrada errónea, porfavor ingrese un número.'
        print(colored(msj_error, 'red'))
        return calcular_sumatoria_promedio()


def verificar_anio_bisiesto() -> str:
    try:
        resultado = ''
        anio = int(input('Ingrese un año: '))
        bisiesto = 'Año Bisiesto' if ((anio % 4) == 0) & (
            (anio % 100) != 0) | ((anio % 400) == 0) else 'No Bisiesto'
        resultado = (f'El año {anio} es {bisiesto}')
        print(resultado)
        nombre = 'Comprobar Año bisiesto'
        operacion = str(resultado)
        HistorialController.agregar(nombre, operacion)
        return
    except ValueError:
        msj_error = 'Entrada errónea, porfavor ingrese un número.'
        print(colored(msj_error, 'red'))
        return verificar_anio_bisiesto()


def calcular_mayor_de_tres() -> str:
    try:
        resultado = ''
        num_a = int(input('Ingrese un número '))
        num_b = int(input('Ingrese un segundo número '))
        num_c = int(input('Ingrese un tercer número '))
        if ((num_a > num_b) & (num_a > num_c)):
            mensaje = 'El primer número ingresado es el mayor de los tres'
            resultado = (f'{(mensaje), (num_a), (num_b), (num_c)}')
        elif ((num_a < num_b) & (num_b > num_c)):
            mensaje = 'El segudo número ingresado es el mayor de los tres'
            resultado = (f'{(mensaje), (num_a), (num_b), (num_c)}')
        elif ((num_a < num_c) & (num_c > num_b)):
            mensaje = 'El tercer número ingresado es el mayor de los tres'
            resultado = (f'{(mensaje), (num_a), (num_b), (num_c)}')
        print(resultado)
        nombre = 'Comprobar el Mayor de 3 n°'
        operacion = str(resultado)
        HistorialController.agregar(nombre, operacion)
        return
    except ValueError:
        msj_error = 'Entrada errónea, porfavor ingrese un número.'
        print(colored(msj_error, 'red'))
    return calcular_mayor_de_tres()


def calcular_area_circulo() -> str:
    try:
        resultado = ''
        r = float(input('Ingrese el radio del circulo '))
        Pi = 3.14159
        area = round(Pi * r**2, 2)
        resultado = (f'Para un circulo de radio {r} su área es {str(area)}')
        print(resultado)
        nombre = 'Calcular área de un círculo'
        operacion = str(resultado)
        HistorialController.agregar(nombre, operacion)
        return
    except ValueError:
        msj_error = 'Entrada errónea, porfavor ingrese un número.'
        print(colored(msj_error, 'red'))
    return calcular_area_circulo()
