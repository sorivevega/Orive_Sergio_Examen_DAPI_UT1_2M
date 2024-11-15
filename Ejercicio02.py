nombre = input('Inserta tu nombre completo: ')
name = nombre
name.split(' ')
print(name[-1: ])
word = input('Escriba una palabra: ')
letra = input('Escriba una vocal: ')
word_2 = word.replace(letra, letra.upper())
print(word_2)