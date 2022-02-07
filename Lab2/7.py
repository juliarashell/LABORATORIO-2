#Ejercico 7

multiplos = 0
for j in range(1001):
    if j % 7 == 0 and j != 0:
          multiplos += 1

print(f"Los multiplos con un rango son: {multiplos}")

multiplos = 0
for j in range(7, 80, 6):
        if j % 7 == 0 and j != 0:
           multiplos += 1

print(f"Los multiplos con tres rangos son: {multiplos}")