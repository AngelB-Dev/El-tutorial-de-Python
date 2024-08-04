base = 15
altura = 8
area_rectangulo = base * altura

print(f'''
1. Calcula el área de un rectángulo con base {base} y altura {altura}.

Para calcular el área del rectángulo, primero plasmamos los datos.
Datos:
Base = {base}
Altura = {altura}

Ya con ello usamos la fórmula para calcular.
Base * Altura = Área

El área del rectángulo es: {area_rectangulo}
''')



numerador = 100
denominador = 6
resultado = numerador / denominador

print(f'''
2. Divide {numerador} entre {denominador} y muestra el resultado como número decimal.

Definimos los números {numerador} y {denominador} para realizar la división y presentar el resultado con cuatro decimales:

El resultado de dividir {numerador} entre {denominador} es: {resultado:.4f}
''')



grupo = 4
elementos = 30
completos = elementos//grupo
sobrantes = elementos % grupo

print(f'''
3. Calcula cuántos grupos completos de {grupo} elementos se pueden formar con un total de {elementos} elementos y cuántos elementos sobran.

Para el total de {elementos} elementos:
- Se pueden formar {completos} grupos de {grupo} elementos cada uno.
- Quedan {sobrantes} elementos sobrantes.

Este cálculo utiliza:
- La división entera (//) para obtener el número de grupos completos.
- El módulo (%) para determinar los elementos sobrantes.

Ejemplo adicional:
Si tenemos 50 elementos y queremos formarlos en grupos de 7:
- Grupos completos: {50 // 7} = {50 // 7}
- Elementos sobrantes: {50 % 7} = {50 % 7}
''')


calculo = 3**3

print(f'''
4. Eleva 3 al cubo.

Para calcular 3 elevado al cubo, usamos la operación de potencia: 3**3.

El resultado es {calculo}. Por lo tanto:
- Tres elevado al cubo es {calculo}.

Este cálculo utiliza:
- La operación de potencia (**), que eleva el número 3 a la tercera potencia.

Ejemplo adicional:
- Para elevar 2 al cubo:
  - El cálculo sería: 2**3
  - El resultado es: {2**3}
''')



total = 80
porcentaje = 15
resultado = (porcentaje / 100) * total

print(f'''
5. Calcula el 15% de 80 utilizando operaciones aritméticas básicas.

El {porcentaje}% de {total} es: {resultado}
''')



suma = (1 + 2 + 3 + 4 + 5)
resultado_final = suma * 2

print(f'''
6. Suma los números del 1 al 5 y luego multiplica el resultado por 2.

La suma de los números del 1 al 5 es: {suma}
El resultado final (suma * 2) es: {resultado_final}
''')


numero = 64
divisor = 8
residuo = numero % divisor

if residuo == 0:
    mensaje = f'{numero} es divisible por {divisor}.'
else:
    mensaje = f'{numero} no es divisible por {divisor}.'

print(f'''
7. Determina si 64 es divisible por 8 utilizando el operador de módulo

{mensaje}
''')
