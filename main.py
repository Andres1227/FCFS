tiempo_proceso = []

n = int(input('Ingresa el numero de procesos: '))
for i in range(n):
    tiempo_proceso.append(
        int(input("Ingrese el tiempo del proceso " + str(i) +
                  ": ")))  #Agregamos el proceso

print(tiempo_proceso)
tiempo_espera = []
tiempo_respuesta = []
espera_promedio = 0
respuesta_promedio = 0
tiempo_espera.append(0)
tiempo_respuesta.append(tiempo_proceso[0])

for i in range(1, n):
    tiempo_espera.append(tiempo_espera[i - 1] + tiempo_proceso[i - 1])
    tiempo_respuesta.append(tiempo_espera[i] + tiempo_proceso[i])
    espera_promedio += tiempo_espera[i]
    respuesta_promedio += tiempo_respuesta[i]

print("Pr\tTP\tTE\tTR")
for i in range(n):
    print(
        i, tiempo_proceso[i], tiempo_espera[i], tiempo_respuesta[i], sep="\t")
print("Espera Promedio:", espera_promedio / n, sep="\t")
print("Respuesta Promedio:", respuesta_promedio / n, sep="\t")
