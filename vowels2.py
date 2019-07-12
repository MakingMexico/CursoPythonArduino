text = input('Ingrese un texto: ').lower()

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letter in text:
    if letter == 'a':
        contador_a += 1
    elif letter == 'e':
        contador_e += 1
    elif letter == 'i':
        contador_i += 1
    elif letter == 'o':
        contador_o += 1
    elif letter == 'u':
        contador_u += 1

print("Hay {} a".format(contador_a))
print("Hay {} e".format(contador_e))
print("Hay {} i".format(contador_i))
print("Hay {} o".format(contador_o))
print("Hay {} u".format(contador_u))
