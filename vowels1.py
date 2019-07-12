"""Programa para contar vocales."""
texto = input('Ingrese un texto: ').lower()

contador = 0

for letter in texto:
    if letter in 'aeiou':
        contador += 1

print("Hay {} vocales".format(contador))
