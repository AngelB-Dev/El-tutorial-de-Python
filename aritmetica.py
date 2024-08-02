print('1. Calcula el área de un rectángulo con base 15 y altura 8.\n\nPara calcular el área del rectángulo, primero plasmamos los datos.\nDatos:')

base = 15
altura = 8
print(f' Base = {base}\n Altura = {altura}')

area_rectangulo = base * altura
print( '\nYa con ello usamos la fórmula para calcular.\nBase * Altura = Área')

print(f'\nEl área del rectángulo es: {area_rectangulo}\n')





print('2. Divide 100 entre 6 y muestra el resultado como número decimal.\n\nDefinimos los numeros "100" y "6" para dividir y mostrar el resultado float:')

numerador = 100
denominador = 6

resultado = numerador / denominador

print(f' El resultado de dividir {numerador} entre {denominador} es: {resultado:.4f}\n')





print('3. Calcula cuántos grupos completos de 4 se pueden formar con 30 elementos y cuántos elementos sobran.\n')

grupo = 4
elementos = 30

completos = elementos//grupo
sobrantes = elementos % grupo

print('Grupos completos de 4 elementos:', completos)
print('Elementos sobrantes:', sobrantes)





print('\n4. Eleva 3 al cubo.\n')
calculo = 3**3
print(f'Tres elevado al cubo es {calculo}')





print('\n5. Calcula el 15% de 80 utilizando operaciones aritméticas básicas.\n')

total = 80
porcentaje = 15

resultado = (porcentaje / 100) * total

print(f'El {porcentaje}% de {total} es: {resultado}\n')





print('6. Suma los números del 1 al 5 y luego multiplica el resultado por 2.\n')

suma = 1 + 2 + 3 + 4 + 5

resultado_final = suma * 2

print(f'La suma de los números del 1 al 5 es: {suma}')
print(f'El resultado final (suma * 2) es: {resultado_final}\n')





print('7. Determina si 64 es divisible por 8 utilizando el operador de módulo.\n')

numero = 64
divisor = 8

residuo = numero % divisor

mensaje_divisible = f'{numero} es divisible por {divisor}.'
mensaje_no_divisible = f'{numero} no es divisible por {divisor}.'

print(mensaje_divisible[:(len(mensaje_divisible) - residuo * len(mensaje_divisible))] + 
      mensaje_no_divisible[:(residuo * len(mensaje_no_divisible))])