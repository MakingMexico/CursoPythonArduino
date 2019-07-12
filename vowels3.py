texto = input('Ingrese un texto: ').lower()

vowels = {
    "contador_a": 0,
    "contador_e": 0,
    "contador_i": 0,
    "contador_o": 0,
    "contador_u": 0,
}

for letter in texto:
    if letter == 'a':
        vowels["contador_a"] += 1
    elif letter == 'e':
        vowels["contador_e"] += 1
    elif letter == 'i':
        vowels["contador_i"] += 1
    elif letter == 'o':
        vowels["contador_o"] += 1
    elif letter == 'u':
        vowels["contador_u"] += 1

resultado = "Hay {a} a\nHay {e} e\nHay {i} i\nHay {o} o\nHay {u} u".format(
    e=vowels["contador_e"],
    u=vowels["contador_u"],
    o=vowels["contador_o"],
    a=vowels["contador_a"],
    i=vowels["contador_i"],
)

print(resultado)
