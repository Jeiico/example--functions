# funcion print() imprime el objeto dado en el dispositivo de salida estándar (pantalla) o en el archivo de flujo de texto.
print(5 != 5)
print(12 == 12)
print(25 // 10)

# funcion input() toma la entrada del usuario y la devuelve.
name = input("Please, enter your name: ")
print("Your name is " + name + "!")

# funcion sum()  agrega los elementos de un iterable y devuelve la suma.
def sumar(primero, segundo):
    return primero + segundo

print(sumar(1, 2))


# funcion map() aplica una función determinada a cada elemento de un iterable (lista, tupla, etc.) y devuelve un iterador que contiene los resultados.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x * 2, lista)))

# funcion filter() función selecciona elementos de un iterable (lista, tupla, etc.) en función de la salida de una función.
def square(x):
    return x * 2

print(list(filter(square, lista)))

# funcion min() devuelve el elemento más pequeño en un iterable. También se puede utilizar para encontrar el elemento más pequeño entre dos o más parámetros.
numbers = [5,7,9,-25,-123,78]
smallest_number = min(numbers)

print(smallest_number)


# funcion max() devuelve el elemento más grande en un iterable. También se puede utilizar para encontrar el elemento más grande entre dos o más parámetros.
numbers = [5,7,9,-25,-123,78]
largest_number = max(numbers)

print(largest_number)

# funcion len() función devuelve el número de elementos (longitud) en un objeto.
languages = ["emilio","aristobulo petty", "benito arias", "colombia", "doña transito", "tio profilio", "armando casas", "sacarias piedras del rio"]
leng = len(languages)

print(leng)

# funcion enumerate() función agrega un contador a un iterable y lo devuelve (el objeto de enumeración).
languages = ["emilio","aristobulo petty", "benito arias", "colombia", "doña transito", "tio profilio", "armando casas", "sacarias piedras del rio"]

enumerate_prime = enumerate(languages)
print(list(enumerate_prime))

# funcion range() función devuelve una secuencia de números entre el rango dado.
numbers = range(50)
print(list(numbers))

# funcion id() método devuelve un entero único (identidad) de un objeto de argumento pasado.
vegetables = ("zanahoria", "basil", "cabbage", "broccoli", "tomato", "avocado")

print("The id of the vegetables set is", id(vegetables))

# funcion chr() método convierte un número entero en su carácter Unicode y lo devuelve.
print(chr(97))
print(chr(82))
print(chr(52))

# funcion abs() devuelve el valor absoluto del número dado. Si el número es un número complejo, abs()devuelve su magnitud.
integer = -1000
print('Absolute value of -1000 is:', abs(integer))

floating = -100.3
print('Absolute value of -100.3 is:', abs(floating))

# funcion reversed() método calcula el reverso de un objeto de secuencia dado y lo devuelve en forma de lista.
red_string = "benito"
print(list(reversed(red_string)))

blue_number = ['8', '12558', '7842', '155','t','o']
print(list(reversed(blue_number)))

# funcion round() devuelve un número de coma flotante redondeado al número especificado de decimales
number = 14.25
rounded_number = round(number)
print(rounded_number)

# Str método devuelve la representación de cadena de un objeto dado.
print(str('1993'))
print(str('sonic'))
print(str('swim'))

# funcion set() crea un conjunto en Python.
list_numbers = [2,4,6,8,10,12]
numbers_set = set(list_numbers)
print(numbers_set)

# funcion int() convierte un número o una cadena en su entero equivalente.
result = int(10.12)
print('int(10.12):',result)

# funcion type() devuelve el tipo del objeto o devuelve un nuevo tipo de objeto basado en los argumentos pasados.
prime_number = [1,10,25,56,789]

result = type(prime_number)
print(result)

# El constructor dict() crea un diccionario en Python
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

# El list()constructor devuelve una lista en Python.

vowel_string = 'aeiou'
print(list(vowel_string))


vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))


vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))

# tuple() es un tipo de secuencia inmutable. Una de las formas de crear tuplas es usando la tuple()construcción.

""" crear una tupla a partir de una lista """ 
t2 = tuple([1, 4, 6])
print('t2 =', t2)

"""  creando una tupla a partir de una cadena """ 
t1 = tuple('Python')
print('t1 =',t1)

"""  crear una tupla a partir de un diccionario """ 
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)

# float() método devuelve un número de punto flotante de un número o una cadena.
number = 10
print('float(10):',float(number))

# eval() método analiza la expresión pasada a este método y ejecuta la expresión (código) de Python dentro del programa.
number = 50

square_number = eval('number * number')
print(square_number)

# open() abre el archivo (si es posible) y devuelve el objeto de archivo correspondiente.
"""
'r'	Abre un archivo para leer. (por defecto)
'w'	Abre un archivo para escribir. Crea un nuevo archivo si no existe o trunca el archivo si existe.
'x'	Abra un archivo para la creación exclusiva. Si el archivo ya existe, la operación falla.
'a'	Abrir para agregar al final del archivo sin truncarlo. Crea un nuevo archivo si no existe.
't'	Abrir en modo texto. (por defecto)
'b'	Abrir en modo binario.
'+'	Abrir un archivo para actualizar (lectura y escritura)
"""

file_name = open("path_to_file", mode='r')
print(file_name)

file_name = open("path_to_file", mode='w')

file_name = open("path_to_file", mode='a')

file_name = open("text.txt", mode='t')



# all() devuelve el valor absoluto del número dado. Si el número es un número complejo, abs()devuelve su magnitud.
boolean_list = ['True', 'True', 'True']

result = all(boolean_list)
print(result)

boolean_list = ['True', 'True', 'False', 'False']

result = all(boolean_list)
print(result)

