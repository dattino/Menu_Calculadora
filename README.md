# Menu_Calculadora

## Acerca del proyecto:
Este proyecto está basado en Python 3.12.7, es un menú de calculadora donde se realizan diferentes tipos de operaciones como son calcular promedio, área de un circulo, funciones simple de suma resta multiplicación o división.
Cada entrada a estas operaciones se almacenan en un historial al cual se puede acceder desde el menu para realizar las funciones de CRUD sobre el historial.
Dicho historial posee persistencia sobre un archivo JSON para que una vez finalizado la ejecución del programa no se pierda el mismo.
en el cual se utilizan las clases, objetos y sus respectivos métodos.
Utiliza la dependencia de terceros termcolor Versión 2.4.0 para darle un entorno más amigable al uso de la terminal
### Operaciones que incluye
#### Calculadora Simple
Realiza operaciones de suma, resta, division y multiplicacion de números reales.
#### Calcular Promedio
Calcula el promedio de una lista de numero diferentges de cero, suma los mismo y los divide por la cantidad de numeros agregados.
#### Calcular Área de un circulo
Calcula el área de un circulo a partir de su radio tomando a Pi como 3.14159.
#### Comprobar el mayor de 3 números
Se ingresan 3 numeros y el programa indica cual de los 3 números ingresado es el mayor.
#### Comprobar año bisiesto
Se ingresa un año y el programa indica si es bisiesto o no.
 
### Pasos a seguir para su funcionamiento
#### 1. Crear un entorno virtual
Se debe ejecutar la siguiente linea de código por terminal ubicado sobre la carpeta raiz del proyecto
python -m  venv env
Luego para activarlo se ejecuta:
env\Scripts\activate
Para desactivarlo (solo de ser necesario) se ejecuta:
deactivate

#### 2. Instalar dependencias de terceros
Una vez creado el entorno virtual (Ver paso 1 y no ejecutar el comando "deactivate")
Se debe ejecutar la siguiente linea de código por terminal ubicado sobre la carpeta raiz del proyecto
pip install -r .\requirements.txt

#### 3. Ejecutar el programa
Se debe ejecutar la siguiente linea de código por terminal ubicado sobre la carpeta raiz del proyecto
python main.py

#### 4. Menu principal
Al ejecutar el comando del punto anterior se ingresa a un menu donde se puede realizar diferentes operaciones descriptas en el apartado: "Operaciones que incluye", detalladas mas arriba.
Aparte de las mencionadas operaciones se puede ingresar al menú del historial, si es que poseé alguna entrada previa, sino se indica con un mensaje que el historial no esta disponible.
También posee la opción de salir de dicho menú lo cual finaliza la ejecución del programa.

#### 5. Menu Historial
Este es un menú secundario al cual se ingresa atrabes de la opcion Menu Historial del menú principal.
En este menu se puede consultar el historial, solo si existe una entrada previa de alguna operación matemática.
Editar el historial, solo si existe una entrada previa de alguna operación matemática, la entrada editada queda marcada como que se a modificado y dicha marca no se puede alterar.
Y eliminar una entrada al historial, solo si existe una entrada previa de alguna operación matemática.
Al elejir la opcion 0 (cero) se vuelve al menú principal.

    

## Propietario:
Araya, Pablo.
