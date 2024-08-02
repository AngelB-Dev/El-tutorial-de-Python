print('1. Crea una cadena que incluya un diálogo, utilizando comillas dobles para la cadena principal y comillas simples para las palabras del personaje.')
dialogo = "El profesor dijo: 'Recuerden entregar sus tareas mañana'"
print(f'{dialogo}\n')

print('2. Define una cadena de texto que represente un poema corto de tres líneas, usando triple comillas y caracteres de escape para el formato.')
poema = """Rosas rojas,\nVioletas azules,\nPython es genial\ny tú también lo eres."""
print(f'{poema}\n')

print('3. Crea una cadena sin formato (raw string) que represente una expresión regular simple, por ejemplo, para encontrar números de teléfono.')
regex_telefono = r'\d{3}-\d{3}-\d{4}'
print(f'{regex_telefono}\n')

print('4. Combina tres variables de cadena diferentes para formar una dirección de correo electrónico completa.')
nombre = "usuario"
dominio = "ejemplo"
extension = "com"
email = f"{nombre}@{dominio}.{extension}"
print(f'{email}\n')

print('5. Crea una cadena que repita un emoji (por ejemplo, 😊) cinco veces utilizando operadores de cadena.')
emoji = "😊"
emoji_repetido = emoji * 5
print(f'{emoji_repetido}\n')

print('6. Define una cadena larga que represente un párrafo de un artículo, dividiéndola en múltiples líneas de código pero que se muestre como un párrafo continuo al imprimirla.')
parrafo = ("Python es un lenguaje de programación versátil y poderoso. "
           "Es conocido por su sintaxis clara y legible, lo que lo hace "
           "ideal para principiantes y expertos por igual. Python se utiliza "
           "en una amplia gama de aplicaciones, desde desarrollo web hasta "
           "inteligencia artificial y análisis de datos.")
print(f'{parrafo}\n')

print('7. Demuestra la diferencia entre usar len() en una cadena con caracteres Unicode (como emojis) y en una cadena con solo caracteres ASCII.')
cadena_ascii = "Hola, mundo!"
cadena_unicode = "Hola, mundo! 😊🐍"
print(f"Longitud de cadena ASCII: {len(cadena_ascii)}")
print(f"Longitud de cadena Unicode: {len(cadena_unicode)}")
