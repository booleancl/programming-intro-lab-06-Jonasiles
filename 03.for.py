#ejemplo de estructura para iterar utilizando secuencias de cosas
#litas


drinks = ["Mojito","Margarita","Piña Colada"]
for drink in drinks:
    print(drink)

print("####")
# El for tambin funciona con letter
for letter in "Tio Charlie":
    print(letter)

print("####")

#El for tambien puede ser usado con el break
for drink in drinks:
    if drink == "Margarita":
        break
    print(drink)

print("####")

#continue
for drink in drinks:
    if drink == "Margarita":
        continue
    print(drink)
else:
    print("Bertha se termino las margaritas")

print("####")

# for aninador
sizes = ["normal", "Large", "Tio Charlie XL"]
for size in sizes:
    for drink in drinks:
        print(drink,size)