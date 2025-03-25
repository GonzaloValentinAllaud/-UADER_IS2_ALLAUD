#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Definir los límites del intervalo
lower = 1
upper = 500

# Imprimir el rango de búsqueda
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   # Los números primos son mayores que 1
   if num > 1:
       # Verificar si el número es divisible por algún otro número menor que él
       for i in range(2, num):
           if (num % i) == 0: # Si es divisible, no es primo
               break # Salir del bucle si encuentra un divisor
       else:
           # Si no se encontró ningún divisor, es un número primo
           print(num)
