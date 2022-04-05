#Saltarnos un paso con continue
iterator = 1
while iterator <= 100:
    iterator += 1
    if iterator % 3 == 0:
        continue
    print(iterator)
else:
    print("El iterator es mnor que 100")