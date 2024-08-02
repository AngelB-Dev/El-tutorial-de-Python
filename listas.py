print('1. Crea una lista llamada primes con los primeros 5 números primos y luego imprime el tercer elemento de la lista.')
primes = [2, 3, 5, 7, 11]
print(f'{primes[2]}\n')

print('2. Dada la lista temperatures = [20, 25, 18, 30, 15], corrige el valor incorrecto (18) reemplazándolo por la temperatura correcta de 28.')
temperatures = [20, 25, 18, 30, 15]
temperatures[2] = 28
print(f'{temperatures}\n')

print('3. Crea una lista llamada fruits con tres frutas, y luego añade dos frutas más al final de la lista utilizando el método append().')
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.append("kiwi")
print(f'{fruits}\n')

print('4. Haz una copia superficial de una lista de animales y demuestra que agregar un elemento a la copia no afecta a la lista original.')
animals = ["dog", "cat", "bird"]
animals_copy = animals[:]
animals_copy.append("fish")
print(f"Original: {animals}")
print(f"Copia: {animals_copy}\n")

print('5. Crea una lista de números del 1 al 7, luego reemplaza los elementos en las posiciones 3 a 5 (inclusive) por sus cuadrados.')
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[3:6] = [16, 25, 36]
print(f'{numbers}\n')

print('6. Crea una lista anidada que contenga dos sublistas: una con los días de la semana laboral y otra con los días del fin de semana. Luego, accede e imprime el primer día del fin de semana.')
week = [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["Saturday", "Sunday"]]
print(f'{week[1][0]}\n')

print('7. Escribe un programa que genere e imprima una lista de los primeros 8 números triangulares (1, 3, 6, 10, 15, 21, 28, 36).')
triangular = [1, 3, 6, 10, 15, 21, 28, 36]
print(f'{triangular}\n')
